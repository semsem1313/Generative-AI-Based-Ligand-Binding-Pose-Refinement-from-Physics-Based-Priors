#our main steps
# 1. load the complex.pdb file
# 2. find the ligand
# 3. find the pocket and get the com
# 4. find the size using Xmax - Xmin
# 5. seperate protein and ligand pdb files
# 6. create vina_config and update with necessary infos for docking


import mdtraj as md
import numpy as np

input_pdb="1hsg_complex.pdb"
cutoff=0.5   #this is in nm
protein_output="protein-receptor.pdb"
ligand_output="ligand.pdb"

unec_residue={'HOH'}


#loading complex

traj=md.load(input_pdb)
top=traj.topology


ligand_candidates = [res for res in top.residues if res.name=='MK1']
if not ligand_candidates:
    raise ValueError("No ligand found! Check the PDB file.")


print(ligand_candidates)

ligand_res = ligand_candidates[0]
ligand_resname = ligand_res.name


#we will now work on the com calculation

ligand_indices = top.select(f'resname {ligand_resname}')
protein_indices = top.select('protein')

neighbors=md.compute_neighbors(
          traj,
          cutoff=cutoff,
          query_indices=ligand_indices,
          haystack_indices=protein_indices,
          periodic=False
)

neighbor_atom_indices = neighbors[0]


pocket_residues=set()

for atom_idx in neighbor_atom_indices:
        res = top.atom(atom_idx).residue
        pocket_residues.add((res.name, res.resSeq,
        res.chain.index, res.index))
print(f"  Unique binding pocket residues: {len(pocket_residues)}")


pocket_resids = [str(resid) for _, _, _, resid in pocket_residues]
pocket_selection = 'resid ' + ' '.join(pocket_resids)

com_nm = md.compute_center_of_mass(traj, select=pocket_selection)
com_angstrom = com_nm[0]*10.0

print(f"  COM (Angstroms):   x={com_angstrom[0]:.3f}, y={com_angstrom[1]:.3f}, z={com_angstrom[2]:.3f}")

# getting the (x,y,z) coordinates of the pocket atoms
pocket_coords_nm = traj.xyz[0,neighbor_atom_indices,:]
# finding the min and max coords along each axis
min_coords_nm = np.min(pocket_coords_nm, axis=0)
max_coords_nm = np.max(pocket_coords_nm, axis=0)
# size = max-min
box_size_ang = (max_coords_nm-min_coords_nm) * 10.0 #in angstorm
# adding a buffer
buffer_space = 5.0
size_x = box_size_ang[0] + buffer_space
size_y = box_size_ang[1] + buffer_space
size_z = box_size_ang[2] + buffer_space
print(f"  Final Size (with buffer)  : x={size_x:.2f} y={size_y:.2f} z={size_z:.2f}")



#seperating protein and ligand files from the complex
protein_traj = traj.atom_slice(protein_indices)
protein_traj.save_pdb(protein_output)
ligand_traj = traj.atom_slice(ligand_indices)
ligand_traj.save_pdb(ligand_output)


with open('vina_config.txt', 'w') as f:
    f.write(f"receptor = protein-receptor.pdbqt\n")
    f.write(f"ligand = ligand.pdbqt\n\n")
    f.write(f"center_x = {com_angstrom[0]:.3f}\n")
    f.write(f"center_y = {com_angstrom[1]:.3f}\n")
    f.write(f"center_z = {com_angstrom[2]:.3f}\n\n")
    f.write(f"size_x = {size_x:.3f}\n")
    f.write(f"size_y = {size_y:.3f}\n")
    f.write(f"size_z = {size_z:.3f}\n\n")
    f.write(f"exhaustiveness = 32\n")
    f.write(f"num_modes = 9\n")
    f.write(f"energy_range = 4\n")
