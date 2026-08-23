import numpy as np
import matplotlib.pyplot as plt
from Bio.PDB import PDBParser, PDBList
from scipy.spatial.distance import pdist, squareform
import os

#retrieving protein structure
pdb_ids=['1MBA','1HLB','2ZTA','2OMF','1CDO','1G6N']
pdbl=PDBList()
for pdb_id in pdb_ids:
    pdbl.retrieve_pdb_file(pdb_id,pdir='pdb_files',file_format='pdb')

#extracting the Ca coordinates
def get_ca_coords(pdb_id, filepath):
    parser=PDBParser(QUIET=True)
    structure=parser.get_structure(pdb_id, filepath)
    model=structure[0]
    chain=next(model.get_chains())
    
    ca_coords=[]
    for x in chain:
        if 'CA' in x:
            ca_coords.append(x['CA'].get_coord())
    return np.array(ca_coords)

#calculating pairwise dist and using squareform
def calc_distance_matrix(coords):
    return squareform(pdist(coords))

cutoff=8.0

#ploting the contact map
fig,axes=plt.subplots(2,3, figsize=(12,8))
axes=axes.flatten()  # Flatten 2D array of axes to 1D for easy looping

for idx,pdb_id in enumerate(pdb_ids):
    filepath=f"pdb_files/pdb{pdb_id.lower()}.ent"
    
    if not os.path.exists(filepath):
        print(f"File missing for {pdb_id},skipping...")
        continue
    #building contact map    
    coords=get_ca_coords(pdb_id,filepath)
    dist_matrix=calc_distance_matrix(coords)
    contact_map=dist_matrix<cutoff
    
    # Plot each map into its own subplot quadrant
    axes[idx].imshow(contact_map,cmap='Greys',origin='lower')
    axes[idx].set_title(f"Contact Map: {pdb_id}")
    axes[idx].set_ylabel("Residue Index")
plt.tight_layout()
plt.show()