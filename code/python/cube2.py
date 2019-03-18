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
			if i > 0:
				output += "    \\"
				for j in range(1,i):
					output += "/    \\"
			output += "\n"

			# draw top row of squares
			output += space[1
