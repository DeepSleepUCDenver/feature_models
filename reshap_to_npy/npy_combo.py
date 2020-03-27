import numpy as np
label = [np.load('all_labeled_data_y_' + str(i) + '.npy') for i in range(20)]
y = np.concatenate(label)
data = [np.load('all_labeled_data_X_' + str(i) + '.npy') for i in range(20)]
info = [np.load('all_labeled_data_X_' + str(i) + '.npy').shape for i in range(20)]
info = [i[0] for i in info]
c=0
ranges = []
for i, l in enumerate(info):
    ranges.append((i,c,l))
    c = l

o = np.concatenate([[j for k in range(i)] for j, i in enumerate(info)])
o = np.concatenate([[j for k in range(i)] for j, i in enumerate(info)])
x = np.concatenate(data)
np.save('all_labeled_data_X.npy', x)
np.save('all_labeled_data_y.npy', y)
np.save('all_labeled_data_observation_sets.npy', ranges)