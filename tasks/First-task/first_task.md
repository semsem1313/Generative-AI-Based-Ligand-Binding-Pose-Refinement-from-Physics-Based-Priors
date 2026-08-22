## Task 1
**Protein sequence similarity and clustering**

- Download 20-30 protein sequences belonging to 3-4 different protein families from
UniProt.
- Calculate pairwise sequence identity or similarity.
- Construct a similarity matrix and visualize it as a heatmap.
- Use hierarchical clustering to group the proteins.
- Compare whether the computational clusters correspond to the known protein
families.

## My Procedure
1. first i researched some protein families on the net and then searched them up on UniProt
2. Then I scrolled down and noted their accession id (Pfam identifier)
3. My procedure is that im gonna search up 5 protein families and get 4 from each my families are: Kinases, G-Protein Coupled Receptors (GPCRs), Cytochromes, Immunoglobulins, ATP Synthases
4. I foundout about FastaAPI and how we can use it to get the sequence of protein so whaat i did was i thought of using the accession id and then fetch the api to get the corresponding sequence. i couldve actually fetched the sequence from website only but i found this as a shortcut
5. I went through the biopython lib and read thru the pairwise sequence alignment




new:{
    "P56390":"Kinases", "P35968":"Kinases", "P61024":"Kinases", "P08463":"Kinases",

    "P00698":"Lysozyme", "P61626":"Lysozyme","P08905":"Lysozyme", "P00695":"Lysozyme",

    "P20853":"Cytochromes", "P08684":"Cytochromes", "P05181":"Cytochromes","P69490":"Cytochromes",

    "P01597":"Immunoglobulins", "P01615":"Immunoglobulins", "P01764":"Immunoglobulins", "P01825":"Immunoglobulins",

    "P00760": "Protease", "P00766": "Protease", "P00772": "Protease", "P00761": "Protease"
}

old: {"P68871": "Globin", "P02042": "Globin", "P01942": "Globin", "P02144": "Globin",
    "P00004": "Cytochrome_C", "P99999": "Cytochrome_C", "P00008": "Cytochrome_C", "P00011": "Cytochrome_C",
    "P00698": "Lysozyme", "P61626": "Lysozyme", "P08905": "Lysozyme", "P00695": "Lysozyme",
    "P00760": "Protease", "P00766": "Protease", "P00772": "Protease", "P00761": "Protease"}