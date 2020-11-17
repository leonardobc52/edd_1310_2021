class Array:
    def __init_(selfd, tam ):
        self.__info =[ 0 for x in range (tam)]

    def get_item( self , posicion):
        dato = 0
        try:
            dato = self.__info[posicion]
        except Exception as e:
            print("Error de posicon")
        return dato

    def set_item(self , dato , posicion):
        try:
            sefl.__info[posicion]
        except Exception as e:
            print("Error de posicion")

    def get_length( self ):
        return len( self.__info)

    def clear( self , dato ):
        self.__info = [dato for x in range(len(self.__info))]

    def __iter__( self ):
        return_IteradorArreglo( self-__info )

class _IteradorArreglo:
    def __init__( sel , arr ):
        self.__arr = arr
        self.__indice = 0

    def __iter__( self ):
        return self

    def __next__( self):
        if self.__indice < len(self.__arr):
            dato = self.__arr[self.__indice]
            self.__indice += 1
            return dato
        else:
            raise StopIteration
