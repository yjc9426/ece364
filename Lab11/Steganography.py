import sys,numpy,base64,re
from os.path import join
from numpy import ndarray
from scipy.misc import *
from PIL import Image
from zlib import compress,decompress


class Payload:
    def __init__(self, img=None, compressionLevel=-1, xml=None):
        if img is None and xml is None:
            raise ValueError("no input")
        if compressionLevel>9 or compressionLevel<-1:
            raise ValueError("wrong compression level")
        if img is not None and type(img) != ndarray or xml is not None and type(xml) != str:
            raise TypeError("bad image")

        if img is not None:
            self.img=img
            self.cmplvl = compressionLevel
            self.xml = self.picToXml()
        if xml is not None:
            self.xml = xml
            self.img=self.xmlToPic()
            self.cmplvl = compressionLevel

    def picToXml(self):
        xml='<?xml version="1.0" encoding="UTF-8"?>\n'
        s=self.img.shape
        scale=self.getScale()
        if self.cmplvl != -1:
            bol="True"
        else:
            bol="False"
        xml+='<payload type="'+scale+'" size="'+str(s[0])+','+str(s[1])+'" compressed="'+bol+'">\n'
        xml+=self.codePic()
        xml+='\n</payload>'
        return xml

    def codePic(self):
        if self.getScale() == "Gray":
            gray=ndarray.flatten(self.img)
            if self.cmplvl != -1:
                gray=compress(ndarray.flatten(self.img),self.cmplvl)
            imgCode = base64.b64encode(gray)
        elif self.getScale() == "Color":
            color = []
            for i in self.img:
                for j in i:
                    color.append(j[0])
            for i in self.img:
                for j in i:
                    color.append(j[1])
            for i in self.img:
                for j in i:
                    color.append(j[2])
            color = numpy.array(color)
            if self.cmplvl != -1:
                color = compress(color,self.cmplvl)
            imgCode = base64.b64encode(color)
        return str(imgCode)[2:-1]

    def getScale(self):
        if(len(self.img.shape)<3):
            return "Gray"
        elif len(self.img.shape)==3:
            return "Color"
        else:
            raise ValueError('sb')

    def xmlToPic(self):
        temp = self.xml.splitlines()
        m = re.search(r'<payload type="(?P<payloadType>.*)" size="(?P<size>.*)" compressed="(?P<bol>.*)">', temp[1])
        pType=m.group("payloadType")
        psize=m.group("size")
        psize = psize.split(',')
        bol=m.group("bol")
        spl = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
        if pType == 'Gray':
            pic = base64.b64decode(temp[2])
            if bol == 'True':
                pic = list(decompress(pic))
            else:
                pic = list(pic)

            l=numpy.resize(pic,(int(psize[0]),int(psize[1])))

        elif pType == 'Color':
            pic = base64.b64decode(temp[2])
            if bol == "True":
                pic = list(decompress(pic))
            else:
                pic = list(pic)
            lst = spl(pic,int(len(pic)/3))
            l=[]
            for i in range(int(len(pic)/3)):
                l.append([lst[0][i],lst[1][i],lst[2][i]])
            l=numpy.array(l)
            l=numpy.resize(l,(int(psize[0]),int(psize[1]),3))
        return l


class Carrier:
    def __init__(self, img):
        if type(img) != ndarray:
            raise TypeError("bad image")
        self.img=img

    def payloadExists(self):
        if self.getScale() == "Gray":
            new_img = self.img & 1
            num = numpy.packbits(ndarray.flatten(new_img))
        else:
            color = []
            for i in self.img:
                for j in i:
                    color.append(j[0])
            for i in self.img:
                for j in i:
                    color.append(j[1])
            for i in self.img:
                for j in i:
                    color.append(j[2])
            color = numpy.array(color) & 1
            num = numpy.packbits(numpy.array(color))
        xml=''
        for i in num:
            xml += chr(i)
        if re.search(r'<?xml version',xml):
            return True
        else:
            return False

    def clean(self):
        new_img = self.img & 254
        return new_img


    def getScale(self):
        if(len(self.img.shape)<3):
            return "Gray"
        elif len(self.img.shape)==3:
            return "Color"
        else:
            raise ValueError('sb')

    def embedPayload(self, payload, override=False):
        if type(payload) != Payload:
            raise TypeError
        if payload.img.size > self.img.size:
            raise ValueError
        if self.payloadExists() and override == False:
            raise Exception
        xml = ndarray.flatten(numpy.unpackbits(numpy.fromstring(payload.xml,dtype='uint8')))
        img = self.img

        if self.getScale() == "Color":
            crimg=[]
            for i in img:
                for j in i:
                    crimg.append(j[0])
            for i in img:
                for j in i:
                    crimg.append(j[1])
            for i in img:
                for j in i:
                    crimg.append(j[2])
            crimg = ndarray.flatten(numpy.array(crimg))
            crimg[0:xml.size] &= 254
            crimg[0:xml.size] += xml
            spl = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
            lst = spl(crimg,int(len(crimg)/3))
            l=[]
            for i in range(int(len(crimg)/3)):
                l.append([lst[0][i],lst[1][i],lst[2][i]])
            img=numpy.array(l)
            psize = self.img.shape
            img=numpy.resize(img,(int(psize[0]),int(psize[1]),3))
        else:
            img = ndarray.flatten(img)
            img[0:xml.size] &= 254
            img[0:xml.size] += xml
            psize = self.img.shape
            img=numpy.resize(img,psize)
        return img


    def extractPayload(self):
        if self.payloadExists() is False:
            raise Exception
        if self.getScale() == "Gray":
            new_img = self.img & 1
            num = numpy.packbits(ndarray.flatten(new_img))
        else:
            color = []
            for i in self.img:
                for j in i:
                    color.append(j[0])
            for i in self.img:
                for j in i:
                    color.append(j[1])
            for i in self.img:
                for j in i:
                    color.append(j[2])
            color = numpy.array(color) & 1
            num = numpy.packbits(numpy.array(color))
        xml=''
        for i in num:
            xml += chr(i)
        return Payload(xml=xml)



if __name__ == "__main__":
    img = imread(join("test_images", "payload1.png"))
    f = Image.open(join("test_images", "payload1.png"), 'r')
    pixels = list(f.getdata())
    print(img.shape)
    if(len(img.shape)<3):
        print('gray')
    elif len(img.shape)==3:
        print('Color(RGB)')
    else:
        print('others')
    print(img)
    f = open(join("test_images", "payload1_0.xml"),'r')
    ex=f.read()
    print(type(ex))

    plaintext = ''


    a=bytes()
    imgCode = base64.b64encode(bytes())
    print(imgCode)
    print (str())
    a = [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1]
    b= numpy.packbits(a)
    for n in b:
        print(chr(n))
    print(numpy.unpackbits(b))
    img = imread(join("test_images", "result1.png"))
    img2= imread(join("test_images", "result5.png"))

    print(109 & 254)
    print(ord('s'))

    p = imread(join("test_images", "payload4.png"))
    c = imread(join("test_images", "carrier2.png"))
    expectedValue = imread(join("test_images", "result1.png"))
    print(expectedValue)
