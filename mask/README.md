# Mask Generation
Here are the steps for generating the DMN mask
1) neurosynth: use reverse inference map from 100-topic set (see getDMN.py)
2) constrain map to anatomy defined by the Harvard-Oxford Atlas (AngularGyrus, FPole, PCC, ACC, iLOC, sLOC, pSupraMarg, ParaCing, VMPFC)
3) remove clusters that are k < 50
