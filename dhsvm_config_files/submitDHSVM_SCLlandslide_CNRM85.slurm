#!/bin/bash
## job name 
#SBATCH --job-name=DHSVMskagit_run20190227

#SBATCH --mail-user=cband@uw.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL


#SBATCH --account=coastal
#SBATCH --partition=coastal
## Resources 
## Nodes 
#SBATCH --nodes=1       
## Tasks per node (Slurm assumes you want to run 28 tasks per node unless explicitly told otherwise)
#SBATCH --ntasks-per-node=26 
## Walltime (hh:mm:ss) 
#SBATCH --time=300:00:00 
## Memory per node 
#SBATCH --mem=100G 
## Specify the working directory for this job 
#SBATCH --workdir=/gscratch/coastal/cband/skagit/Skagit/

## Modules needed to run
/gscratch/coastal/cband/skagit/Skagit/DHSVM3.1.3 /gscratch/coastal/cband/skagit/Skagit/INPUT.skagitSCLlandslide.bclivlow.G.CNRM-CM5__rcp85 > log_INPUT_SCLCNRM85
