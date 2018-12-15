import os, cv2, requests
from imutils import paths

# path to images url
# on windows, be aware to unicode issue (use double backslash)
urls = open("C:\\Users\\LIK\\banjir\\urls.txt")
urls = urls.read().strip().split("\n")
# path to output directory
output = "C:\\Users\\LIK\\banjir\\img\\"

counter = 1
for url in urls:
	try:
		r = requests.get(url, timeout = 60)
		p = output + "{}.jpg".format(str(counter).zfill(5))
		f = open(p, "wb")
		f.write(r.content)
		f.close()

		temp = p.split("\\")
		path = temp[0] + '\...\\' + temp[-2] + '\\'+ temp[-1]

		print ("[STATUS] - Downloaded: {}".format(path))
		counter += 1
                       
	except:
		print ("[STATUS] - Error downloading {} - Skip".format(path))

for imagepath in paths.list_images(output):
	delete = False
	try:
		image = cv2.imread(imagepath)
		if image is None:
			delete = True

	except:
		print ("[STATUS] - Exception")
		delete = True	
	
	if delete:
		print ("[STATUS] - Deleting {}".format(imagepath))
os.remove(imagepath)