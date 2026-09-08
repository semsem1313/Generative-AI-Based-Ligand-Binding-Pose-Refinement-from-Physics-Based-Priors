# Generative AI-Based Ligand Binding Pose Refinement from Physics-Based Priors
 
**Author:** Samarth M. Pawar

**Guide:** [Prof. Saumajit Dutta](https://github.com/soumajit2706) 

**Status:** 🟡 In Progress — Week 3 (Hands On Phase)
 
## Project Overview
 
This project explores using generative AI methods (flow matching / diffusion
models, geometric deep learning) to refine ligand binding poses, guided by
physics-based priors from classical molecular docking approaches. The goal is
to combine the accuracy of physics-based scoring functions with the
flexibility and speed of modern generative models.
 
## Current Goal (Week 3)
This week, my job was to perform redocking on the complex 1HSG, which is the HIV protein-ligand complex. This redocking was done to And how the RMSD values produced and the later-on structure produced through docking aligns exactly similar to the crystalline structure of the complex or not?

 
## Roadmap
 
- [x] Proteins, Ligand-Protein Interactions, and Molecular docking basics
- [x] Write a literature review on scoring functions and finish assigned tasks
- [ ] Perform Re-Docking on 1HSG complex
- [ ] Survey existing generative AI docking approaches
- [ ] Define physics-based priors to incorporate into the model
- [ ] Prototype pose refinement pipeline
- [ ] Evaluate against benchmark datasets
## Repository Structure
 
```
.
├── README.md
├── .gitignore
├── .env          # template for environment 
├── requirements.txt     # Python dependencies
├── pdb_files       #contains the pdb_files used in task2
├── tasks          #all tasks
├── dock-files      #all docking fies & py scripts
├── docs/
│   └── project_background.md   # resources
└── reports                 # weekly progress reports
```
 
## Setup
 
```bash
python -m venv venv
source venv/bin/activate     # on Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env         # then fill in any required values
```
 
## Resources
 
Key references and reading material used for this project are tracked in
[`docs/project_background.md`](docs/project_background.md), including:
 
- Protein structure databases (RCSB PDB)
- Small molecule databases (PubChem, ChEMBL)
- Python libraries: MDTraj, MDAnalysis, RDKit, Open Babel
- Docking literature (AutoDock Vina, QuickVina, Uni-Dock, etc.)
- Visualization tools: VMD, Chimera
## Notes
 
This README will be updated as the project progresses through each phase.