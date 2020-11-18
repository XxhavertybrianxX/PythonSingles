
import os, os.path,time,datetime,asyncio
import win32com.client as win32
import win32com.client.gencache as gc
from pathlib import Path as pth

from inspect import getmembers
oldcwd = os.getcwd()

#Session = gc.EnsureDispatch("MAPI.Session")


#Session.Logon(0)

        # no mapi.Session - let's try outlook

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



try:
    comadmin = gc.EnsureDispatch("Windows.Storage.Search")
    listproperties(comadmin,"MailItem")
except AttributeError:
    import re,sys,shutil
    MODULE_LIST = [m.__name__ for m in sys.modules.values()]
    for module in MODULE_LIST:
        if re.match(r'win32com\.gen_py\..+', module):
            delfsys.modules[module]
    shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
    comadmin = gc.EnsureDispatch('Windows.Storage.Search')



"""
collApps = comadmin.GetCollection("Applications")
listproperties(collApps,"apps")
collApps.Populate
print(collApps.Count)
"""
# listproperties(outapp,"cad")
