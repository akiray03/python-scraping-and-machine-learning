# coding: utf-8
from sklearn import svm
import pandas as pd

# XORの演算結果・学習器に与える入力データ
xor_input = [
  # P, Q, result
  [0, 0, 0],
  [0, 1, 1],
  [1, 0, 1],
  [1, 1, 0],
]

# 学習用にデータとラベルに分ける
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0:1] # data
xor_label = xor_df.ix[:, 2] # label

# 学習
clf = svm.SVC()
clf.fit(xor_data, xor_label)

# 予測
pre = clf.predict(xor_data)
print("予測結果:", pre)

# 正解と合っているか結果確認
ok = 0; total = 0
for idx, answer in enumerate(xor_label):
    p = pre[idx]
    if p == answer:  ok+= 1
    total += 1
print("正解率:  {} / {} = {}".format(ok, total, ok/total))
