class PriorityQueue:
	#CTOR
	def __init__(self):
		#data[i] = [a, b, c]
		#a = posisi X
		#b = posisi Y
		#c = cost
		self.data = []
		self.size = 0
	#SISIP
	def Insert(self, L):
		i = 0
		if (self.size > 0):
			while ((L[2] + L[3]) > (self.data[i][2] + self.data[i][3])):
				i = i + 1
			#sudah berada di posisi pas
			self.data.insert(i, L)
		else:
			self.data.append(L)
		self.size += 1
	def removeFirst(self):
		self.size -= 1
		return (self.data.pop(0))[2]

	#GETTER
	def GetFirstI(self):
		if (self.size > 0):
			return self.data[0][0]
	def GetFirstJ(self):
		if (self.size > 0):
			return self.data[0][1]
	#PRINT
	def Print(self):
		for i in range(0, self.size, 1):
			print(self.data[i], end = "\n")
	
	#PREDIKAT
	def Count(self):
		return self.data.count
	def IsEmpty(self):
		if self.data.count == 0:
			return True
		else:
			return False
		
def main():
	example = PriorityQueue()
	ins1 = [11, 4, 10, 4]
	ins2 = [12, 3, 3, 3]
	ins3 = [4, 5, 6, 2]
	
	example.Insert(ins1)
	example.Insert(ins3)
	example.Insert(ins2)
	example.Print()
	q = example.removeFirst()
	print(q)
	example.Print()
	print(type(example.GetFirstI()))
	
if __name__ == "__main__":
	main()