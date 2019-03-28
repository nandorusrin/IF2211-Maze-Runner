def main():
	#external readfile
	matriks = open('testfile.txt').read()
	matriks = [line.split() for line in matriks.split('\n')[:-1]]
	for i in range(len(matriks)):
		matriks[i] = list("".join(map(str,matriks[i])))
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			matriks[i][j] = int(matriks[i][j])
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			print(matriks[i][j], end = " ")
		print()
	print()
	
main()		
