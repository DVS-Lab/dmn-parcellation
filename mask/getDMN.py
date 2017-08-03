
from os import getcwd
from os.path import join
from neurosynth import Dataset
mypwd = getcwd()
dataset = Dataset.load(join(mypwd, 'data', 'dataset.pkl'))
dataset.add_features(join(mypwd, 'data','v4-topics-100.txt'), append=False)
ids = dataset.get_studies('59_network_default_dmn', frequency_threshold=0.05)
ma = meta.MetaAnalysis(dataset, ids)
ma.save_results(prefix='dmn')
