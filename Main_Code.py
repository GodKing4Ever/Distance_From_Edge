
Distance_From_The_Edge_Of_The_Table=int(input("How far from the table edge do you want the block to be? \nJust enter a number down below (Try to limit to 7): \n"))
Do_You_Want_Each_Step = "No"

#Try to avoid numbers above 7


#For 9, the answer is 272400600. It will take a while to get the answer.
#For 8, the answer is 36865412

#Don't touch any code below here.


under=""
CenterOfMass=Distance_From_The_Edge_Of_The_Table+0.5
blocks=1
i=0

X=2
#print("Instead of starting from the bottom, we start from the top. The first block will be comepletely out. So, if we take a parallel drawn to the edge of the table as 0, the center of mass of a 1 unit long block will be 0.5 units away from it.")

while True:
	if Do_You_Want_Each_Step=="Yes":

	   print("\n")
	   print("No of blocks = " + str(blocks))
	   print("COM = " + str(CenterOfMass))

	BlockCOM=CenterOfMass-0.5
	
	
	NewCOM=(BlockCOM+(CenterOfMass*(i+1)))/(i+2)
	CenterOfMass=NewCOM


	if X==0:
        
	    print("No of blocks = " + str(blocks))
	    print("COM = " + str(CenterOfMass))

	
	
	if CenterOfMass<=0:
		X=X-1
	if X==0:
		break
	blocks+=1
	i+=1


for z in range(len(str(blocks))+6):

	under+= "="
print("\n")
print("                    {N}".format(N=under))
print("We need a minium of || {X} || blocks for the structure to remain stable".format(X=blocks))
print("                    {N}".format(N=under))
for i in range(5):
	print("\n")

