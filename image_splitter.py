#%%

import cv2
import numpy as np
import os

def image_splitter(imagefn,desiredheight,desiredwidth,outputinfo=None,overlap=0.0):
    """_summary_

    Parameters
    ----------
    imagefn : string
        filename with full path
    desiredheight : integer
        the desired height of each tile
    desiredwidth : integer
        the desired height of each tile
    outputinfo : dict, optional
        a dict with keys 'prefix' for prefix
        'sufix' for sufix and 'path' for the output path
        by default None
    overlap : float, optional
        fraction of overlap between tiles, if any
        by default 0.0

    Returns
    -------
    _type_
        _description_
    """
    rois=list()
    verbose=0
    try:
        #rewrite using pathlib, OS indenpendent
        image=cv2.imread(imagefn)
        purefn=os.path.basename(imagefn)
        filepath=os.path.dirname(imagefn)
        
        if verbose: print("processing file "+purefn)
        fileext=os.path.splitext(purefn)[-1]
        filenamenoext=os.path.splitext(purefn)[:-1][0]
        if verbose: print(filenamenoext)

        strideW=overlap*desiredwidth
        strideH=overlap*desiredheight
        inputwidth=image.shape[1]
        inputheight=image.shape[0]

        xmin=0
        ymin=0
        xmax=desiredwidth
        ymax=desiredheight
        
        rois=list()
        last=False

        while not(last):
            xmin=0
            xmax=desiredwidth
            
            while True:

                if xmax>=inputwidth:
                    xmin=inputwidth-desiredwidth
                    xmax=inputwidth
                    dummy=[xmin,ymin,xmax,ymax]
                    rois.append(dummy)
                    if verbose: print(dummy)
                    break

                dummy=[xmin,ymin,xmax,ymax]
                if verbose: print(dummy)
                rois.append(dummy)
                xmin+=round(desiredwidth-strideW)
                xmax+=round(desiredwidth-strideW)

            if ymax>=inputheight and xmax>=inputwidth:
                if verbose: print("out")
                last=True
            
            else:
                ymin+=round(desiredheight-strideH)
                ymax+=round(desiredheight-strideH)
                if ymax>=inputheight:
                    if verbose: print("last row")
                    ymin=inputheight-desiredheight
                    ymax=inputheight
        
    except:
        print("cant open image")
        return None
        
    
    outputpath=''
    outputprefix=''
    outputsuffix=''

    if outputinfo!=None:
    
        if type(outputinfo)==dict:
            if 'prefix' in outputinfo.keys():
                outputprefix=outputinfo['prefix']
            elif 'suffix' in outputinfo.keys():
                outputsuffix=outputinfo['suffix']
            elif 'path' in outputinfo.keys():
                outputpath=outputinfo['path']
    else:
        outputpath=filepath+'/'
    counter=0
    for i in rois:
        roi=image[i[1]:i[3],i[0]:i[2]]
        if outputprefix=='':
            outputfn=outputpath
        else:
            outputfn=outputpath+outputprefix
        outputfn+=str(filenamenoext)+'_'
        outputfn+=str(counter)
        if outputsuffix=='':
            outputfn+='_'+ fileext
        else:
            outputfn+=+'_'+outputsuffix+ fileext
        print('writing '+outputfn)
        cv2.imwrite(outputfn,roi)
        counter+=1

    return rois


def main():
    imagepath="/home/abarrios/Pictures/"   
    splitpath="/home/abarrios/Pictures/ig"
    imagename="Mudo5fd.jpeg"
    dummy=os.listdir(splitpath)
    print(dummy)
    fn=imagepath+'barco 1.jpg'
    salida={'path':splitpath,'prefix':'','suffix':'sub'}
    salida={'path':splitpath}
    cajitas=image_splitter(fn,4068,4068,salida,0.0)

    return cajitas




if __name__=="__main__":
    cajitas=main()
