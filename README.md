# Functional parcellation for the default mode network (DMN): a large-scale meta-analysis
This repository contains code, data, and results for Wang, Taren & Smith (bioRxiv, 2017). 

The codes are based on previous work parcellating MFC and LFC (de la Vega et al., 2016; 2017): 
https://github.com/adelavega/neurosynth-mfc

https://github.com/adelavega/neurosynth-lfc

We thank Alexandro de la Vega for sharing his codes online and answer our technical questions!

link to the preprint: https://www.biorxiv.org/content/early/2017/11/27/225375

Figures for the manuscript (in .eps format) available at figures/

The main results can be produced following Clustering, Coactivation and Functional preference profiels.

### Requirements
Python 2.7.x

For analysis:
- Neurosynth tools (github.com/neurosynth/neurosynth)

    Note: PyPI is acting strange so install directly from github: `pip install git+https://github.com/neurosynth/neurosynth.git`
- Scipy/Numpy (Easiest way is using miniconda distribution)
- Scikit-learn
- joblib
- nibabel 1.x (this is very important for the codes to work!)

For visualization:
- Pandas
- nilearn
- seaborn

Unzip pre-generated Neurosynth dataset prior to analysis


