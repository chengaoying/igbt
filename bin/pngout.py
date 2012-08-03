import sys
import os
if len(sys.argv) < 2:
	print "please input the path you want to compress"
	sys.exit()
for root, dirs, files in os.walk(sys.argv[1]):
	for filespath in files:
		fullpath = os.path.join(root,filespath)
		if fullpath.endswith(".png"):
			os.system("pngout-win32.exe"+" "+fullpath)