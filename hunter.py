# Author: Mehrshad Matin






# Functions that ask the user for input
def step1():
	
	yorno = raw_input("would you like to play?")
	
	return yorno
	

def info():
	name = raw_input("Name of treasure hunter: ")
	return name 
	
def boardsize():
	size = input("Size of board (between 3 and 6 inclusive): ")
	return size
	
def randomoruser():
	creation = raw_input("Creation of board?(r-randim, u-user): ")
	return creation 
	
def usertypes():
	listoflist = input("Provide a list of lists, same number of rows and columns with integer numbers between 0 and 10 inclusive and maybe one -1 ==> ")
	return listoflist
	
	
# Shows the board (after trip board also)	
def showboard ():
	
	i=0
	for c in range(len(z)):
		print "           Col"+str(c),
	print 
	
	while i<len(z):
		b=0
		print "Row "+str(i),"      ",
		while b<len(z):
			print z[i][b],"             ",
			b=b+1
			
		print ""
		i=i+1


# Shows the option 
def decision():
			
	print "How would you want that "+player +" travels?:"
	print "r - row"
	print "c - col"
	print "m - main diagonal"
	print "s - secondary diagonal"
	
	

# User inputs the their desired rows	
def rows ( ):
	numberofrows= input("Number row (0 to "+str(len(z)-1)+"):")
	return numberofrows
	
# User inputs the their desired cols	
def cols():
	numberofcoums= input("Number colums (0 to "+str(len(z)-1)+"):")
	return numberofcoums
	
	
	
	
# Checks if there is negative in row, returns bool

def checknegativeR(numberofrows1):
		
	flag=False
	for i in range(len(z)):
		if z[numberofrows1][i]==-1:
			flag=True
			
	return flag 
	


# Checks if there is negative in coln, returns bool
def checknegativeC(numberofcols1):
	flag=False
	for i in range(len(z)):
		if z[i][numberofcols1]==-1:
			flag=True
	return flag




## Shows positions if there is negative for rows
def choiceRnegative(z,numberofrows1 ):
	i=0
	while i<len(z) and z[numberofrows1][i]!=-1:
		print [numberofrows1],[i]
		i=i+1
	print [numberofrows1],[i], "ooooh! a -1!!"
	
	
	
	
## Shows positions if there is negative for cols
def choiceCnegative(z,numberofcols1):
	i=0
	while i<len(z) and z[i][numberofcols1]!=-1:
		print [i],[numberofcols1]
		i=i+1
	print [i],[numberofcols1], "ooooh! a -1!!"


	
	
# Shows poisition visited for cols, no negative
def choiceCPositive(numberofcols1):
	i=numberofcols1
	b=0
	while b<len(z):
		print [b],[i]
		b=b+1
		
		
		
# Shows poisition visited for rows, no negative
def choiceRpositive(numberofrows1):
	i=numberofrows1
	b=0
	while b<len(z):
		print [i],[b]
		b=b+1
		
		
	
# Returns sum of points for rows
def sumpoints(numberofrows1,z):
	z1=0
	for i in range(len(z)):
					
		if (z[numberofrows1][i])%2==0:
			z1=z1+ (z[numberofrows1][i])/2
		elif (z[numberofrows1][i])%2!=0:
			z1=z1+ (z[numberofrows1][i])
	return z1
	
# Changes the board, rows
def CHANGER():
	for c in range(len(z)):
		if (z[numberofrows1][c])%2==0:
			z[numberofrows1][c]= (z[numberofrows1][c])/2
		else:
			z[numberofrows1][c]=0
	
### Returns ponits of Colns NO NEGATIVE
def sumCnonegative(z,numberofcols1):
	z1=0
	for i in range(len(z)):
		if (z[i][numberofcols1])%2==0:
			z1= z1+(z[i][numberofcols1])/2
		elif (z[i][numberofcols1])%2!=0:
			z1= z1+(z[i][numberofcols1])
			
			
	for c in range(len(z)):
		if (z[c][numberofcols1])%2==0:
			z[c][numberofcols1]=  (z[c][numberofcols1])/2
		else:
			z[c][numberofcols1]=0
			
			
	return z1 
	

# Returns position of -1, rows
def findi(z,numberofrows1):
	i=0
	while i<len(z) and z[numberofrows1][i]!=-1:
		[numberofrows1],[i]
		i=i+1
	return i
	

# Returns points for rows, if we have negative
def sumpointsnegative(findy):
	z1=0
	for b in range(0,findy):
		if (z[numberofrows1][b])%2==0:
			z1=z1+((z[numberofrows1][b]))/2
		elif (z[numberofrows1][b])%2!=0:
			z1=z1+((z[numberofrows1][b]))
			
			
				
	for c in range(0,findy):
			
		if (z[numberofrows1][c])%2==0:
			z[numberofrows1][c]= (z[numberofrows1][c])/2
		else:
			z[numberofrows1][c]=0
			
	
		
			
	return z1


#Returns position of -1 for cols
def findiC(z, numberofcols1):
	i=0
	while i<len(z) and z[i][numberofcols1]!=-1:
		[i],[numberofcols1]
		i=i+1
	return i 

#Returns points for cols, if we have negative
	
def sumCnegative(findc):
	z1=0
	for b in range(0,findc):
		if (z[b][numberofcols1])%2==0:
			z1=z1+((z[b][numberofcols1])) /2
		elif (z[b][numberofcols1])%2!=0:
			z1=z1+((z[b][numberofcols1]))
			
				
	for c in range(0,findc):
		if (z[c][numberofcols1])%2==0:
			z[c][numberofcols1]=(z[c][numberofcols1])/2
		else:
			z[c][numberofcols1]=0
			
			
	return z1
	
	
# Checks if there is negative for path M, returns bool
def checknegativeM():
	print "positions visited: ..."
	flag=False
	for i in range(len(z)):
		if z[i][i]==-1:
			flag=True
	return flag


#Shows we have negative for path M	
def Mnegativefound():
	i=0
	while i<len(z) and z[i][i]!=-1:
		print [i],[i]
		i=i+1
	print [i],[i], "ooooh! a -1!!"


# Returns points for path M if we have negative	
def sumMnegative(findb):
	z1=0
	for b in range(0,findb):
		if (z[b][b])%2==0:
			z1=z1+(z[b][b])/2
		elif (z[b][b])%2!=0:
			z1=z1+(z[b][b])			
		
	for b in range(0,findb):
		if z[b][b]%2==0:
			z[b][b]=(z[b][b])/2
		else:
			z[b][b]=0
			
			
	return z1
	

# Returns -1 position for path M
	
def findiM():
	i=0
	while i<len(z) and z[i][i]!=-1:
		[i],[i]
		i=i+1
	return i 
	

# Shows positions visited for path M
def Mnonegative():
	for g in range(len(z)):
		print [g],[g]


# Returns points for path M					
def Msum():
	z1=0
	for i in range(len(z)):
		if (z[i][i])%2==0:
			z1=z1+(z[i][i])/2
		elif (z[i][i])%2!=0:
			z1=z1+(z[i][i])
			
			
	return z1

# Changes the board, path M	
def changem():
	
	for i in range(len(z)):
		if z[i][i]%2==0:
			z[i][i]=(z[i][i])/2
		else:
			z[i][i]=0
						
							

# Checks for negative in path S	, returns bool	
def checknegativeS():
	flag=False
	i=0
	b=(len(z)-1)
	while i<len(z) and b>=0:
		if listoflist[i][b]==-1:
			flag=True
		i=i+1
		b=b-1
		
	return flag 
	

# Shows posistion visited  w/ -1 in path S	
def ShowohhS():
	i=0
	b=(len(listoflist)-1)
	while z[i][b] != -1:
		print [i],[b]
						
		i=i+1
		b=b-1
	print [i],[b], "ooooh! a -1!!"
	
#Returns postion of -1 in path S
	
def sumSnegative():
	z1=0
	i=0
	b=(len(z)-1)
	while z[i][b] != -1:
		i=i+1
		b=b-1
			
	return  i
	
	
# Returns the postion of -1 in path S (matrix)
def secondplace():
	z1=0
	i=0
	b=(len(z)-1)
	while z[i][b] != -1:
		i=i+1
		b=b-1
			
	return  b
	
	
# Shows positions visited in path S	
def Spositionsdisplay():
	i=0
	b=len(z) -1
	while i<len(z) and b>=0:
		print [i],[b]
		
		i=i+1
		b=b-1

# Returns points without negative in path S		
def SsumNONegative():
	i=0
	b=len(z) -1
	z1=0
	while i<len(z) and b>=0:
		if (z[i][b])%2==0:
			z1= z1+(z[i][b])/2
		elif (z[i][b])%2!=0:
			z1= z1+(z[i][b])
			
					
		i=i+1
		b=b-1
	return z1
	
	
# Changes the board after path S
def Schange():
	i=0
	b=len(z) -1
	while i<len(z) and b>=0:
		if z[i][b] %2 ==0:
			z[i][b]= (z[i][b])/2
		else:
			z[i][b]=0
			
		i=i+1
		b=b-1

# Chcecks if in path S we have a neagtive, returns bool
def Schecknegative():
	flag=False
	i=0
	b=(len(z)-1)
	while i<len(z) and b>=0:
		if z[i][b]==-1:
			flag=True
		i=i+1
		b=b-1
	return flag 


# Shows the -1 in path S	
def Snegativefound():
	i=0
	b=(len(z)-1)
	while i<len(z) and b>=0 and z[i][b]!=-1:
		print [i],[b]
		
		i=i+1
		b=b-1
	print [i],[b], "ooooh! a -1!!"
	

# Returns points for path S	
def sumwithnegative():
	i=0
	b=(len(z)-1)
	z1=0
	while i<len(z) and b>=0 and z[i][b]!=-1:
		if (z[i][b])%2==0:
			z1= z1+(z[i][b])/2
		elif (z[i][b])%2!=0:
			z1 = z1 + (z[i][b])
		
		i=i+1
		b=b-1
	return z1
		

		
def sumall(w2):
	
	sumofall= 0
	sumofall = sumofall + int(w2)
	return sumofall

	
	
# Changes te board to binary #	
def changetobinary():
	i=0
	while i<len(z):
		b=0
		while b<len(z):
			
			if z[i][b]%2!=0:
				z[i][b]=1
			elif z[i][b]%2==0:
				z[i][b]=0
			else:
				z[i][b]=1
			b=b+1
			
		i=i+1
		

# Shows the value for each row converted to decimal
def valueofbinary():
	kk=len(z[0])
	i=0
	m=[]
	
	while i<len(z):
		b=0
		val=0
			
		while b<len(z[0]):
			digit=z[i][b]
			ex= kk-1 -b
			h=digit*2**ex
			val=val+h
			b=b+1
		m.append(val)
		i=i+1
		
	for i in range(len(m)):
		print m[i],
	


		





# Returns the sum of all binary numbers
def luckynumber():
	kk=len(z[0])
	i=0
	sum1=0
	val=0
	m=[]
	while i<len(z):
		sum1=sum1+val
		b=0
		eachrow=0
		while b<len(z[0]):
			digit=z[i][b]
			ex= kk-1 -b
			part1=digit*2**ex
			eachrow=eachrow+part1
			b=b+1
			
			val=val+part1
		m.append(eachrow)
		i=i+1
	return val


import sys
	


firststep= raw_input("would u like to play?")

while firststep!="y" and firststep!="n":
	print "That is not a valid input, please re-enter"
	firststep= raw_input("would u like to play?")
if firststep=="n":
	sys.exit("bye")
	
numberofplayers=0
# Total Points for all hunters
stotal=0
# adds the points to the list
maximumP=[]
maximumPlayer=[]
# adds the "fine" or "trapped" to the list
fineornot=[]
# adds the lucky numbers to the list 
minimumlucky=[]
while firststep=="y":
	trapped=False
	print "One more game... "
	print "================"
	
	numberofplayers= numberofplayers+1
	player=info()
	sizeofbox=boardsize()
	while sizeofbox%1!=0 or sizeofbox>6 or sizeofbox<3:
		
		if sizeofbox%1!=0:
			print "It should be int, Try again"
		elif sizeofbox>6:
			print "It should be 6 or less"
			
		elif sizeofbox<3:
			print "It should be 3 or more"
		sizeofbox=boardsize()


		
		
		
	randomoruser()
		
	
	
	z=usertypes()
	
	while len(z)!=sizeofbox:
		
		print "Not same as the size of board, type again"
		z=usertypes()

		
		
		
	# IF user is not trapped
	ticket=False
	z12=0
	zh=0
	while ticket==False:
		print 
		print "The board is"
		print "------------"
		showboard()
		decision()
		
		zz=0
		
		path = raw_input("x - random        :")
		
		
		if path=="r":
			numberofrows1=rows()
			while int(numberofrows1)>len(z)-1 or int(numberofrows1)<0:
			
				print "That is not a valid input, please re-enter"
				numberofrows1=rows()
			
				
			#Checking for negative	
			if checknegativeR(numberofrows1)==True:
				trapped=True
				choiceRnegative(z,numberofrows1)
				z12=sumpointsnegative(findi(z,numberofrows1))
				print "points obtained in this trip:...", z12
				zh=zh+z12
				print "board after trip"
				showboard()	
				print "Oh no! " +player+" got trapped!"
				print player +" cannot travel again :( "
				print
				
				ticket=True
				#comes out of loop
			else:
				print "positions visited: ..."
				choiceRpositive(numberofrows1)
				z12=sumpoints(numberofrows1,z)
				print "points obtained in this trip:...", z12
				print "board after trip"
				CHANGER()
				showboard()
				zh=zh+z12
				ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				while ask!="y" and ask!="n":
					print "That is not a valid input, please re-enter"
					ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
					
					
				if ask=="y":
					ticket=False
					#plays again
				else:
					ticket=True
					#comes out of loop
					
		
		
				
		
		elif path=="c":
			numberofcols1=cols()
			while int(numberofcols1)>len(z)-1 or int(numberofcols1)<0:
				print "That is not a valid input, please re-enter"
				numberofcols1=cols()
				
			#Checking for negative		
			if checknegativeC(numberofcols1)==True:
				trapped=True
				choiceCnegative(z,numberofcols1)
				z12= sumCnegative(findiC(z, numberofcols1))
				print "points obtained in this trip:...", z12
				zh=zh+z12
				print "board after trip"
				showboard()
				print "Oh no! " +player+" got trapped!"
				print player +" cannot travel again :( "
				print 
				
				ticket=True
				#comes out of loop
				
			
		
			else:
				print "positions visited: ..."
				choiceCPositive(numberofcols1)
				z12= sumCnonegative(z,numberofcols1)
				print "points obtained in this trip:...", z12
				print "board after trip"
				showboard()
				zh=zh+z12
				ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				while ask!="y" and ask!="n":
					print "That is not a valid input, please re-enter"
					ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				if ask=="y":
					ticket=False
					#plays again
				else:
					ticket=True
					#comes out of loop
					
			
			
				
				
		elif path=="m":
			#Checking for negative
			if checknegativeM()==True:
				trapped=True
				Mnegativefound()
				z12 = sumMnegative(findiM())
				print "points obtained in this trip:...", z12
				zh=zh+z12
				print "board after trip"
				showboard()
				print "Oh no! " +player+" got trapped!"
				print player +" cannot travel again :( "
				print 
				ticket=True
				#comes out of loop
				
			
			else:
				
				Mnonegative()
				z12= Msum()
				print "points obtained in this trip:...",z12
				changem()
				print "board after trip"
				showboard()
				zh=zh+z12
				ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				while ask!="y" and ask!="n":
					print "That is not a valid input, please re-enter"
					ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				if ask=="y":
					ticket=False
					#plays again
				else:
					ticket=True
					#comes out of loop
					
		
					
					
		elif path=="s":
			#Checking for negative
			if Schecknegative()==True:
				trapped=True
				Snegativefound()
				z12 = sumwithnegative()
				print "points obtained in this trip:...", z12
				zh=zh+z12
				print "board after trip"
				showboard()
				print "Oh no! " +player+" got trapped!"
				print player +" cannot travel again :( "
				print 
				ticket=True
				#comes out of loop
				
				
				
			
			else:
			
				print "positions visited: ..."
				Spositionsdisplay()
				z12 = SsumNONegative()
				print "points obtained in this trip:...", SsumNONegative()
				Schange()
				print "board after trip"
				showboard()
				zh=zh+z12
				ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				while ask!="y" and ask!="n":
					print "That is not a valid input, please re-enter"
					ask= raw_input("Would  you like "+ player+ " to do another trip? (y/n)")
				if ask=="y":
					ticket=False
					#plays again
				else:
					ticket=True
					#comes out of loop
					
		
		
	
	
	
	print 
	print "The treasure hunter "+ player +" obtained "+ str(zh)+ " points in its game"

	changetobinary()
	print
	print "The values of each row in the board (as binary number) are:"
	valueofbinary(), 
	print " and therefore the board lucky number is: ", luckynumber() 
	# adding all the points
	stotal= stotal+zh
	
	# adding points, luckynumbers, players names and the status of players to their list 
	maximumP.append(zh)
	maximumPlayer.append(player)
	fineornot.append(trapped)
	minimumlucky.append(luckynumber())
	
	print 				
	firststep= raw_input("would u like to play another round?")
	while firststep!="y" and firststep!="n":
		print "That is not a valid input, please re-enter"
		firststep= raw_input("would u like to play another round?")
		
#Out of lopp		

# gets the position of maximum points for referal
maximuminlist= max(maximumP)
x=0
for h in range(len(maximumP)):
	if maximumP[h]==maximuminlist:
		x=h
		
		
# gets the position of minimum lucknumber for referal
getminimumlucky=min(minimumlucky)
d=0
for f in range(len(minimumlucky)):
	if minimumlucky[f]==getminimumlucky:
		d=f

# If false== fine else: they are trappd
for i in range(len(fineornot)):
	if fineornot[i]==False:
		fineornot[i]="fine"
	else:
		fineornot[i]="trapped"


# Final Step
print 			
print "Total hunters that player:", numberofplayers
print "Total points of all hunters: ", stotal
print 
print "Maximum hunter points:"
print "The hunter", maximumPlayer[x], "who is", fineornot[x]
print "got the maximum points: ", maximuminlist

print 

print "Minimum lucky number:"
print "The board with the hunter ", maximumPlayer[d], "who is", fineornot[d]
print "got the minimum lucky number: ", getminimumlucky

print 

print "Bye Bye"
			
			
			
	
			

	
	


