def gotonextLine(k, i, z):
# base case
	if (k == i): return
	print("* ", end=""),
	gotonextLine(k + z, i, z)

# print blank space of diamond
def addblankSpaceInDiamond(j,i,z):
	if (j == i): return
	print(" ",end=""),
	addblankSpaceInDiamond(j + z, i, z)

def upperDiamond(row,i):
# base case
	if (i > row): return
	addblankSpaceInDiamond(row, i, -1)
	gotonextLine(0, i, 1)
	print("\n",end=""),
	upperDiamond(row, i + 1) # recursive call


def lowerDiamond(row,i):
# print the next line of diamond
# base case 
	if (i > row): return
	addblankSpaceInDiamond(0, i, 1)
	gotonextLine(row, i, -1)
	print("\n",end=""),
	lowerDiamond(row, i + 1)

# Code
row = 5
upperDiamond(row, 0) # print uper part of triangle
lowerDiamond(row, 1) # print lower part of diamond

# This code is contributed by akashish__
