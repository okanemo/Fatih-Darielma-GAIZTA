'''
[1] Buatlah sebuah fungsi untuk menvalidasi apakah sebuah kata
	dapat dibaca dengan sama ketika dibaca dari depan maupun belakang

Test Case:
sama('radar') 	// return true
sama('kodok') 	// return true
sama('sapi')	// return false

by Fatih Darielma Gaizta
'''

def sama(kata):
	is_sama = True
	l, r = 0, (len(kata) - 1)
	mid = (len(kata) + 1) / 2
	while is_sama and r > mid:
		if kata[l] != kata[r]:
			is_sama = False
		l += 1
		r -= 1
	return is_sama

''' Driver untuk sama(kata) '''
if __name__ == '__main__':
	print(sama('radar'))	# Expected: True
	print(sama('kodok'))	# Expected: True
	print(sama('macan'))	# Expected: False
	print(sama('macam'))	# Expected: True