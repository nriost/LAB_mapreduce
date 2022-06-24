import sys 
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
#! /usr/bin/python3
import sys 
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
 for line in sys.stdin:
            numero = line.split('   ')[1]
            #print(numero)
            for elemento in numero:
               mes= line.split('-')[1]
            #print(mes)
             
            sys.stdout.write("{}\t1\n".format(mes))
