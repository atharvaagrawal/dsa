# File Rename - to _

import os

# folder = "."

subdirs = [x[0] for x in os.walk('.')]
print(subdirs)

# Iterate
for folder in subdirs:
	print(folder)
	for file in os.listdir(folder):
		# print(file)
		
		oldName = os.path.join(folder, file)
		# print(oldName)
		x = oldName.replace("-", "_")

		n = os.path.splitext(file)[0]
		# print(x)
		# b = n + '_new' + '.txt'
		newName = os.path.join(x)
		print(newName)
		# Rename the file
		os.rename(oldName, newName)
	subdirs = [x[0] for x in os.walk('.')]
	res = os.listdir(folder)
	print(res)	