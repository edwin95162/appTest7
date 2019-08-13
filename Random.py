#Libraries ##################################
import os
from random import randint, uniform, random
# Functions #################################
def calc(n, s, i, z):
    x = 1
    while x<=n :
    #this function generate integer numbers
        if z==1:
            AnsInt = randint(s,i)
            print (AnsInt)
            #this function generate float numbers
        else:
            AnsReal = uniform(s,i)
            print (AnsReal        )
        x = x+1
#Main #######################################
os.system ("clear")
n1 = int(input("Type a number for random: "))
l1 = int(input("type number lower: "))
l2 = int (input("type number higher: "))

print (":::MENU:::")    
print ("1//. INT")
print ("2//. REAL")

opt = int(input("Press an option: \n"))
print("    ")
#Answer
#print ("The Answer is", calc (n1,l1,l2,opt))  
calc (n1,l1,l2,opt)  