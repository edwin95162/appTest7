
# Lista
number_array = []

def check_sum(a,b):
    return a+b

while True:
    print("Digite un número")
    incoming = int(input())

    if len(number_array) >=2:
        if check_sum(number_array[-1],number_array[-2]) != incoming:
            number_array.append(incoming)
        
        else:
            print("El número es igual a la suma de los dos ultimos items")

       
        print("Ultimo: " + str(number_array[-1]))
        print('Penult: ' + str(number_array[-2]))
   
    else:
        number_array.append(incoming)

    
    print('Array size: ' + str(len(number_array)))

#Edwin García - Mauricio Pantoja