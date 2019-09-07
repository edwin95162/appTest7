# Ejercicio 4. Algoritmo que reciba por pantalla N números y deje de solicitar números hasta que la SUMA de los ya ingresados sea mayor a 100.


flag_3 = 0
flag_2 = 0


flag_consecutive = 0


num_consecutive = 2


addition = 0

while addition <100:
    print("Por favor ingrese un número:")
    n = int(input())

   
    if n == 3 and flag_3 < 3:
        addition += n
        flag_3 += 1
        flag_consecutive = 0;
        num_consecutive = 3
    
    elif n == 3 and flag_3 == 3:
        print('Ha ingresado 3 veces el número 3')

    
    if n == 2 and flag_2 < 2:
        addition += n
        flag_2 +=1
        flag_consecutive = 0;
        num_consecutive = 3
    elif n == 2 and flag_2 == 2:
        print('Ha ingresado 2 veces el número 2')

    
    if n != 3 and n != 2:
        
        if n == num_consecutive and flag_consecutive <8:
            addition += n
            flag_consecutive += 1 
        
        elif n != num_consecutive:
            addition += n
            flag_consecutive = 1
            num_consecutive = n
        
        else:
            print("Ha ingresado 8 veces el número " + str(n))

    
    print("La suma va en " + str(addition))

#Edwin García - Mauricio Pantoja