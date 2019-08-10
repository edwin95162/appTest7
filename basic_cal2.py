#This is my first Phyton program
#Developer Edwin Garcìa B.

#Libraries#####################################
import os


###############################################

#Functions#####################################
def calc(x,y):
    suma = x+y
    print("La suma es: ", suma)

#Main#####################################
os.system("clear")
#Pedir variable, siempre se pide como character por 
# lo que es necesario convertir a entero con int antes del input#######
print ("Press number 1: ")
a= int(input())
#forma 2 de pedir una variable 
b= int(input ("Press number 2: \n"))
calc(a,b)