# Generative AI-Based Ligand Binding Pose Refinement from Physics-Based Priors
 
**Author:** Samarth M. Pawar

**Guide:** [Prof. Saumajit Dutta](https://github.com/soumajit2706) 

**Status:** 🟡 In Progress — Week 2 (Learning Phase)
 
## Project Overview
 
This project explores using generative AI methods (flow matching / diffusion
models, geometric deep learning) to refine ligand binding poses, guided by
physics-based priors from classical molecular docking approaches. The goal is
to combine the accuracy of physics-based scoring functions with the
flexibility and speed of modern generative models.
 
## Current Goal (Week 2)
In this week my job is to make a literature review on the various scoring functions and figure out which one is the best for this project, Also I have been assigned with some tasks by my Prof. which I'm currently working on.

 
## Roadmap
 
- [x] Proteins, Ligand-Protein Interactions, and Molecular docking basics
- [ ] Learn flow matching and diffusion models
- [ ] Learn geometric deep learning fundamentals
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
├── pdb_files
├── tasks
├── docs/
│   └── project_background.md   # resources
└── reports/                 # weekly progress reports
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