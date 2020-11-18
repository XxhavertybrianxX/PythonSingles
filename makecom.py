import sys
from win32com.client import makepy

sys.argv = ["makepy", r"c:\windows\msagent\agtctl15.tlb"]
makepy.main ()