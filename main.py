from PIL import Image,ImageFont,ImageDraw
import numpy as np
np.set_printoptions(threshold=np.inf)
def bw(threshold, path):
    '''

    :param path: file path
    :param threshold: color value, more big, more deep
    :return: PIL Image
    '''
    img = Image.open(path)
    Img = img.convert('L')
    Img = Img.point([0]*(threshold-1)+[1]*(257-threshold),'1')
    return Img


def textimage(text):

    im = Image.new("RGB", (len(text)*16, 16), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\DengXian\Deng.ttf", 14)
    dr.text((1.25, 1.25), text, font=font, fill="#000000")
    return im

def con(text, threshold=150, color=None):
    textimage(text).save("miao.png")
    im = np.array(bw(threshold, "miao.png"), dtype="int32").tolist()
    img = [[] for i in range(256)]
    white = Image.new("RGB", (16, 16), (255, 255, 255))
    white.save("white.png")
    white = np.array(bw(6, "white.png"),dtype="int32").tolist()
    for x in range(16):
        for y in im[x]:
            if y==0:
                for z in range(16):
                    img[x*16+z].extend(im[z])

            else:
                for z in range(16):
                    img[x*16+z].extend(white[z])
    n = np.array(img)
    if color==None:
        n[n == 1] = 255
        return Image.fromarray(n).convert("L")
    else:
        n = n.tolist()
        for x in range(256):
            for y in range(256):
                if n[x][y]==0:
                    n[x][y]=color
                else:
                    n[x][y]=[255,255,255]
        n = np.uint8(n)

        return Image.fromarray(n).convert("RGB")



con("抄",color=[255,0,0]).save("chu.png")
con("了").save("wan.png")
con("作").save("ning.png")
con("文").save("aa.png")