#!/bin/bash

# activate your conda environment
#source activate microbiome_evolution

# run MIDAS
#sh ./qsub_midas/qsub_script_HMP_MIDAS_species_snps_cnvs.sh

# merge MIDAS species
#sh ./qsub_midas/qsub_script_HMP_MIDAS_species_merge.sh

# merge MIDAS genes
#sh ./qsub_midas/qsub_script_HMP_MIDAS_CNVs_merge.sh

# merge MIDAS SNPs
#sh ./qsub_midas/qsub_script_HMP_MIDAS_SNPs_merge.sh

# postproces midas data
#python postprocess_all_midas_data_serial.py

# split all BAM files into separate species
#sh ./qsub_HMP_MAPGD/split_all_bam_files.sh

# run MAPGD on each host for each species
#sh ./qsub_HMP_MAPGD/run_mapgd_all_species.sh

# make dictionary of alleles for all species
#sh ./qsub_prevalence/run_make_alleles_dict_all_species.sh

# predict prevalence for all species
#sh ./qsub_prevalence/run_prevalence_prediction_all_species.sh

# run StrainFinder
#sh ./qsub_strains/qsub_strainfinder.sh




