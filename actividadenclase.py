class lista:
    def __init__(self,datos=[]):
        self.lista=datos

    def insertar(self,dato):
        self.lista.append(dato)

    def obtener(self):
        ultimo = self.lista.pop() #pop-ultimo
        return ultimo

    def eliminarElemento(self,pos):
        if pos in range(0,len(self.lista)):
            elemento = self.lista[pos]
            self.lista = self.lista[0:pos] + self.lista[pos+1:]
            return elemento
        else:
            return None
            #return "Posicion:{} no existe en la lista".format(pos)    
    
    def insertarElemento(slef,pos,dato):
        pass
    

    def mostrar(self):
        pass
    


numeros = lista() #instanciando la clase
numeros.insertar("Ana")
numeros.insertar("Daniel")
numeros.insertar("Jose")
numeros.insertar("Miguel")
numeros.insertar("Moises")
#print(numeros.obtener())
print(numeros.lista)
resp = numeros.eliminarElemento(4)
print(resp if resp else "Posicion:{} no válida".format(4))
#print(resp)
print(numeros.lista)