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

    curkey = None
    suma = 0
    conteo = 0
    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key, val, cont = line.split("\t") 
        val = float(val)
        cont = float(cont) 
        if key == curkey:
            ##
            ## No se ha cambiado de clave. Aca se
            ## acumulan los valores para la misma clave.
            ##
            suma += val
            conteo += cont
        else:
            ##
            ## Se cambio de clave. Se reinicia el
            ## acumulador.
            ##
            if curkey is not None:
                ##
                ## una vez se han reducido todos los elementos
                ## con la misma clave se imprime el resultado en
                ## el flujo de salida
                ##
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo)))  

            curkey = key
            suma = val 
            conteo = cont 
            promedio= float(float(val)/float(conteo)) 
            
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, suma, float(suma/conteo))) 
