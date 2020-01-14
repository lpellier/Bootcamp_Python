class Vector:
	def __init__(self, values):
		self.values = values
		self.size = len(values)

	def __str__(self):
		txt = ""
		for i in range(self.size):
			txt += str(self.values[i]) + ', '
		return ('values = ' + txt + 'size = ' + str(self.size))

	def __add__(self, other):
		if self.size == other.size:
			for i in range(self.size):
				self.values[i] += other.values[i]
			return (self.values)
		else:
			return("Error : Different sizes")

	def __radd__(self, other):
		for i in range(self.size):
			self.values[i] += other
		return (self.values)

	def __sub__(self, other):
		if self.size == other.size:
			for i in range(self.size):
				self.values[i] -= other.values[i]
			return (self.values)
		else:
			return("Error : Different sizes")

	def __rsub__(self, other):
		for i in self.size:
			self.values[i] -= other
		return (self.values)
ß
	def __truediv__(self, other):
		if other == 0:
			return ("Error : division by zero")
			exit(0)
		if self.size == other.size:
			for i in range(self.size):
				self.values[i] /= other
			return self.values
	
	def __rtruediv__(self, other):
		if other == 0:
			return ("Error : division y zero")
			exit(0)
		if type(other) == int or type(other) == float:
			for i in range(self.size):
				self.values[i] /= other0
			return (self.values)
	
	def __mul__(self, other):
		if self.size == other.size:
			for i in range(self.size):
				self.values[i] *= other.values[i]
		return self.values

	def __rmul__(self, other):
		for i in range(self.size):
			self.values[i] *= other
		return self.values

	def __repr__(self):
		return (f'<Vector object at {hex(id(self))}>')
