[![DOI](https://zenodo.org/badge/99120146.svg)](https://zenodo.org/badge/latestdoi/99120146)

# Functional parcellation for the default mode network (DMN): a large-scale meta-analysis
This repository contains code, data, and results for Wang, Taren, Tepfer, & Smith (bioRxiv, 2019). 
Preprint of the manuscript: https://www.biorxiv.org/content/10.1101/225375v3

The code is based on previous work parcellating MFC and LFC (de la Vega et al., 2016; 2017): 

https://github.com/adelavega/neurosynth-mfc

https://github.com/adelavega/neurosynth-lfc

We thank Alejandro de la Vega for sharing his code online and answering our technical questions!

Figures for the manuscript (in .eps format) available at figures/

The main results can be produced following Clustering, Coactivation and Functional preference profiles.

### Requirements
Python 2.7.x

For analysis:
- Neurosynth tools (github.com/neurosynth/neurosynth)

    Note: PyPI is acting strange so install directly from github: `pip install git+https://github.com/neurosynth/neurosynth.git`
- Scipy/Numpy (Easiest way is using miniconda distribution)
- Scikit-learn
- joblib
- nibabel 1.x (this is very important for the code to work!)

For visualization:
- Pandas
- nilearn
- seaborn

Unzip pre-generated Neurosynth dataset prior to analysis


