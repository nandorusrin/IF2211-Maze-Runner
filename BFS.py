import matplotlib.pyplot as plt
'exec(%matplotlib inline)'

def IsPathValid(matriks, visited, I, J):
    ret = False
    if (I >= 0 and J >= 0 and I < len(matriks) and J < len(matriks[0])):
        if (visited[I][J] == 0 and matriks[I][J] == 0):
            ret = True
    return ret

#input	:	matriks jalur
#			jalur masuk dan keluar

def Count(L):
    count = 0
    for i in L:
        count += 1
    return count

def bfs(matriks, visited, path, Ii, Ji, If, Jf):
    #asumsi entrJ dan out sudah benar
    queue =[[Ii, Ji]]
    found = False
    finished = False
    while (finished == False):
        if (Count(queue) > 0):
            #masukkan simpul tetangga ke queue
            #MoveLeft
            if (IsPathValid(matriks, visited, Ii, Ji - 1) == True):
                tempList = [Ii, Ji - 1]
                queue.append(tempList)
            #MoveRight
            if (IsPathValid(matriks, visited, Ii, Ji + 1) == True):
                tempList = [Ii, Ji + 1]
                queue.append(tempList)
            #MoveDown
            if (IsPathValid(matriks, visited, Ii + 1, Ji) == True):
                tempList = [Ii + 1, Ji]
                queue.append(tempList)
            #MoveUp
            if (IsPathValid(matriks, visited, Ii - 1, Ji) == True):
                tempList = [Ii - 1, Ji]
                queue.append(tempList)
            #buang list sekarang
            visited[Ii][Ji] = 7
            if (Ii == If and Ji == Jf):
                found = True
                finished = True

            Ii = queue[0][0]
            Ji = queue[0][1]

            queue.pop(0)
        else:
            finished = True

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
    if (len(path) > 0):
        for itr in range (0, len(path), 1):
            matriks[path[itr][0]][path[itr][1]] = 7

    for i in range (0, len(matriks), 1):
        for j in range(0, len(matriks), 1):
            if (matriks[i][j] == 1):
                print(u'\u2588', end =u'\u2588')
            elif (path[i][j] == flag):
                print("o", end = " ")
            else:
                print(" ", end = " ")
        print()

def step(solution, flag):
    count = 0
    for i in range(0, len(solution), 1):
        for j in range(0, len(solution), 1):
            if (solution[i][j] == flag):
                count = count + 1
    return count

def join(matriks, solution):
	for i in range(0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			if (solution[i][j] == 1):
				matriks[i][j] = solution[i][j]

def join(matriks, solution):
	for i in range(0, len(matriks), 1):
		for j in range(0, len(matriks), 1):
			matriks[i][j] += 3
			if (solution[i][j] == 1):
				matriks[i][j] = 7

def main():
    matriks = []
    path = []
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

    bfs(matriks, visited, path, Iin, Jin, Iout, Jout)
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