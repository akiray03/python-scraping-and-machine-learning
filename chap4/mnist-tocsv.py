# coding: utf-8

import struct

def to_csv(name, maxdata):
    lbl_f = open('./mnist/{}-labels-idx1-ubyte'.format(name), 'rb')
    img_f = open('./mnist/{}-images-idx3-ubyte'.format(name), 'rb')
    csv_f = open('./mnist/{}.csv'.format(name), 'w', encoding='utf-8')
    # read header
    mag, lbl_count = struct.unpack('>II', lbl_f.read(8))
    mag, img_count = struct.unpack('>II', img_f.read(8))
    rows, cols = struct.unpack('>II', img_f.read(8))
    pixels = rows * cols
    # 画像データを読んでCSVで保存
    res = []
    for idx in range(lbl_count):
        if idx > maxdata:
            break
        label = struct.unpack('B', lbl_f.read(1))[0]
        bdata = img_f.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))
        csv_f.write(str(label) + ",")
        csv_f.write(",".join(sdata) + "\n")
        # PGM test
        if idx < 10:
            s = "P2 28 28 255\n"
            s += " ".join(sdata)
            iname = "./mnist/{}-{}-{}.pgm".format(name, idx, label)
            with open(iname, 'w', encoding='utf-8') as f:
                f.write(s)
    csv_f.close()
    lbl_f.close()
    img_f.close()

to_csv('train', 100000)
to_csv('t10k', 500)
