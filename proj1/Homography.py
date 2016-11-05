#! /bin/bash
#
# $Author$
# $Date$
# $Revision$
# $HeadURL$

import numpy as np
import sys
import scipy
from PIL import Image
import os


class Homography():
    def __init__(self, **kwargs):
        homo = kwargs.get('homographyMatrix')
        if 'homographyMatrix' not in kwargs:
            raise ValueError('wrong name')
        else:
            if len(kwargs['homographyMatrix']) != 3:
                raise ValueError('wrong length')
            else:
                homoM = kwargs['homographyMatrix']
                for l in homoM:
                    if type(homoM) != list:
                        raise ValueError('not list')
                    else:
                        for f in l:
                            if type(f) != float:
                                raise ValueError('not float')
                            else:
                                self.homoMatrix = np.array(homoM)
        print(self.homoMatrix)
    def forwardProject(self,point):
        plist = []
        plist.append(list(point)[0]*self.homoMatrix[0,0])
        plist.append(list(point)[1]*self.homoMatrix[1,1])
        return tuple(plist)

    def inverseProject(self,pointPrime):
        pPlist = []
        pPlist.append(list(pointPrime)[0]/self.homoMatrix[0,0])
        pPlist.append(list(pointPrime)[1]/self.homoMatrix[1,1])
        return tuple(pPlist)

class Transformation():
    def __init__(self, sourceImage, homography):


if __name__ == "__main__":
    #myim = Image.open('GrayFine.png')
    #myim.show()
    mat = [[1.2, 2.3, 4.5], [9.0, 4.4, 5.5], [0.0, 0.0, 1.0]]
    Homo = Homography(homographyMatrix=mat)
    p = 3.5, 2.0
    affineH = np.array([[2, 0, 0], [0, 3, 0], [0, 0, 1]], dtype=np.float64).tolist()
    h = Homography(homographyMatrix=affineH)
    actual1, actual2 = h.forwardProject(p)
    print(actual1,actual2)