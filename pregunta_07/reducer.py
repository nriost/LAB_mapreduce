import sys 
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import itertools 
##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':
    
 lista=[]  
 for line in sys.stdin:
    clave, fecha, valor = line.split("\t") 
    valor=int(valor) 
    lista.append([clave, fecha, valor]) 

 lista = sorted(lista, key=lambda x: (x[0], x[2])) 
 for line in lista: 
    sys.stdout.write("{}   {}   {}\n".format(line[0], line[1], line[2])) 
