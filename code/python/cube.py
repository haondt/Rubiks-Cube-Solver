class Cube():
	sides = 6*[None]
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
	cToN = {"RGYBORW"[i]:i for i in range(6)}
	nToC = ["RGYBORW"[i] for i in range(6)]
	sidelen = 0
	
	# lists the 4 faces touching given face
	# clockwise
	touching = {
		"F":"URDL",
		"R":"UBDF",
		"U":"BRFL",
		"L":"UFDB",
		"B":"ULDR",
		"D":"FRBL"
	}
	def __init__(self, sidelen):
		# initialize a solved rubiks cube
		self.sidelen = sidelen
		for i in range(6):
			self.sides[i] = [self.nToC[i] for j in range(sidelen**2)]
	def print(self):
		for i in range(6):
			print(self.sidenames[i], ":\n")
			for j in range(self.sidelen):
				print("\t", self.sides[i][j*3:(j*3)+3])
	# face FRULBD, direction 0 for clockwise, 1 for counterclockwise
	# TODO
	def turn(self, face, direction):
		# rotate face
		# rotate bottom row of each of touching faces

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
				output += "  %s /\\" % self.sides[1][mapping[y]]
				y += 1
			output += "\n"

			# draw middle row of squares
			output += space[2:]
			for j in range(self.sidelen):
				output += "  %s  /" % self.sides[2][x]
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
				output += "\\  %s /" % self.sides[1][mapping[y]]
				y += 1
			output += "\n"

			# draw middle mini row
			output += space + " "
			for j in range(self.sidelen):
				output += "\\  %s  " % self.sides[0][z]
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
cube.draw()
