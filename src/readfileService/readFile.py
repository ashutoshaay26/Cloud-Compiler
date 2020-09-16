import os

def readFILE(language, userID ,filename):
	if language=='py3':
		language='py'

	if not os.path.exists('../repository'):
		return "Data not exists"

	if not os.path.exists('../repository/'+str(userID)):
		return "Data not exists"

	if not os.path.exists('../repository/'+str(userID)+'/'+language):
		return "Data not exists"

	filepath = '../repository/'+str(userID)+'/'+language+'/'+filename+'.'+language
	if not os.path.exists(filepath):
		return "File not exists"

	try:
		file_c = open(filepath,'r')
		code = file_c.read()
	except IOError:
		code = "Problem in reading file...please again"

	return code

if __name__=='__main__':
	print readFILE('c','harshmehta','hello_world')
