from priorityQueueClass import PriorityQueue

def ManhattanDist(X, Y, Xout, Yout):
	return (abs(X - Xout) + abs(Y - Yout))

#validasi apakah petak matriks tsb adalah path
def IsXYValid(matriks, X, Y):
	valid = False
	if (X >= 0 and Y >= 0 and X < len(matriks[0]) and Y < len(matriks)):
		valid = True
	return valid

def IsPathValid(matriks, visited, X, Y):
	valid = False
	if (IsXYValid(matriks, X, Y) and matriks[X][Y] == 0 and visited[X][Y] == True):
		valid = True
	return valid
		
	
#input	:	matriks jalur
#			jalur masuk dan keluar

def astar(matrix, visited, Xi, Yi, Xf, Yf):
	#asumsi entry dan out sudah benar
	steppedCost = 0
	queue = PriorityQueue()
	tempList = [Xi, Yi, steppedCost + ManhattanDist(Xi, Yi, Xf, Yf)]
	queue.Insert(tempList)

	while (Xi != Xf and Yi != Yf):
		#buang list sekarang
		steppedCost = 2
		queue.removeFirst()
		#masukkan simpul tetangga ke queue
		#MoveLeft
		if (IsPathValid(matrix, visited, Xi - 1, Yi) == True):
			tempList = [Xi - 1, Yi, steppedCost + ManhattanDist(Xi - 1, Yi, Xf, Yf)]
			queue.Insert(tempList)




def main():
	matriks = 	[[1, 1, 1, 0, 1, 1],
				[1, 0, 1, 0, 1, 1],
				[1, 0, 0, 0, 0, 1],
				[0, 0, 1, 1, 0, 1],
				[1, 0, 0, 0, 0, 1],
				[1, 1, 1, 1, 1, 1]]
	visited = matriks
	for i in range (0, len(visited), 1):
		for j in range (0, len(visited[0]), 1):
			visited[i][j] = False
	print(visited)
	print(IsXYValid(matriks, -12, 0))

if __name__ == "__main__":
	main()