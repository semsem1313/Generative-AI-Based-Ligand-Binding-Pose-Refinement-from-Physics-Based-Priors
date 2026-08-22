import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

#this dict will contain accession id : protein family
uniprot_ids={
    "P56390":"Kinases", "P35968":"Kinases", "P61024":"Kinases", "P08463":"Kinases",

    "P00698":"Lysozyme", "P61626":"Lysozyme","P08905":"Lysozyme", "P00695":"Lysozyme",

    "P20853":"Cytochromes", "P08684":"Cytochromes", "P05181":"Cytochromes","P69490":"Cytochromes",

    "P01597":"Immunoglobulins", "P01615":"Immunoglobulins", "P01764":"Immunoglobulins", "P01825":"Immunoglobulins",

    "P00760": "Protease", "P00766": "Protease", "P00772": "Protease", "P00761": "Protease"
}

#now using the rest api of fasta we can get the sequences of these acc ids directly
def get_seq(acc):
    url=f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
    try:
        res=requests.get(url)
        res.raise_for_status()
        return "".join(line.strip() for line in res.text.splitlines() if not line.startswith(">"))
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {acc}:{e}")
        return ""

#this dict will contain accession id : protein sequence
sequences={acc:get_seq(acc) for acc in uniprot_ids}
sequences={acc: seq for acc, seq in sequences.items() if len(seq) > 0}

missing = set(uniprot_ids.keys()) - set(sequences.keys())
if missing:
    print(f"Skipping empty/failed sequences: {missing}\n")

#now we will start with the pairwise sequence identity
from Bio import Align
aligner=Align.PairwiseAligner(mode='global')
acc_list=list(sequences.keys())
n=len(acc_list)
seq_matrix=pd.DataFrame(index=acc_list,columns=acc_list,dtype=float) #n*n matrix with both rows and columns as acc ids
#main loop
for i in range(n):
    for j in range(i,n):
        id1,id2=acc_list[i],acc_list[j]
        seq1,seq2=sequences[id1],sequences[id2]
        if i==j:
            score=100.0
        else:
            alignment=aligner.align(seq1,seq2)[0]
            try:
                matches=alignment.counts().identities
            except AttributeError:
                matches=alignment.counts().id
            
            score=(matches/min(len(seq1),len(seq2)))*100
        seq_matrix.loc[id1,id2]=score
        seq_matrix.loc[id2,id1]=score
#for heatmap
families = pd.Series([uniprot_ids[acc] for acc in acc_list], index=acc_list)
unique_fams = families.unique()
colors = sns.color_palette("husl", len(unique_fams))
family_to_color = dict(zip(unique_fams, colors))
row_colors = families.map(family_to_color)

sns.clustermap(
    seq_matrix.astype(float),
    method='average',
    cmap='viridis',
    row_colors=row_colors,
    col_colors=row_colors
)
plt.show()