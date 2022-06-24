import sys 
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys
import itertools 
##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':
    
 for line in sys.stdin:
       letra=line.split('   ')[0] 
       numero = int(line.split('   ')[2]) 
       sys.stdout.write("{}\t{}\t1\n".format(letra,numero))  
