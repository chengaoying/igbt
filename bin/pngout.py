import sys
import os
if len(sys.argv) < 2:
	print "please input the path you want to compress"
	sys.exit(-1)
for path in sys.argv[1:]:
	for root, dirs, files in os.walk(path):
		for filespath in files:
			fullpath = os.path.join(root,filespath)
			if fullpath.endswith(".png"):
				os.system("pngout-win32.exe"+" "+fullpath)