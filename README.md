Pythonによるスクレイピング & 機械学習
===============

 - [https://www.amazon.co.jp/dp/4802610793](https://www.amazon.co.jp/dp/4802610793)
 - [サンプルプログラム (src.zip)](http://www.socym.co.jp/download/1079/src.zip)

setup (macOS)
-------------

```bash
# rbenvのPython版を入れる
$ brew install pyenv pyenv-virtualenv
# pyenvの設定を追加してshellをリロード
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ source ~/.bash_profile

# Python 3.6 をインストール & 仮想環境作成 & local デフォルトに設定
$ pyenv install 3.6.0
$ pyenv virtualenv 3.6.0 3.6.0-ml
$ pyenv local 3.6.0-ml
$ pip install --upgrade pip

# 必要そうなあれこれを入れる
$ pip install --upgrade numpy scipy scikit-learn matplotlib pandas jupyter ipython seaborn
```
