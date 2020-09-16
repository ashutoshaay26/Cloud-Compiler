import os

def saveFILE(code, language, userID, filename, inp):
	if language=='py3':
		language='py'

	if not os.path.exists('../compile'):
		os.makedirs('../compile')

	if not os.path.exists('../compile/'+str(userID)):
		os.makedirs('../compile/'+str(userID))

	if not os.path.exists('../compile/'+str(userID)+'/'+language):
		os.makedirs('../compile/'+str(userID)+'/'+language)

	file_c = open('../compile/'+str(userID)+'/'+language+'/'+filename+'.'+language,'w')
	file_i = open('../compile/'+str(userID)+'/'+language+'/'+filename+'_input.txt','w')
	file_c.write(code)
	file_i.write(inp)
	file_c.close()
	file_i.close()
	return '../compile/'+str(userID)+'/'+language+'/'+filename+'.'+language

if __name__=='__main__':
	saveFILE('print(\'yes\')','py','123','1')
