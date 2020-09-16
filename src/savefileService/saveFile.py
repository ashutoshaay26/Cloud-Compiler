import os

def saveFILE(code, language, userID, filename, inp):
	if language=='py3':
		language='py'

	if not os.path.exists('../repository'):
		os.makedirs('../repository')

	if not os.path.exists('../repository/'+str(userID)):
		os.makedirs('../repository/'+str(userID))

	if not os.path.exists('../repository/'+str(userID)+'/'+language):
		os.makedirs('../repository/'+str(userID)+'/'+language)

	file_c = open('../repository/'+str(userID)+'/'+language+'/'+filename+'.'+language,'w')
	file_i = open('../repository/'+str(userID)+'/'+language+'/'+filename+'_input.txt','w')
	file_c.write(code)
	file_i.write(inp)
	file_c.close()
	file_i.close()
	return '../repository/'+str(userID)+'/'+language+'/'+filename+'.'+language

if __name__=='__main__':
	saveFILE('print(\'yes\')','py','123','1')
