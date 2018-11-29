# -*- coding: utf-8 -*-

from torch.utils.data import Dataset
import os
import numpy as np
from six.moves import cPickle as pickle
import codecs


class FilterNYTData(Dataset):

    def __init__(self, root_path, train=True):
        if train:
            path = os.path.join(root_path, 'train/')
            print('loading train data')
        else:
            path = os.path.join(root_path, 'test/')
            print('loading test data')

        self.labels = np.load(path + 'labels.npy')
        self.x = np.load(path + 'bags_feature.npy')
        self.x = list(zip(self.x, self.labels))

        print('loading finish')

    def __getitem__(self, idx):
        assert idx < len(self.x)
        return self.x[idx]

    def __len__(self):
        return len(self.x)


class FilterNYTLoad(object):
    '''
    load and preprocess data
    max_len: the sentence's max length
    limit: the max length of position's one side(entity' left side or right side)
    '''
    def __init__(self, root_path, max_len=25, limit=50, pos_dim=5, pad=1):

        self.max_len = max_len
        self.limit = limit
        self.root_path = root_path
        self.pos_dim = pos_dim
        self.pad = pad

        self.w2v_path = os.path.join(root_path, 'vector.txt')
        self.word_path = os.path.join(root_path, 'dict_new.txt')
        self.train_path = os.path.join(root_path, 'train', 'train_sdp.pickle')
        self.test_path = os.path.join(root_path, 'test', 'test_sdp.pickle')
        self.entity_dict_path = os.path.join(root_path, 'dict.txt')

        print('loading start....')
        self.w2v, self.word2id, self.id2word, self.entity_word2id = self.load_w2v()

        np.save(os.path.join(self.root_path, 'w2v.npy'), self.w2v)

        print("parsing train text...")
        self.bags_feature, self.labels = self.parse_sen(self.train_path)
        np.save(os.path.join(self.root_path, 'train', 'bags_feature.npy'), self.bags_feature)
        np.save(os.path.join(self.root_path, 'train', 'labels.npy'), self.labels)

        print("parsing test text...")
        self.bags_feature, self.labels = self.parse_sen(self.test_path)
        np.save(os.path.join(self.root_path, 'test', 'bags_feature.npy'), self.bags_feature)
        np.save(os.path.join(self.root_path, 'test', 'labels.npy'), self.labels)
        print('save finish!')

    def load_w2v(self):
        '''
        reading from vec.bin
        add two extra tokens:
            : UNK for unkown tokens
            : BLANK for the max len sentence
        '''
        wordlist = []
        vecs = []

        wordlist.append('BLANK')
        wordlist.extend([word.strip('\n') for word in codecs.open(self.word_path, encoding="utf-8")])

        for line in open(self.w2v_path):
            line = line.strip('\n').split()
            vec = list(map(float, line))
            vecs.append(vec)

        dim = len(vecs[0])
        vecs.insert(0, np.zeros(dim))
        for i in range(78):
            vecs.append(np.random.uniform(low=-1.0, high=1.0, size=dim))

        word2id = {j: i for i, j in enumerate(wordlist)}
        id2word = {i: j for i, j in enumerate(wordlist)}

        entity_wordlist = ['BLANK']
        entity_wordlist.extend([word.strip('\n') for word in codecs.open(self.entity_dict_path, encoding="utf-8")])
        entity_word2id = {j: i for i, j in enumerate(entity_wordlist)}

        return np.array(vecs, dtype=np.float32), word2id, id2word, entity_word2id

    def parse_sen(self, path):
        '''
        parse the records in data
        '''
        all_sens = []
        all_labels = []

        f = open(path, 'rb')
        f_data = pickle.load(f)
        all_sens = f_data["data"]
        f.close()

        max_length = 0
        for item in all_sens:
            item[2], temp_max_length = self.get_sentence_id(item[2])
            item[0] = self.get_entity_id(item[0])
            if temp_max_length > max_length:
                max_length = temp_max_length
            all_labels.append(item.pop(-1))

        bags_feature = self.get_sentence_feature(all_sens)

        return bags_feature, all_labels

    def get_sentence_id(self, sen):
        sen_ids = []
        max_len = 0
        for each_sen in sen:
            sen_id = []
            for each_word in each_sen:
                sen_id.append(self.word2id[each_word])
            sen_ids.append(sen_id)
            if len(each_sen) > max_len:
                max_len = len(each_sen)
        return sen_ids, max_len

    def get_entity_id(self, entity):
        entity_ids = []
        for each_entity in entity:
            entity_ids.append(self.entity_word2id[each_entity])
        assert len(entity_ids) == 2
        return entity_ids

    def get_sentence_feature(self, bags):
        '''
        : word embedding
        : postion embedding
        return:
        sen list
        '''
        update_bags = []

        for bag in bags:
            es, num, sens = bag
            new_sen = []
            for idx, sen in enumerate(sens):
                new_sen.append(self.get_pad_sen(sen))
            update_bags.append([es, num, new_sen])

        return update_bags

    def get_pad_sen(self, sen):
        '''
        padding the sentences
        '''
        sen.insert(0, self.word2id['BLANK'])
        if len(sen) < self.max_len + 2 * self.pad:
            sen += [self.word2id['BLANK']] * (self.max_len + 2 * self.pad - len(sen))
        else:
            sen = sen[: self.max_len + 2 * self.pad]

        return sen


if __name__ == "__main__":
    data = FilterNYTLoad('./FilterNYT/')
