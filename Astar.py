import matplotlib.pyplot as plt
import sys

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

def astar(matriks, visited, Ii, Ji, If, Jf):
	#asumsi entrJ dan out sudah benar
	steppedCost = 0
	upperBound = len(matriks)**2
	queue =[[Ii, Ji, steppedCost, ManhattanDist(Ii, Ji, If, Jf)]]
	found = False
	finished = False
	while (finished == False):
		#masukkan simpul tetangga ke queue
		if (upperBound > steppedCost and Count(queue) > 0):
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

		elif (upperBound <= steppedCost and Count(queue)> 0):
			visited[Ii][Ji] = 7
			steppedCost =(queue.pop(0))[2]
		else:
			finished = True
			#Periksa sisa elemen pada Queue yg F(N) < upperBound

def backtrack(visited, Ii, Ji, If, Jf, solution):
	if (Ii == If and Ji == Jf):
		solution[Ii][Ji] = 1
		return True
	if (visited[Ii][Ji] == 7 and solution[Ii][Ji] == 0):
		solution[Ii][Ji] = 1

		if (backtrack(visited, Ii + 1, Ji, If, Jf, solution)== True ):
			return True
		if (backtrack(visited, Ii - 1, Ji, If, Jf, solution) == True):
			return True
		if (backtrack(visited, Ii, Ji + 1, If, Jf, solution) == True):
			return True
		if (backtrack(visited, Ii, Ji - 1, If, Jf, solution) == True):
			return True
		solution[Ii][Ji] = 0
		return False

def printPath(matriks, path, flag):
	for i in range (0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			if (matriks[i][j] == 1):
				print(u'\u2588', end =u'\u2588')
			elif (path[i][j] == flag):
				print("o", end = " ")
			else:
				print(" ", end = " ")
		print()

def main():
	matriks = []
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
	solution = []
	for i in range (0, len(matriks), 1):
		visited.append([])
		solution.append([])
		for j in range(0, len(matriks), 1):
			solution[i].append(0)
			visited[i].append(0)

	#astar(matriks, visited, path, 11, 0, 27, 40)
	astar(matriks, visited, 1, 0, 9, 10)
	printPath(matriks, visited, 7)
	if (backtrack(visited, 1, 0, 9, 10, solution) == True):
		printPath(matriks, solution, 1)
	else:
		print("Solution doesn't exist")
	#printPath(matriks, visited)

if __name__ == "__main__":
	main()