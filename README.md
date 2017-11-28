# neurosynth-mfc
This repository contains code, data, and results for Wang, Taren & Smith (bioRxiv, 2017). 

link to the preprint: https://www.biorxiv.org/content/early/2017/11/27/225375

Figures (.eps) for the manuscript available at figures/

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


