import utils
import os

root_dir = './../out'
folder_list = os.listdir(root_dir)
for i in range(len(folder_list)):
    path = os.path.join(root_dir, folder_list[i])
    if os.path.isfile(path):
        continue
    file_list = os.listdir(path)
    max_f1 = 0
    max_f1_file = ''
    max_f1_pre = 0
    max_f1_rec = 0
    for j in range(len(file_list)):
        if file_list[j].find("_DEF_") == -1:
            continue
        file_path = os.path.join(path, file_list[j])
        pre = []
        rec = []
        f = open(file_path)
        for line in f.readlines():
            temp = [float(num) for num in line.split()]
            pre.append(temp[0])
            rec.append(temp[1])
        f1_pre, f1_rec, f1 = utils.calculate_max_fi(pre, rec)
        if f1 > max_f1:
            max_f1 = f1
            max_f1_file = file_list[j]
            max_f1_pre = f1_pre
            max_f1_rec = f1_rec

    print("{}/{} max f1 {}, pre {}, rec {}".format(folder_list[i], max_f1_file, max_f1, max_f1_pre, max_f1_rec))


