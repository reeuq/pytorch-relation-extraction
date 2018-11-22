from six.moves import cPickle as pickle
import codecs

word_set = set()
word_path = "./../dict_new.txt"
word_set.update([word.strip('\n') for word in codecs.open(word_path, encoding="utf-8")])


new_word_set = set()
f = open("./../train/train_sdp.pickle", 'rb')
f_data = pickle.load(f)
train_data = f_data["data"]
f.close()

f = open("./../test/test_sdp.pickle", 'rb')
f_data = pickle.load(f)
test_data = f_data["data"]
f.close()

for data in train_data:
    for item in data[2]:
        new_word_set.update(item)

for data in test_data:
    for item in data[2]:
        new_word_set.update(item)

rest = new_word_set - word_set

for item in rest:
    print(item)
