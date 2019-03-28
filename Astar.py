def ManhattanDist(I, J, Iout, Jout):
	return (abs(I - Iout) + abs(J - Jout))

def IsPathValid(matriks, visited, I, J):
	ret = 0
	if (I >= 0 and J >= 0 and I < len(matriks) and J < len(matriks[0])):
		if (visited[I][J] == 0 and matriks[I][J] == 0):
			ret = 1
	return ret

		
#asumsikan queue tidak kosong
def Insert(ML, L):
	i = 0
	if (len(ML) > 0):
		#pengecekan elemen indeks 0..N-2
		while ((L[2] + L[3]) > (ML[i][2] + ML[i][3]) and i <len(ML)-1):
			i = i + 1
		#jika elemen terakhir < elemen yg mau disisip (N-1)
		if ((L[2] + L[3]) > (ML[i][2] + ML[i][3])):
			ML.append(L)
		else:
		#sudah berada di posisi pas
			ML.insert(i, L)
	else:
		ML.append(L)

#input	:	matriks jalur
#			jalur masuk dan keluar

def astar(matriks, visited, Ii, Ji, If, Jf):
	#asumsi entrJ dan out sudah benar
	steppedCost = 0
	upperBound = len(matriks)**2
	queue =[[Ii, Ji, steppedCost, ManhattanDist(Ii, Ji, If, Jf)]]
	found = False
	finished = False
	while (finished == False):
		#masukkan simpul tetangga ke queue
		if (upperBound > steppedCost and queue.count() > 0):
			#MoveLeft
			if (IsPathValid(matriks, visited, Ii, Ji - 1) == 1):
				tempList = [Ii, Ji - 1, steppedCost, ManhattanDist(Ii, Ji - 1, If, Jf)]
				Insert(queue, tempList)
			#MoveRight
			if (IsPathValid(matriks, visited, Ii, Ji + 1) == 1):
				tempList = [Ii, Ji + 1, steppedCost, ManhattanDist(Ii, Ji + 1, If, Jf)]
				Insert(queue, tempList)
			#MoveDown
			if (IsPathValid(matriks, visited, Ii + 1, Ji) == 1):
				tempList = [Ii + 1, Ji, steppedCost, ManhattanDist(Ii + 1, Ji, If, Jf)]
				Insert(queue, tempList)
			#MoveUp
			if (IsPathValid(matriks, visited, Ii - 1, Ji) == 1):
				tempList = [Ii - 1, Ji, steppedCost, ManhattanDist(Ii - 1, Ji, If, Jf)]
				Insert(queue, tempList)
			#buang list sekarang
			visited[Ii][Ji] = 7
			steppedCost = (queue.pop(0))[2] + 1
			if (Ii == If and Ji == Jf):
				upperBound = steppedCost
				found = True

				Ii = queue[0][0]
				Ji = queue[0][1]

		elif (upperBound <= steppedCost and queue.count() > 0):
			visited[Ii][Ji] = 7
			steppedCost =(queue.pop(0))[2]
		else:
			finished = True
			#Periksa sisa elemen pada Queue yg F(N) < upperBound
	while (queue.count >0):
		costList = queue.pop(0)
		cost = costList[2] + costList[3]
		#if (cost < upperBound):


def main():
	#external readfile
	matriks = open('testfile.txt').read()
	matriks = [line.split() for line in matriks.split('\n')[:-1]]
	for i in range(len(matriks)):
		matriks[i] = list("".join(map(str,matriks[i])))

	#CASTING
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			matriks[i][j] = int(matriks[i][j])

	#CETAK
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			print(matriks[i][j], end = " ")
		print()
	print()

	#VISITED
	visited = []
	for i in range (0, len(matriks), 1):
		visited.append([])
		for j in range(0, len(matriks), 1):
			visited[i].append(0)


	astar(matriks, visited, 1, 0, 9, 10)
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			if (matriks[i][j] == 1):
				print("#", end = " ")
			elif (visited[i][j] == 7):
				print("O", end = " ")
			else:
				print(" ", end = " ")
		print()

if __name__ == "__main__":
	main()