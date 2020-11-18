from pathlib import Path

import os,time,glob,datetime


import fnmatch

import os.path
import re



def chksz(mFile):
    try:
        fsz = mFile.stat().st_size
        return fsz
    except (PermissionError,OSError) as e:
        print(e)
        return(0)

"""
      
def foldersize(mfile):
    for fldr in dctry:
        try:
            if fldr.is_dir():
                
                dct.append({'folder':fldr.name,'size':str(sum(chksz(f) for f in fldr.glob('**/*') if f.is_file())/1000000)})

        except (PermissionError,OSError) as e:
            print(e)
            continue
    dct.sort(key=myFunc)

"""

def datetime_to_float(d):
    d = datetime.datetime.strptime(d, '%c')
    epoch = datetime.datetime.utcfromtimestamp(0)
    total_seconds =  (d - epoch).total_seconds()
    # total_seconds will be in decimals (millisecond precision)
    return total_seconds

def myFunc(e,sorton=None):
      
      return datetime_to_float(e[sorton])


def filerecursor(rootpath,excludes,mdict,searchstr):

    rpath = Path(rootpath)
    rootdir = rpath.glob('./*') 
    for f in rootdir:
        if f.is_file():
            if searchstr in f.name:
                abspth = rootpath + "\\" + f.name
                mtime = time.ctime(os.path.getmtime(abspth))  
                mdict.append({'folder':abspth,'filenm':f.name,'date':mtime})
        if f.is_dir():
            i = 0
            for exc in excludes:

                if re.match(exc, f.name):
                    i = 1
            if i == 0:
                abspth = rootpath + "\\" + f.name
                try:
                    filerecursor(abspth,excludes,mdict,searchstr)
                except OSError as e:
                    print(e)
                    pass
    return mdict
    
    

def foldersearch(rootpath,excludes,searchstring,sorton):
    from functools import partial


    mdct = []
    mdct  = filerecursor(rootpath,excludes,mdct,searchstring)
    #for f in fldr.glob(finsrch):


    func = partial(myFunc,sorton=sorton)
    mdct.sort(key=func)
    print(mdct)
    return mdct


def writedicttotext(dct,rootdir):

    with open("C:\\ProgramData\\Automation\\Python\\Textfiles\\" + rootdir + ".txt", "w") as f:
        for k in dct:
            f.write(str(k))
            f.write("\n")


def runlookup(rootdirnm,rootpath,srch,sort,excludes):

    apspthDir = rootpath + "\\" + rootdirnm

    print(apspthDir)


    mdct = foldersearch(apspthDir,excludes,srch,sort)

    writedicttotext(mdct,rootdirnm)
