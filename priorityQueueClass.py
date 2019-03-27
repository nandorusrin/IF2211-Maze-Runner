class PriorityQueue:
	#CTOR
	def __init__(self):
		#data[i] = [a, b, c]
		#a = posisi X
		#b = posisi Y
		#c = cost
		self.data = []
	#SISIP
	def Insert(self, L):
		i = 0
		if (self.IsEmpty != False):
			while (L[2] > self.data[i][2]):
				i = i + 1
			#sudah berada di posisi pas
			self.data.insert(i, L)
		else:
			self.data.append(L)
	def removeFirst(self):
		self.data.pop()


	#PRINT
	def Print(self):
		for i in range(0, self.Count(), 1):
			print(self.data[i], end = "\n")
	
	#PREDIKAT
	def Count(self):
		return self.data.count()
	def IsEmpty(self):
		return self.data.count() == 0
		
def main():
	example = PriorityQueue()
	ins1 = [11, 4, 10]
	ins2 = [12, 3, 3]
	ins3 = [4, 5, 6]
	
	example.Insert(ins1)
	example.Insert(ins3)
	example.Insert(ins2)
	example.Print()
	
#if __name__ == "__main__":
#	main()