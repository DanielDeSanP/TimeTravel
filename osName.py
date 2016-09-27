import os
import sys

sisOperativo = sys.platform
clear = ""
if sisOperativo == "darwin" or sisOperativo == "linux2":
	clear = lambda : os.system("clear")
else:
	clear = lambda : os.system("cls")