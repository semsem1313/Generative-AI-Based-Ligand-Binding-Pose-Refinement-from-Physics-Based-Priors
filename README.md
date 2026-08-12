# Generative AI-Based Ligand Binding Pose Refinement from Physics-Based Priors
 
**Author:** Samarth M. Pawar

**Guide:** Prof. Saumajit Dutta

**Status:** 🟡 In Progress — Week 1 (Learning Phase)
 
## Project Overview
 
This project explores using generative AI methods (flow matching / diffusion
models, geometric deep learning) to refine ligand binding poses, guided by
physics-based priors from classical molecular docking approaches. The goal is
to combine the accuracy of physics-based scoring functions with the
flexibility and speed of modern generative models.
 
## Current Goal (Week 1)
 
Before diving into modeling, the focus this week is on building foundational
understanding of:
 
- Proteins, amino acids, and protein structure
- Substrates and protein–ligand interactions
- Molecular docking (physics-based methods, e.g. AutoDock Vina and its
  derivatives)
Progress and notes from this phase are being written up in
[`reports/report_1.docx`](reports/report_1.docx), updated as topics are
covered.
 
## Roadmap
 
- [o] Report 1: Proteins, substrates, and molecular docking basics
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
├── .env        # template for environment 
├── requirements.txt      # Python dependencies
├── docs/
│   └── background.md     # resources
└── reports/
    └── report_1.docx     # weekly progress reports
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
[`docs/background.md`](docs/background.md), including:
 
- Protein structure databases (RCSB PDB)
- Small molecule databases (PubChem, ChEMBL)
- Python libraries: MDTraj, MDAnalysis, RDKit, Open Babel
- Docking literature (AutoDock Vina, QuickVina, Uni-Dock, etc.)
- Visualization tools: VMD, Chimera
## Notes
 
This README will be updated as the project progresses through each phase.