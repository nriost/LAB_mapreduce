#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
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
       fields=line [0:-1].split(',')
       sys.stdout.write("{}\t1\n".format(fields[2]))     
