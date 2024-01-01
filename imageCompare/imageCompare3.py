from PIL import Image
from PIL import ImageChops
import cv2
import numpy as np
import os
def compare_images(imageOne, imageTwo, diffSavePath,anotationSavePath):
    path = "./originImages"
    path2 = "./static/img"
    path = os.path.abspath(path)
    path2 = os.path.abspath(path2)
    print(path,path2)
    images = os.listdir(path)
    a = 1
    for image in images:
        image_abs = os.path.join(path,image)
        # new_image = os.path.join(path,"image%s.jpg"%str(a))
        # order = "mv {} {}".format(image_abs,new_image)
        order2 = "cp {} {}".format(image_abs,os.path.join(path2,image))
        os.system(order2)
        ## remove from old path
        # if os.path.exists(os.path.join(path2,"image%s.jpg"%str(a))):
        #     print('image%s.jpg  exist, so remove firstly'%str(a))
        #     os.system("rm {}".format(os.path.join(path2,"image%s.jpg"%str(a))))
        # os.system(order2)
        a+=1
    ## remove the old result
    if os.path.exists(os.path.join(path2, "diff.jpg")):
        print('diff file exist, so remove firstly')
        os.system("rm {}".format(os.path.join(path2, "diff.jpg")))
    if os.path.exists(os.path.join(path2, "result.jpg")):
        print('result file exist, so remove firstly')
        os.system("rm {}".format(os.path.join(path2, "result.jpg")))
    image_one = Image.open(imageOne)
    image_two = Image.open(imageTwo)
    try:
        diff = ImageChops.difference(image_one, image_two)
        if diff.getbbox() is None:
            # 图片间没有任何不同则直接退出
            print("We are the same!")
            image_one = cv2.imread(imageOne)
            cv2.imwrite(anotationSavePath, image_one)
        else:
            # print(diff.getbbox())  ## diff这张图像的大小
            ## 转为灰色,再转为白色, 再转为HSV, 再圈出灰色区域
            diff.save(diffSavePath)
            diff = cv2.imread(diffSavePath)
            image_one = cv2.imread(imageOne)
            diff = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
            diff = cv2.cvtColor(diff, cv2.COLOR_GRAY2RGB)
            diff = cv2.cvtColor(diff, cv2.COLOR_BGR2HSV)
            lowerColor = np.array([0, 0, 40])
            upperColor = np.array([180, 43, 220])
            diff = cv2.inRange(diff, lowerColor, upperColor)
            diff = cv2.medianBlur(diff, 9)
            contours, hieracy = cv2.findContours(diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
            res = cv2.drawContours(image_one, contours, -1, (0, 0, 255), 4)
            cv2.imwrite(diffSavePath, diff)
            if os.path.exists(anotationSavePath):
                os.system("rm {}".format(anotationSavePath))
            cv2.imwrite(anotationSavePath, res)
    except ValueError as e:
        print("【{0}】{1}".format(e))

if __name__ == '__main__':
    compare_images('./originImages/image1.jpg','./originImages/image2.jpg',
    './static/img/diff.jpg','./static/img/result.jpg')

