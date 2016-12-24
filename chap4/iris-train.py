# coding: utf-8
from sklearn import svm, metrics, cross_validation
import random, re
import pandas as pd

"""
# read CSV
csv = []
with open('chap4/iris.csv', 'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        csv.append(cols)

del csv[0]

random.shuffle(csv)

# 学習用とテスト用に分割
total_len = len(csv)
train_len = int(total_len * 2 / 3)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data = csv[i][0:4]
    label = csv[i][4]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
"""

csv = pd.read_csv('chap4/iris.csv')
csv_data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
csv_label = csv["Name"]

train_data, test_data, train_label, test_label = \
        cross_validation.train_test_split(csv_data, csv_label)

# 学習し、予測する
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)

# 正解率
ac_score = metrics.accuracy_score(test_label, pre)
print("正解率 = ", ac_score)
