"""
主要处理内容：
1、将">>> relation >>>"转化为">>>relation>>>"(切分后，三个字符串变为一个)
"""

from six.moves import cPickle as pickle


def get_sentence_id(sen):
    sen_ids = []
    max_len = 0
    for each_sen in sen:
        sen_id = []
        words = each_sen.split(' ')
        assert (len(words)-1) % 4 == 0
        for i in range(0, len(words)-1, 4):
            sen_id.append(words[i])
            sen_id.append(words[i+1] + words[i+2] + words[i+3])
        sen_id.append(words[-1])
        sen_ids.append(sen_id)
        if len(sen_id) > max_len:
            max_len = len(sen_id)
    return sen_ids, max_len


def parse_sen(path, path_write):
    """
    parse the records in data
    """
    f = open(path, 'rb')
    f_data = pickle.load(f)
    data = f_data["data"]
    f.close()

    max_length = 0
    for item in data:
        item[2], temp_max_length = get_sentence_id(item[2])
        if temp_max_length > max_length:
            max_length = temp_max_length

    print("max length:", max_length)

    fw = open(path_write, 'wb')
    result = {
        'data': data,
    }
    pickle.dump(result, fw, protocol=2)
    fw.close()


if __name__ == '__main__':
    print("parse start")
    parse_sen("./../original_data/train/train_sdp.pickle", "./../train/train_sdp.pickle")
    print("parse train end")
    parse_sen("./../original_data/test/test_sdp.pickle", "./../test/test_sdp.pickle")
    print("parse test end")
