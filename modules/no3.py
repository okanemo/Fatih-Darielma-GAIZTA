'''
[3] Buatlah sebuah fungsi untuk memfilter jika nilai array lebih dari 5 dan lebih kecil dari sama dengan 8,
	serta diurutkan dari kecil ke besar dan hilangkan duplikasi.

numbers = [3,2,1,2,1,4,6,5,7,8,8,9,2]
filterNumber(numbers) // return [1,2,3,4,5,9]

by Fatih Darielma Gaizta
'''

def filterNumber(arr):
	return sorted(list(set([i for i in arr if (i <= 5 or i > 8)])))

''' Driver untuk filterNumber(arr) '''
if __name__ == '__main__':
	print(filterNumber([3,2,1,2,1,4,6,5,7,8,8,9,2]))	# Expected: [1,2,3,4,5,9]
	print(filterNumber([1111,2,3,1,14,5,4,6,7,7,9]))	# Expected: [1,2,3,4,5,9,14,1111]
	print(filterNumber([-1,-2,-30,0,1,2,30,5,60,7]))	# Expected: [-30,-2,-1,0,1,2,5,30,60]