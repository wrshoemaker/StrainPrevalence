[![DOI:10.1101/2021.10.05.463161](http://img.shields.io/badge/DOI-10.1101/2021.10.05.463161-B31B1B.svg)](https://doi.org/10.1101/2022.04.07.487434)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6793770.svg)](https://doi.org/10.5281/zenodo.6793770)

# StrainPrevalence

Repository for code associated with the preprint:

[A macroecological perspective on genetic diversity in the human gut microbiome](https://doi.org/10.1101/2022.04.07.487434).



### Setting up your environment

Set up the repo under a folder named Github: `~/GitHub/StrainPrevalence/`. Use the following file structure


```
StrainPrevalence
│   README.md   
│
└───data
│   
│   
└───scripts
│   
│   
└───analysis
```

All code was written in Python 2.7. You should be able to recreate the conda environment using the provided `environment.yml` file.

```bash
conda env create -f environment.yml
```

Sometimes conda does not cooperate. If that is the case, you just need to run the following commands:

```bash
conda create -n microbiome_evolution python=2.7.18
conda install matplotlib
conda install scipy
conda install numpy
```



### Getting the data

If you just want to regenerate my figures from the data, all you need is the data in the Zenodo repo (DOI: [10.5281/zenodo.6793770](https://doi.org/10.5281/zenodo.6793770)). Place the the data in your file directory as `~/GitHub/macroeco_phylo/data`. 




### Running the analyses


Running the commands to rerun the analyses from processed data is straightforward and are written to be run on a local machine. These commands are contained in 'run_analysis.sh`. To redo all analyses, run the following two commands


```bash
source activate microbiome_evolution
sh run_analysis.sh
```


If you would like to reprocess the raw data, meaning that you want to reprocess a FASTQ samples from the Human Microbiome Project (HMP), you will need to first obtain this publicly available data. I recommend using this repoisotory: <https://aws.amazon.com/datasets/human-microbiome-project/>. If you cannot access the data through this link, you can obtain it from the HMP Data Portal <https://portal.hmpdacc.org/>. Move the FASTQ files to the following directory: `~/GitHub/StrainPrevalence/data/SRA_files/`

Reprocessing the raw data is not a trivial task. It will require considerable computational time and power so I recommend you run all of these analyses on a cluster. The commands to reprocess the data starting from the FASTQ step are in `run_everything.sh`. This script contains commands for all data processing and analyses, including MIDAS, the program used to handle FASTQ metagenomic data. MIDAS v1.2.2 can be downloaded and installed from its [GitHub repo](https://github.com/snayfach/MIDAS).  You will need to change the paths in the scripts listed in `run_everything.sh` to get it working on your cluster. Place the MIDAS code in the following filepath: `~/GitHub/StrainPrevalence/data/midas_db_v1.2/`.



