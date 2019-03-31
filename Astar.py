import time
import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

def ManhattanDist(I, J, Iout, Jout):
	return (abs(I - Iout) + abs(J - Jout))

# Cek jika jalan in boundary dan merupakan jalan, bukan dinding
def IsPathValid(matriks, visited, I, J):
	ret = 0
	if (I >= 0 and J >= 0 and I < len(matriks) and J < len(matriks[0])):
		if (visited[I][J] == 0 and matriks[I][J] == 0):
			ret = 1
	return ret
		
# Memasukkan Elemen tuple ke dalam list dengan terurut menurut COSTNYA
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

# Banyak elemen di dalam LIST
def Count(L):
	count = 0
	for i in L:
		count += 1
	return count

# Algoritma A*
def astar(matriks, visited, Ii, Ji, If, Jf):
	#asumsi entrJ dan out sudah benar
	steppedCost = 0
	upperBound = len(matriks)**2
	queue =[[Ii, Ji, steppedCost, ManhattanDist(Ii, Ji, If, Jf)]]
	found = False
	finished = False
	while (finished == False):
		printPath(matriks, visited, 7)
		#time.sleep(0.1)
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

# Mencari Jalur dari simpul-simpul yang pernah dilalui
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

# Mencetak jalur di CONSOLE
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

# Menghitung Banyak Step / Jalan ke TUJUAN
def step(solution, flag):
    count = 0
    for i in range(0, len(solution), 1):
        for j in range(0, len(solution), 1):
            if (solution[i][j] == flag):
                count = count + 1
    return count

# Gabungkan solusi dengan matriks peta utk proses GUI
def join(matriks, solution):
	for i in range(0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			matriks[i][j] += 3
			if (solution[i][j] == 1):
				matriks[i][j] = 7
			
	
def main():
	matriks = []
	visited = []
	textFile = input()

	Iin, Jin = input().split(" ")
	Iin, Jin = int(Iin), int(Jin)
	Iout, Jout = input().split(" ")
	Iout, Jout = int(Iout), int(Jout)

	#external readfile
	textFile += ".txt"
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

	astar(matriks, visited, Iin, Jin, Iout, Jout)
	if (backtrack(visited, Iin, Jin, Iout, Jout, solution) == True):
		print(step(solution, 1))
		join(matriks, solution)
		plt.matshow(matriks)
		plt.show()
	else:
		print("Solution doesn't exist")
	printPath(matriks, visited)

if __name__ == "__main__":
	main()