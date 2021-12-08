'''
[4] Buatlah sebuah fungsi sum yang dapat dipanggil menggunakan:
	normal invocation function expression dan immediate invocation function expression

Test Case:
sum(2,3); 	// normal invocation return 5
sum(2)(3);	// immediate invocation also return 5

by Fatih Darielma Gaizta
'''

def sum(a, b=None):
	if b == None:
		return lambda x: x + a
	else:
		return a + b

''' Driver untuk sum(a,b) '''
if __name__ == '__main__':
	print(sum(2,3))		# Expected: 5 (Normal Invocation)
	print(sum(2)(3))	# Expected: 5 (Immediate Invocation)
	print(sum(10,12))	# Expected: 22 (Normal Invocation)
	print(sum(10)(12))	# Expected: 22 (Immediate Invocation)