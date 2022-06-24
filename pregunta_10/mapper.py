import sys 
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
from operator import itemgetter
import sys 
if __name__ == "__main__":

    lista=[]
    for line in sys.stdin:
            line= line.replace('\n','')
            clave = line.split('\t')[0]
            valor= line.split('\t')[1]
            
            for letra in valor.split(','):
                lista.append((clave,letra))
    for elemento in lista:
        sys.stdout.write("{}\t{}\n".format(elemento[1].strip(),elemento[0].strip())) 
