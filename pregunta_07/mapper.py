import sys 
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#

import sys 
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
 for line in sys.stdin:
           letra = line.split('   ')[0]
           fecha = line.split('   ')[1]
           numero = int(line.split('   ')[2]) 
           sys.stdout.write("{}\t{}\t{}\n".format(letra,fecha,numero)) 
        
        

  
