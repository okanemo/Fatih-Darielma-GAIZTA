'''
[2] Buatlah sebuah fungsi untuk merubah “kalimat” menjadi multi dimensional array kalimat[kata[huruf]],
	tanpa menggunakan fungsi split() atau explode()

Test Case:
kalimat = "saya suka coding"
stringToArray(kalimat) //return [[s,a,y,a], [s,u,k,a], [c,o,d,i,n,g]]

by Fatih Darielma Gaizta
'''

def stringToArray(string):
	arr = []
	tmp = string + ' '
	idx = 0
	for i in range(len(tmp)):
		if tmp[i] == ' ':
			elmt = tmp[idx:i]
			arr.append(list(elmt))
			idx = i + 1
	return arr

''' Driver untuk stringToArray(string)  '''
if __name__ == '__main__':
	print(stringToArray('saya suka coding'))	# Expected: [[s,a,y,a], [s,u,k,a], [c,o,d,i,n,g]]
	print(stringToArray('saya suka chiggo'))	# Expected: [[s,a,y,a], [s,u,k,a], [c,h,i,g,g,o]]
	print(stringToArray('semakin di depan'))	# Expected: [[s,e,m,a,k,i,n], [d,i], [d,e,p,a,n]]