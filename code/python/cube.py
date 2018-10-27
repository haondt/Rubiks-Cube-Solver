class Cube():
	sides = {i:[None] for i in "FRULBD"}
	# holds an array of ixi values representing the color of each square, 
	# left to right top to bottom when looking at each face	
	# each side is regarded with the front as the bottom
	# the back is regarded the same way as the front
	sidenums = {"FRULBD"[i]:i for i in range(6)}
	# maps letters (F, R, U, L, B, D) to sides 0-6
	# F: front
	# R: right side
	# U: up (top) side
	# L: left side
	# B: back (rear) side
	# D: down (bottom) side
	# color to number converters and vice versa
	sidenames = "FRULBD"
	cToN = {"RGYBOW"[i]:i for i in range(6)}
	nToC = ["RGYBOW"[i] for i in range(6)]
	sidelen = 0
	
	# lists the 4 faces and side of face that are touching the given face
	# side of face = (B)ottom, (L)eft, (R)ight or (T)op
	# clockwise
	touching = {
		"F":(("U","B"),("R","L"),("D","B"),("L","R")),
		"R":(("U","R"),("B","L"),("D","L"),("F","R")),
		"U":(("B","T"),("R","T"),("F","T"),("L","T")),
		"L":(("U","L"),("F","L"),("D","R"),("B","R")),
		"B":(("U","T"),("L","L"),("D","T"),("R","R")),
		"D":(("F","B"),("R","B"),("B","B"),("L","B"))
	}
	# perhaps easier way of defining the above would be 
	# listing the four sides that the given face touches,
	# instead of vice-versa
	def __init__(self, sidelen):
		# initialize a solved rubiks cube
		self.sidelen = sidelen
		for i in range(6):
			self.sides[self.sidenames[i]] = [self.nToC[i]+str(j) for j in range(sidelen**2)]

	def print(self):
		output = ""
		for i in self.sidenames:
			output += i + ":\n"
			for j in range(self.sidelen):
				output += "\t" + str(self.sides[i][j*3:(j*3)+3])
				output += "\n"
		return output
	
	# face FRULBD, direction 0 for clockwise, 1 for counterclockwise
	# number of rows below face to turn, should be < sidelen/2 
	# for efficiency
	# TODO
	def turn(self, face, direction, numrows):
		# rotate face
		# rotate bottom row of each of touching faces
		# get indexes of bottom row
		print(face + ":")
		print(self.touching[face])
		#temp = [self.sides[self.touching[face][-1]][i] for i in brow]
		#print(face,brow)
		for face,side in self.touching[face]:
			print(face, side)
			for row in self.getRowIndexes(side, numrows):
				
				print([self.sides[face][i] for i in row])

		for s in 'TLRB':
			pass
			#print(s)
			#print(self.sides[s])
			#print(self.getRowIndexes(s,1))
	
	# return an array of indexes for the given row parameters 
	def getRowIndexes(self, side, numrows):
		rows = []
		
		if side == 'T':
			for i in range(numrows):
				rows.append(list( \
				range(i*self.sidelen, i*self.sidelen+self.sidelen) \
				))
		elif side == 'L':
			for i in range(numrows):
				rows.append([j*self.sidelen+i for j in range(self.sidelen)])
		elif side == 'R':
			for i in range(numrows):
				rows.append([j*self.sidelen-1-i for j in range(1,self.sidelen+1)])
		
		elif side == 'B':
			for i in range(numrows):
				row = self.sidelen**2-self.sidelen*(i+1)
				row = list(range(row, row+self.sidelen))
				rows.append(row)
		return rows

	# draw (print) the FRU sides of the cube in ascii form
	def draw(self):
		# generate diagonal conversion matrix
		# 0 1  -->   0
		# 2 3  --> 1   2
		#            3
		mapping = []
		for i in range(self.sidelen):
			for j in range(i+1):
				mapping.append((self.sidelen*(j+1))-((i-j)+1))
		for i in range(self.sidelen-1,0,-1):
			for j in range(i):
				mapping.append((self.sidelen*(self.sidelen-(i-j)))+j)
		x = 0
		y = 0
		z = 0
		output = ""
		# draw top half of cube
		for i in range(self.sidelen):
			space = " "*((self.sidelen-i)*3) + "/"
			
			# draw top of squares
			# draw lines
			if i==0:
				output += space[:-1] + " "
			else:
				output += space
			# draw top mini row
			for j in range(self.sidelen):
				if i == 0:
					output += "_____ "
				else:
					output += "_____/"
			# draw bottom of corners for all but bottom one
			if(i>0):
				output += "    \\"
				for j in range(1,i):
					output += "/    \\"
			output += "\n"
			# draw top row of squares
			output += space[1:]
			for j in range(self.sidelen):
				output += "     /"
			# draw top mini corner	
			output += "\\"
			for j in range(i):
				output += "  %s /\\" % self.sides["R"][mapping[y]]
				y += 1
			output += "\n"

			# draw middle row of squares
			output += space[2:]
			for j in range(self.sidelen):
				output += "  %s  /" % self.sides["U"][x]
				x += 1
			# draw 2nd top row of corners
			output += "  \\"
			for j in range(i):
				output += "  /  \\"
			output += "\n"

		
		# draw center line
		for i in range(self.sidelen):
			output += "/_____"
		output += "/"
		# draw bottom of corners for bottom section
		output += "    \\"
		for i in range(1,self.sidelen):
			output += "/    \\"
		output += "\n"

		# draw bottom half of cube
		for i in range(self.sidelen):
			space = " "*(i*3)	
			# draw top mini row
			output += space
			for j in range(self.sidelen):
				output += "\\     "
			# draw bottom of corners for all but bottom one
			for j in range(self.sidelen-i):
				output += "\\  %s /" % self.sides["R"][mapping[y]]
				y += 1
			output += "\n"

			# draw middle mini row
			output += space + " "
			for j in range(self.sidelen):
				output += "\\  %s  " % self.sides["F"][z]
				z += 1
			for j in range(self.sidelen-i):
				output += "\\  /  "
			output += "\n"

			# draw bottom row
			output += space + "  "
			for j in range(self.sidelen):
				output += "\\_____"
			for j in range(self.sidelen-i):
				output += "\\/    "
			output += "\n"
		
		return output
	
	# TODO	
	def shuffle(self):
		pass

cube = Cube(3)
print(cube.draw())
cube.turn('F',1,1)
