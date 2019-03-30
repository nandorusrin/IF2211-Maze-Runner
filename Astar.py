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

def Count(L):
	count = 0
	for i in L:
		count += 1
	return count

def Push(path, L):
	t = len(path) - 1
	if (len(path) == 0):
		path.append(L)
	elif (path[t][0] != L[0] or path[t][1] != L[1]):
		path.append(L)

#untuk mencari path optimal
def Evaluate(path, If, Jf):
	#jika elemen terakhir path bukan GOAL, buang
	#pengecekan dari GOAL ke AWAL
	#Jika path[i] dengan path[i-1] berselisih petak != 1, tahan di i
	#iterasi dari j = i-1 hingga 1, bandingkan j dengan i, jika selisih petak != 1
	#buang path[j]
	path.reverse()
	i = 0
	while (i < len(path)-1):
		if (path[0][0] == If and path[0][1] == Jf and i < len(path)-1):
			j = i
			while (ManhattanDist(path[j][0], path[j][1], path[j+1][0], path[j+1][1]) > 1) and (j != len(path)):
				path.remove(path[j+1])
				j += 1
			i += 1
		else:
			path.remove(path[0])
	path.reverse()

def astar(matriks, visited, path, Ii, Ji, If, Jf):
	#asumsi entrJ dan out sudah benar
	steppedCost = 0
	upperBound = len(matriks)**2
	queue =[[Ii, Ji, steppedCost, ManhattanDist(Ii, Ji, If, Jf)]]
	Push(path, [Ii, Ji])
	found = False
	finished = False
	while (finished == False):
		#masukkan simpul tetangga ke queue
		if (upperBound > steppedCost and Count(queue) > 0):
			#MoveLeft
			if (IsPathValid(matriks, visited, Ii, Ji - 1) == 1):
				tempList = [Ii, Ji - 1, steppedCost, ManhattanDist(Ii, Ji - 1, If, Jf)]
				Insert(queue, tempList)
				Push(path, [Ii, Ji -1])
			#MoveRight
			if (IsPathValid(matriks, visited, Ii, Ji + 1) == 1):
				tempList = [Ii, Ji + 1, steppedCost, ManhattanDist(Ii, Ji + 1, If, Jf)]
				Insert(queue, tempList)
				Push(path, [Ii, Ji+1])
			#MoveDown
			if (IsPathValid(matriks, visited, Ii + 1, Ji) == 1):
				tempList = [Ii + 1, Ji, steppedCost, ManhattanDist(Ii + 1, Ji, If, Jf)]
				Insert(queue, tempList)
				Push(path, [Ii +1, Ji])
			#MoveUp
			if (IsPathValid(matriks, visited, Ii - 1, Ji) == 1):
				tempList = [Ii - 1, Ji, steppedCost, ManhattanDist(Ii - 1, Ji, If, Jf)]
				Insert(queue, tempList)
				Push(path, [Ii -1, Ji])
			#buang list sekarang
			visited[Ii][Ji] = 7
			steppedCost = (queue.pop(0))[2] + 1
			if (Ii == If and Ji == Jf):
				upperBound = steppedCost
				found = True

			Ii = queue[0][0]
			Ji = queue[0][1]

		elif (upperBound <= steppedCost and Count(queue)> 0):
			visited[Ii][Ji] = 7
			steppedCost =(queue.pop(0))[2]
		else:
			finished = True
			#Periksa sisa elemen pada Queue yg F(N) < upperBound
	Evaluate(path, If, Jf)

def printPath(matriks, path):
	if (len(path) > 0):
		for itr in range (0, len(path), 1):
			matriks[path[itr][0]][path[itr][1]] = 7

	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			if (matriks[i][j] == 1):
				print("#", end = " ")
			elif (matriks[i][j] == 7):
				print("O", end = " ")
			else:
				print(" ", end = " ")
		print()

def main():
	matriks = []
	path = []
	visited = []
	textFile = "testfile.txt"

	#external readfile
	matriks = open(textFile).read()
	matriks = [line.split() for line in matriks.split('\n')[:-1]]
	for i in range(len(matriks)):
		matriks[i] = list("".join(map(str,matriks[i])))

	#CASTING
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			matriks[i][j] = int(matriks[i][j])

	for i in range (0, len(matriks), 1):
		visited.append([])
		for j in range(0, len(matriks), 1):
			visited[i].append(0)

	print(matriks[10])
	#Small
	#astar(matriks, visited, path, 1, 0, 9, 10)
	#Med
	#astar(matriks, visited, path, 1, 0, 1, 20)
	#Large
	#astar(matriks, visited, path, 1, 0, 29, 30)
	#XLarge
	astar(matriks, visited, path, 11, 0, 27, 40)
	printPath(matriks, path)

if __name__ == "__main__":
	main()