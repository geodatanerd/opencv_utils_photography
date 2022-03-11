#%%
# Inspired,-copied from
#https://www.youtube.com/watch?v=oXlwWbU8l2o

import cv2
import numpy as np
import matplotlib.pyplot as plt


def rescaleFrame(frame,scale=0.75):

    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)

    return cv2.resize(frame,dimensions,interpolation=cv2.INTER_CUBIC)

#def changeRes(w,h):

def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    #print(transMat)
    dimensions=(img.shape[1],img.shape[0])

    return cv2.warpAffine(img,transMat,dimensions)


def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat=cv2.getRotationMatrix2D(rotPoint,angle=angle,scale=1.0)
    dimensions=(width,height)
    return cv2.warpAffine(img,rotMat,dimensions,cv2.INTER_CUBIC,borderMode=cv2.BORDER_TRANSPARENT)

def randomColor(seed=10):
    import random
    random.seed(seed)
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)


def imageHistograms(img,n_bins=50,LOG=False):
    
    
    rows,cols,bands=img.shape
    

        

    b,g,r=cv2.split(img)
    channels=[(b,'blue','b'),(g,'green','g'),(r,'red','r')]
    fig, axs=plt.subplots(3,1,sharey=True,tight_layout=True)
    for c,k in enumerate(channels):
        print(c)
        print(k[0].shape)

        axs[c].hist(np.reshape(k[0],
            (rows*cols,1)),
            bins=n_bins,
            density=True,
            histtype='stepfilled',
            facecolor=k[2],log=LOG)
        axs[c].set_title(k[1]+ " channel")
    plt.show()
    



