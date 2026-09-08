#!/bin/bash
#SBATCH --job-name=test_job       #Job name
#SBATCH --partition=UR_NODE       #Run "sinfo" command to see the list of available partition
#SBATCH --nodes=1                 #Run all processes on a single node
#SBATCH --ntasks=1                #Run a single task
#SBATCH --cpus-per-task=8         #Number of CPU cores per task
#SBATCH --gres=gpu                #Include gpu for the task (optional only for GPU jobs)
#SBATCH --mem=8gb                 #Total memory limit (optional)
#SBATCH --time=00:30:00           #Time limit hrs:min:sec (optional)
#SBATCH --output=dock_1hsg_%j.out #Standard output and error log
#SBATCH --error=dock_1hsg_%j.err  #If any error is caused



echo "Job Started at: $(date)"
echo "Running on node: $(hostname)"
echo "Working Dir: $(pwd)"


#setup to start with batch
module load python/3.11.9-gcc-12.3.0-b2e7upc
source ~/UR_PATH/docking_env/bin/activate


#setting up some variables for ease
#i can do this bcuz i have some prior experience with linux :)
MGLTOOLS=~/UR_PATH/mgltools_x86_64Linux2_1.5.7
MGLPY=$MGLTOOLS/bin/pythonsh
ADT_UTILS=$MGLTOOLS/MGLToolsPckgs/AutoDockTools/Utilities24
VINA=~/UR_PATH/autodock_vina_1_1_2_linux_x86/bin/vina

echo "Running Python Script"
python3 dock-prep-1hsg.py

echo "Converting PDB->PDBQT"
$MGLPY $ADT_UTILS/prepare_receptor4.py -r protein-receptor.pdb -o protein-receptor.pdbqt
$MGLPY $ADT_UTILS/prepare_ligand4.py -l ligand.pdb -o ligand.pdbqt

echo "DOCKING"
$VINA --config vina_config.txt --out docked_output.pdbqt --log docking_log.txt

echo "Job finished at: $(date)"