import sys
#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

#! /usr/bin/python3

import sys
import itertools 
##
## Esta funcion reduce los elementos que
## tienen la misma clave
##

if __name__ == '__main__':

  for line in sys.stdin:
        num, key, val = line.split(",")
        val=int(val)

        sys.stdout.write("{},{}\n".format(key, val))
