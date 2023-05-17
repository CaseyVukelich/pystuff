import os, sys, getopt

file_name = ""
text_add = ""
delete = ""
rename_file = ""
owner = ""
argv = sys.argv[1:]

try:
	options, args = getopt.getopt(argv, "n:a:d:r:o:", ["file_name =", "text_add =", "delete =", "rename_file =", "owner ="])
except getopt.getopterror:
	print("not a recognized option")
	sys.exit()

#name = ""
#value = ""
#name = options

match argv[0]:
	case '-n' | '--file_name':
		file_name = argv[1]
		if 2 < len(argv):
			print("too many inputs")
		elif os.path.exists(file_name):
			print("This file exists")
		else:
			f = open(file_name, "x")
			f.close()
			print(file_name + " exists now")
	
	case '-a' | '--text_add':
		text_add = sys.argv[2:]
		for i in range(len(text_add)):
			text_add[i]
			if ".txt" in text_add[i]:
				filename = text_add[i] #if this creates an error set variable to str(x[i])
				if os.path.exists(filename):
					f = open(filename, "a")
					f.write(text_add[0])
					f.close()
					print("you have appended the file")
				else:
					f = open(filename, "w")
					f.write(text_add[0])
					f.close()
					print("the file did not exist, but it does now the the added text")
			else:
				continue

	case '-d' | '--delete':
		delete = argv[1]
		if 2 < len(argv):
			print("way too many inputs")
		elif os.path.exists(delete):
			os.remove(delete)
			print("file deleted")
		else:
			print("file does not exist, or detail not specified")
	
	case '-r' | '--rename_file':
		rename_file = argv[1:]
		a = rename_file[0]
		b = rename_file[1]
		if 2 < len(rename_file):
			print("too many inputs, enter the new name of a file, and the current name of the file")
		elif os.path.exists(b):
			print(b + " already exists, choose a different name")
		elif os.path.exists(a) == False:
			print(a + " does not exist")
		elif os.path.exists(a) and os.path.exists(b) == False:
			os.rename(a, b)
			print("you have renamed the file")
		else:
			print("error")
	
	case '-o' | '--owner':
		file_name = argv[1]
		uid = input("Enter the new owner's id:")
		gid = input("Enter the new owner's group id:")
		if os.path.exists(file_name):
			os.chown(os.path.abspath(file_name), uid, gid)
		else:
			print("that file does not exist")
	
	case _:
		print("wildcard error")