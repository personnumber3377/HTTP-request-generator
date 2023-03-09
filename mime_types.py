
import sys



def get_mime_types(filename: str):
	
	fh = open(filename, "r")
	lines = fh.readlines()
	fh.close()

	mimetypes = []

	for line in lines:
		if "#" in line:
			continue
		thing = line.split("	")
		mimetype = thing[0]
		mimetypes.append(mimetype)

	return mimetypes



if __name__=="__main__":

	if len(sys.argv) < 2:
		print("Usage: "+str(sys.argv[0])+" mimetypefile")
		exit(1)

	print(get_mime_types(sys.argv[1]))