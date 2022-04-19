import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import urllib.request
import pathlib

def scanning(img):
    h, w = img.shape#[:2]    # グレースケール画像のサイズ取得（カラーは3）
    x = int(w/64)           # 領域の横幅
    y = int(h/64)           # 領域の高さ
    x_step = x              # 領域の横方向へのずらし幅
    y_step = y              # 領域の縦方向へのずらし幅
    x0 = 0                  # 領域の初期値x成分
    y0 = 0                  # 領域の初期値y成分
    j = 0                   # 縦方向のループ指標を初期化

    # 縦方向の走査を行うループ
    while y + (j * y_step) < h:
        i = 0                   # 横方向の走査が終わる度にiを初期化
        ys = y0 + (j * y_step)  # 高さ方向の始点位置を更新
        yf = y + (j * y_step)   # 高さ方向の終点位置を更新
        print()

        # 横方向の走査をするループ
        while x + (i * x_step) < w:
            roi = img[ys:yf, x0 + (i * x_step):x + (i * x_step)]    # 元画像から領域をroiで抽出

            # ここからが領域に対する画像処理
            ave = np.mean(roi).astype("uint8")
            img[ys:yf, x0 + (i * x_step):x + (i * x_step)] = np.full(roi.shape, ave)
            pixelValue = img[10, 20]
            print ((str(pixelValue)), end = ",")
            # ここまでが領域に対する画像処理

            i = i + 1   # whileループの条件がFalse（横方向の端になる）まで、iを増分
        j = j + 1       # whileループの条件がFalse（縦方向の端になる）まで、jを増分
    return img

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url',
                        default='a.png')
    parser.add_argument('-s', '--save_file_name', default='a.png')
    arguments = parser.parse_args()

    if not pathlib.Path(arguments.save_file_name).exists():
        print('Downloading ...', end=' ')
        urllib.request.urlretrieve(arguments.url, filename=arguments.save_file_name)
        print('Done.')

    image = cv2.imread(arguments.save_file_name, cv2.IMREAD_UNCHANGED)
    kernel4 = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]], dtype=np.uint8)
    eroded_image4 = cv2.erode(image, kernel4, iterations=1)
    kernel8 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]], dtype=np.uint8)
    eroded_image8 = cv2.erode(image, kernel8, iterations=1)

    cv2.imshow('input image', image)
    cv2.imshow('eroded image4', eroded_image4)
    cv2.imshow('eroded image8', eroded_image8)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


path = 'logo.jpg'
img = cv2.imread(path, 0)     # 画像読み込み

img = scanning(img)
print()

# ここからグラフ設定
# フォントの種類とサイズを設定する。
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'Times New Roman'
fig = plt.figure()
ax1 = fig.add_subplot(111)

# 画像をプロット
ax1.imshow(img, cmap='gray')

# 軸のラベルを設定する。
ax1.set_xlabel('x [pix]')
ax1.set_ylabel('y [pix]')

fig.tight_layout()
plt.show()
plt.close()

"""if __name__ == '__main__':
    main()
"""