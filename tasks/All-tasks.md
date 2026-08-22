## Tasks

- [x] **Protein sequence similarity and clustering** - [x]

- Download 20-30 protein sequences belonging to 3-4 different protein families from
UniProt.
- Calculate pairwise sequence identity or similarity.
- Construct a similarity matrix and visualize it as a heatmap.
- Use hierarchical clustering to group the proteins.
- Compare whether the computational clusters correspond to the known protein
families.

- [ ] **Protein contact-map generation**

- Download 5-10 protein structures from the PDB.
- Calculate all pairwise Ca distances.
- Define two residues as being in contact when their Ca atoms are within a chosen
cutoff, for example 8 Å.
- Construct and plot the residue-residue contact map for each protein.
- Compare contact maps of predominantly a-helical and predominantly B-sheet
proteins.

- [ ] **Ligand similarity using molecular fingerprints**

- Download 50-100 ligands associated with one or more protein targets from
ChEMBL or GPCRdb.
- Convert SMILES strings to RDKit molecules.
- Generate Morgan fingerprints.
- Calculate pairwise Tanimoto similarities.
- Visualize the similarity matrix as a heatmap.
- Cluster the molecules and display representative molecules from different clusters

- [ ] **Principal-component analysis of protein conformations**

- Download several structures of the same protein, for example structures representing different functional states.
- Align the structures using their Ca atoms.
- Construct a coordinate matrix from the aligned structures.
- Perform PCA on the coordinates.
- Plot the structures in PC1-PC2 space.
- Color the points according to experimentally annotated conformational state.
