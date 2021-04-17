from PIL import Image,ImageFont,ImageDraw
import numpy as np
np.set_printoptions(threshold=np.inf)
def bw(threshold, file):
    '''

    :param file: file path or PIL.Image.Image object
    :param threshold: color value, more big, more deep
    :return: PIL Image
    '''
    if type(file)!=str:
        img = file
    else:
        img = Image.open(file)
    Img = img.convert('L')
    Img = Img.point([0]*(threshold-1)+[1]*(257-threshold),'1')
    return Img


def textimage(text, size=16):

    im = Image.new("RGB", (len(text)*size, size), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype("C:\\Windows\\Fonts\\DengXian\Deng.ttf", size)
    dr.text((0,0), text, font=font, fill="#000000")
    return im

def con(text, threshold=150, color=None, size=16):
    im = np.array(bw(threshold, textimage(text, size=size)), dtype="int32").tolist()
    img = [[] for i in range(size*size)]
    white = np.array(bw(6, Image.new("RGB", (size, size), (255, 255, 255))),dtype="int32").tolist()
    for x in range(size):
        for y in im[x]:
            if y==0:
                for z in range(size):
                    img[x*size+z].extend(im[z])

            else:
                for z in range(size):
                    img[x*size+z].extend(white[z])
    n = np.array(img)
    if color==None:
        n[n == 1] = 255
        return Image.fromarray(n).convert("L")
    else:
        n = n.tolist()
        for x in range(size*size):
            for y in range(size*size):
                if n[x][y]==0:
                    n[x][y]=color
                else:
                    n[x][y]=[255,255,255]
        n = np.uint8(n)

        return Image.fromarray(n).convert("RGB")

def conimg(file, threshold=150,):
    origin = Image.open(file).convert("RGB")
    size = origin.size[0]
    im = np.array(bw(threshold, origin).convert("RGB"), dtype="int32").tolist()
    img = [[] for i in range(size*size)]
    origin = np.array(origin).tolist()
    white = np.array(
            Image.new("RGB", (size, size), (255, 255, 255)).convert("RGB")
        ,dtype="int32"
    ).tolist()
    for x in range(size):
        for y in range(size):
            if im[x][y]==[0,0,0]:
                for z in range(size):
                    img[x*size+z].extend(origin[z])

            else:
                for z in range(size):
                    img[x*size+z].extend(white[z])
    n = np.uint8(img)
    return Image.fromarray(n).convert("RGB")

conimg("compass.png").save("conpass2.png")