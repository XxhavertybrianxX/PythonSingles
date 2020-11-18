from pathlib import Path



root_directory = Path('C:\\Users\\wo033632\\AppData\\Local')

#dctry = root_directory.glob('**/*') 

dct = []
dctry = root_directory.glob('*') 

def chksz(mFile):
    try:
        fsz = mFile.stat().st_size
        return fsz
    except (PermissionError,OSError) as e:
        print(e)
        return(0)


for fldr in dctry:
    try:
        if fldr.is_dir():
            
            dct.append({'folder':fldr.name,'size':str(sum(chksz(f) for f in fldr.glob('**/*') if f.is_file())/1000000)})

    except (PermissionError,OSError) as e:
        print(e)
        continue


def myFunc(e):
      return float(e['size'])



dct.sort(key=myFunc)
with open("C:\\ProgramData\\Automation\\Python\\Textfiles\\" + root_directory.name + ".txt", "w") as f:
    for k in dct:
        f.write(k['folder'] + " : " + k['size'])
        f.write("\n")

"""
        if f.is_dir():
            try:
                print(sum(f.stat().st_size))
            except PermissionError as e:
                print(e)
"""




