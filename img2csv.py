import numpy
import Image
import ImageOps
import ImageFilter

import sys
import glob

def usage():
	print "./img2csv.py img csv"

if len(sys.argv) != 3:
	usage()
	exit(0)
	
_, imgPath, csvPath = sys.argv

def gs(path):
	im = Image.open(path)
	im = ImageOps.grayscale(im)
	im.save("%s_gs.png" % path.split(".")[0])
	return im

def resize(im, x, y):
	return im.resize((x, y))

def edge(im):
	return im.filter(ImageFilter.FIND_EDGES)
	
def img2text(path):
	im = resize(gs(path), 48, 48)
#	im.save("gs.png")
	l = (numpy.asarray(im).flatten() / 255.0).tolist()
	#l = [1 if e > 0.5 else 0 for e in l]
	l = [str(e) for e in l]
	return " ".join(l)
	
def img2csv(imgPath, csvPath):
	import csv
	f = open(csvPath, "w")
	writer = csv.writer(f)
	writer.writerow([1,1])
	for e in glob.glob(imgPath):
		print e
		l = img2text(e)
		writer.writerow([1, l])
	f.close()

if __name__ == "__main__":
	img2csv(imgPath, csvPath)

