class Cube():
	# holds an nxn matrix representing each side of the cube
	cube = {i:None for i in "FRULBD"}
	# holds the dimensions of the cube
	sidelen = 0
	
	# holds colors of cube
	colors = "RGYBOW"
	# holds the faces of cube
	faces = "FRULBD"

	# initializes a solved cube
	def __init__(self, sidelen):
		self.sidelne = sidelen
		for i in range(6):
			face = self.faces[i]
			color = self.colors[i]
			self.cube[face] = [[color for j in range(sidelen)] for k in range(sidelen)]
	
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
