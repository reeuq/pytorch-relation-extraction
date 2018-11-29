import numpy as np

dataset_train_data = np.load('./dataset/FilterNYT/train/bags_feature.npy')
dataset_train_label = np.load('./dataset/FilterNYT/train/labels.npy')
dataset_test_data = np.load('./dataset/FilterNYT/test/bags_feature.npy')
dataset_test_label = np.load('./dataset/FilterNYT/test/labels.npy')
dataset_w2v = np.load('./dataset/FilterNYT/w2v.npy')

dataset_new_train_data = np.load('./dataset_new/FilterNYT/train/bags_feature.npy')
dataset_new_train_label = np.load('./dataset_new/FilterNYT/train/labels.npy')
dataset_new_test_data = np.load('./dataset_new/FilterNYT/test/bags_feature.npy')
dataset_new_test_label = np.load('./dataset_new/FilterNYT/test/labels.npy')
dataset_new_w2v = np.load('./dataset_new/FilterNYT/w2v.npy')

train_data = np.concatenate((dataset_train_data, dataset_new_train_data[:, 2].reshape(-1, 1)), axis=1)
test_data = np.concatenate((dataset_test_data, dataset_new_test_data[:, 2].reshape(-1, 1)), axis=1)

np.save('./dataset/FilterNYT/new_train/bags_feature.npy', train_data)
np.save('./dataset/FilterNYT/new_train/labels.npy', dataset_train_label)
np.save('./dataset/FilterNYT/new_test/bags_feature.npy', test_data)
np.save('./dataset/FilterNYT/new_test/labels.npy', dataset_test_label)
print('end')
