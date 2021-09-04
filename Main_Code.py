
Y = int(input("Enter The Number Of Blocks Outside The Table: "))


def Ans(X):

	N=2*X   #Just for convineance    
	i=1  
	B=0  #Number of Blocks
	C=0  #Center of Mass
	while C<N  :  
		C+=(1/i)
		i+=1
		B+=1 
	return B

print(f"Answer is {Ans(Y)}")  
