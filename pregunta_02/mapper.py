import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys 
#! /usr/bin/opython3
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:
       fields=line [0:-1].split(',')
       sys.stdout.write("{}\t{}\n".format(fields[3],fields[4])) #
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
