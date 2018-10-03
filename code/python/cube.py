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
	cToN = {["red", "green", "yellow", "blue","orange","white"][i]:i for i in range(6)}
	nToC = [["red", "green", "yellow", "blue","orange","white"][i] for i in range(6)]
	sidelen = 0
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
		pass

	# draw (print) the FRU sides of the cube in ascii form
	def draw(self):

		# draw top half of cube
		for i in range(self.sidelen):
			space = " "*((self.sidelen-i)*3) + "/"
			
			# draw top of squares
			# draw lines
			if i==0:
				print(space[:-1] + " ", end="")
			else:
				print(space, end="")
			# draw top mini row
			for j in range(self.sidelen):
				if i == 0:
					print("_____ ", end="")
				else:
					print("_____/", end="")
			# draw bottom of corners for all but bottom one
			if(i>0):
				print("    \\", end="")
				for j in range(1,i):
					print("/    \\", end="")
			print()
			# draw top row of squares
			print(space[1:], end="")
			for j in range(self.sidelen):
				print("     /", end="")
			# draw top mini corner	
			print("\\", end="")
			for j in range(i):
				print("  Y /\\",end="")
			print()

			# draw middle row of squares
			print(space[2:], end="")
			for j in range(self.sidelen):
				print("  X  /", end="")
			# draw 2nd top row of corners
			print("  \\", end="")
			for j in range(i):
				print("  /  \\", end="")
			print()

		
		# draw center line
		for i in range(self.sidelen):
			print("/_____", end="")
		print("/", end="")
		# draw bottom of corners for bottom section
		print("    \\", end="")
		for i in range(1,self.sidelen):
			print("/    \\",end="")
		print()

		# draw bottom half of cube
		for i in range(self.sidelen):
			space = " "*(i*3)	
			# draw top mini row
			print(space, end="")
			for j in range(self.sidelen):
				print("\\     ", end="")
			# draw bottom of corners for all but bottom one
			for j in range(self.sidelen-i):
				print("\\  Y /", end="")
			print()

			# draw middle mini row
			print(space + " ",end="")
			for j in range(self.sidelen):
				print("\\  Z  ", end ="")
			for j in range(self.sidelen-i):
				print("\\  /  ", end="")
			print()

			# draw bottom row
			print(space + "  ", end="")
			for j in range(self.sidelen):
				print("\\_____", end="")
			for j in range(self.sidelen-i):
				print("\\/    ", end="")
			print()
	
	# TODO	
	def shuffle(self):
		pass
cube = Cube(3)

cube.draw()
