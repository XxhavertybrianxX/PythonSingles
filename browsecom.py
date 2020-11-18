from win32com.client import combrowse,tlbrowse
import win32com,pywintypes,pythonwin
import os, os.path,time,datetime,asyncio,sys
import win32com.client as win32
import win32com.client.gencache as gc
from pathlib import Path as pth
#from Util.idletime import get_idle_duration
from inspect import getmembers


def listproperties(obj,obj_name):
    fields = None
    methods = None
    try:
        fields = list(obj._prop_map_get_.keys())
    except AttributeError:
        print("Object has no attribute '_prop_map_get_'")
        print("Check if the initial COM object was created with"
            "'win32com.client.gencache.EnsureDispatch()'")
        pass
    methods = [m[0] for m in getmembers(obj) if (not m[0].startswith("_")
                                            and "clsid" not in m[0].lower())]

    if len(fields) + len(methods) > 0:
        print("Members of '{}' ({}):".format(obj_name, obj))
    else:
        raise ValueError("Object has no members to print")
    if fields:
        for field in fields:
            print(f"\t\t{field}")

    if methods:
        for method in methods:
            print(f"\t\t{method}")
        else:
            print("\t\tObject has no methods to print")


cmb = combrowse.main()
lst = combrowse.HLIRoot(cmb)


l = lst.GetSubList()

for i in l:
    print(i.myobject)
    print(i.__class__)

    if i.__class__ == combrowse.HLIHeadingCategory:
        for j in i.GetSubList():
            
            print(j)
            for k in j.GetSubList():
                print(k.name)
                print(k.myobject)
    elif i.__class__ == combrowse.HLI_IEnumMoniker:
        pass

    elif i.__class__ == combrowse.HLIHeadingRegisterdTypeLibs:

        for j in i.GetSubList():
            print(combrowse.HLICLSID(j.myobject[0]).name)

            
            #print(gc.AddModuleToCache(j.myobject[0],j.myobject[1],1,0))


"""
        for i in l.GetSubList():
           # print(gc.GetModuleForTypelib(i.myobject[0], i.myobject[1], i.major, i.minor))
            print(i.ret)
            try:

                for j in i.GetSubList():
                    print(j.ret)
                    #print(gc.GetModuleForTypelib(j[0], j[1], j.major, j.minor))
            except:
                pass


                #obj = gc.EnsureDispatch(i.GetText().replace("!",""))
            pythonwin.pywin.tools.regedit.
            j = pythonwin.pythonwin.pywin.tools.HLIRegistryKey(i)
            print(j.gettext())

                win32com.client.CLSIDToClass.RegisterCLSID(objnm,i.GetText())
                try:
                    obj = gc.EnsureDispatch(i.myobject.prog_id)
                    print(listproperties(obj,i.GetText()))
                except:
                    pass
            
            #obj = gc.EnsureDispatch(gc.GetModuleForCLSID(i.myobject()),i.myobject[1])
            

            except TypeError as err:
                print(err)
                pass
            except pywintypes.com_error as err:
                print(err)
                pass
"""





        #print(i.__getattribute__('name'))
        #print(i.__getattribute__('object'))
    

#getobj = win32com.client.gencache.EnsureModule('{FD87B84E-7EE1-46A2-A528-B531BBB2A4F5}', 0, 1, 0)

#listproperties(getobj)
