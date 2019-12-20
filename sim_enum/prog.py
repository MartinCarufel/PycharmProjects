from dei_feature import *

version = '14'

if version == '15':
    dei_feat_output = dei_feat_output_15
if version == '14':
    dei_feat_output = dei_feat_output_14


print('aux: {}'.format(dei_feat_output.aux2))
