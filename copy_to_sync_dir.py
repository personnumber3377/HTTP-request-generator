
import os
import sys


if __name__=="__main__":

	if len(sys.argv) < 3:
		print("Usage: "+str(sys.argv[0]) + "ORIGINAL_FILES SYNCDIR")
		exit(1)

	original_dir = sys.argv[1]

	sync_dir = sys.argv[2]

	files = os.listdir(original_dir)

	if original_dir[-1] != "/":
		original_dir += "/"

	if sync_dir[-1] != "/":
		sync_dir += "/"

	id_count = 20

	for file in files:

		length = 6-len(str(id_count))
		filename = "id:"+str(length*"0")+str(id_count)+",stuffwhatever"

		print("Running: "+str("cp "+str(original_dir)+str(file) + " "+str(sync_dir)+filename))
		os.system("cp "+str(original_dir)+str(file) + " "+str(sync_dir)+filename)
		id_count += 1






