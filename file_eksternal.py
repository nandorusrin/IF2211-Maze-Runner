grid = open('testfile.txt').read()
grid = [line.split() for line in grid.split('\n')[:-1]]
for i in range(len(grid)):
	grid[i] = list("".join(map(str,grid[i])))
        
def main():
	for i in range(len(grid)):
		print(grid[i])

main()		
input()