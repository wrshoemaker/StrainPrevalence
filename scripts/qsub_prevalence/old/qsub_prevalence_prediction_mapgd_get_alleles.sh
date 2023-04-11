#!/bin/bash
#$ -N predict_prevalence_mapgd
#$ -e /u/project/ngarud/wrshoema/snv_prevalence/scripts/mapgd_error
#$ -o /u/project/ngarud/wrshoema/snv_prevalence/scripts/mapgd_output
#$ -l h_data=24G
#$ -l time=24:00:00
#$ -l highp
#$ -m bea


. /u/local/Modules/default/init/modules.sh

module unload python
module load python/2.7.15


#python /u/project/ngarud/wrshoema/snv_prevalence/scripts/calculate_predicted_prevalence_mapgd.py --make_alleles_dict

python /u/project/ngarud/wrshoema/snv_prevalence/scripts/calculate_predicted_prevalence_mapgd.py --species all

# qrsh -l h_rt=3:00:00,h_data=24G
