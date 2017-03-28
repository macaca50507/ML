import os
from pprint import pprint
from random import shuffle

n_people = 38
n_img_person = 64
n_train_person = 35
H, W = 192, 168

X_train = []
y_train = []
X_test = []
y_test = []

def is_legal_filename(fn):
    return len(fn) >= 24 and not fn.endswith('.bad')

train = open("train.txt","w")
test = open("test.txt","w")

for i in range(n_people):
    people_id = i + 1 if(i < 13) else i + 2
    dirname = 'CroppedYale/yaleB{:02}/'.format(people_id)
    filenames = [x for x in os.listdir(dirname) if is_legal_filename(x)]
    shuffle(filenames)
    idx = 0
    pp = str(i);
    for a in filenames:
        if idx < 35:
            train.write(dirname + a + ' ' + pp + '\n')
        else:
            test.write(dirname + a + ' ' + pp + '\n')
        idx += 1

train.close()
test.close()
