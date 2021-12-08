'''
[5] `self number` adalah bilangan yang tidak bisa diciptakan melalui metode 
	“penjumlahan dari suatu bilangan dengan invidu angka dari suatu bilangan tersebut”.
	Contohnya, deret `self number` dibawah 200 adalah
	1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97, 108, 110, 121, 132, 143, 154, 165, 176, 187, 198.
	Sedangkan, pada kasus diatas 87 bukan lah self number karena
	dapat diciptakan melalui bilangan 75, dengan penjabaran 75 + 7 + 5 = 87
	Begitu juga 101 bukan lah self number karena dapat diciptakan melalui bilangan 91 atau 100. 
	Dengan penjabaran 91 + 9 + 1 = 101 atau 100 + 1 + 0 + 0 = 101
	Berdasarkan penjelasan diatas, buatlah sebuah fungsi yang dapat mencetak total self number dibawah 200?

by Fatih Darielma Gaizta
'''

def get_self_number(max=200):
	''' KAMUS LOKAL: i	: integer, index of arr
					val	: integer/string, processed number
					arr	: array of integer & bool [1..max] '''
	if max < 1000:
		arr = [[i, True] for i in range(1, max)]
		for i in range(max-1):
			val = str (i + 1)										# val in string
			if len(val) == 1:
				val = int(val)										# val in integer
				if (val * 2 - 1) < max-1:
					arr[(val * 2)-1][1] = False						# val is not a self number
			elif len(val) == 2:
				st, nd = int(val[0]), int(val[1])					# The 1st and 2nd digit of val
				val  = int((st * 10) + nd)							# val in integer
				if (val + st + nd - 1) < max-1:
					arr[(val + st + nd)-1][1] = False				# val is not a self number
			elif len(val) == 3:
				st, nd, rd = int(val[0]), int(val[1]), int(val[2])	# The 1st, 2nd, and 3rd digit of val
				val = int((st * 100) + (nd * 10) + rd)				# val in integer
				if (val + st + nd + rd - 1) < max-1:
					arr[(val + st + nd + rd)-1][1] = False			# val is not a self number
		for elmt in arr:
			if elmt[1]:
				print(elmt[0], end=' ')
		print()
	else:
		print("Please keep the max value below 1000, thanks! :)")

''' Driver untuk get_self_number(max) '''
if __name__ == '__main__':
	get_self_number()			# Expected: 1 3 5 7 9 20 31 42 53 64 75 86 97 108 110 121 132 143 154 165 176 187 198
	get_self_number(max=1000)	# Expected: Please keep the max value below 1000, thanks! :)
	get_self_number(max=9)		# Expected: 1 3 5 7