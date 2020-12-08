from Array2D import Array2D
from stack import Stack
class LaberintoADT:
    """
    0 pasillo , 1 pared, S salida y E entrada
    pasillo es una tupla ((2,1),(2,2),(2,3),(2,4),(3,2)(4,2))
    Entrada en una tupla(5,1)
    salida(2,5)
    """
    def __init__( self , rens , cols , pasillos , entrada , salida ):
        self.__laberinto = Array2D( rens , cols , '1' )
        for pasillo in pasillos:
            self.__laberinto.set_item( pasillo[0] , pasillo[1] ,'0')
        self.set_entrada( entrada[0],entrada[1])
        self.set_salida( salida[0],salida[1])
        self.__camino = Stack()
        self.__previa = None

    def to_string( self ):
        self.__laberinto.to_string()

    #Establece entrada 'E' en la matriz, verificar limites perifericos
    def set_entrada( self , ren , col ):
        #terminar la validacion de las coordenadas
        self.__laberinto.set_item(ren,col,'E')

    #Establece salida 'S', dentro de los limites periericos de la matriz
    def set_salida( self , ren , col ):
        #Terminar las validaciones
        self.__laberinto.set_item(ren,col,'S')

    def es_salida(self,ren,col):
        return self.__laberinto.get_item(ren,col)=='S'

    def buscar_entrada(self):
        encontradp = False
        for renglon in range( self.__laberinto.get_num_rows() ):
            for columna in range( self.__laberinto.get_num_cols() ):
                if self.__laberinto.get_item(renglon,columna) == 'E':
                    self.__camino.push( (renglon,columna) )
                    encontrado = True
        return encontrado

    def set_previa(self,pos_previa):
        self.__previa = pos_previa

    def get_previa(self):
        return self.__previa

    def imprimir_camino( self ):
        self.__camino.to_string()

    def get_pos_actual( self ):
        return self.__camino.peek()

    def resolver_laberinto( self ):
        actual = self.__camino.peek() #(5,2)

        # buscar izquierda                                     \ la diagonalpermite continuar el codigo abajo
        # agregar validaciones para los limites del laberinto
        if actual[1]-1 != -1 \
        and self.__laberinto.get_item(actual[0],actual[1]-1) == '0' \
        and self.get_previa() != (actual[0],actual[1]-1) \
        and self.__laberinto.get_item(actual[0],actual[1]-1) != 'X':
           self.set_previa( actual )
           self.__camino.push((actual[0],actual[1]-1))

        if actual[0]-1 != -1 \
        and self.__laberinto.get_item(actual[0]-1,actual[1]) == '0' \
        and self.get_previa() != (actual[0]-1,actual[1]) \
        and self.__laberinto.get_item(actual[0]-1,actual[1]) != 'X':
           self.set_previa( actual )
           self.__camino.push((actual[0]-1,actual[1]))
