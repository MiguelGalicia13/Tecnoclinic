class articulo:
    def __init__(self, ID, nombre, descrpcion, precio, cantidad, proveedor):
        self.ID = ID
        self.nombre = nombre
        self.descripcion = descrpcion
        self.precio = precio
        self.cantidad = cantidad
        self.proveedor = proveedor

class nodo:
    def __init__(self, articulo):
        self.articulo = articulo
        self.siguiente = None

class lista:
    def __init__(self):
        self.primero = None
    def add(self, nombre, descrpcion, precio, cantidad, proveedor):
        i=0
        if self.primero == None:
            art = articulo(0, nombre, descrpcion, precio, cantidad, proveedor)
            self.primero = nodo(art)
        else:
            actual = self.primero
            while actual.siguiente!= None:
                actual = actual.siguiente
                i+=1
            art = articulo(i+1, nombre, descrpcion, precio, cantidad, proveedor)
            actual.siguiente = nodo(art)
    def sell(self, ID, cantidad):
        actual = self.primero
        while actual != None:
            if actual.articulo.ID == ID:
                actual.articulo.cantidad -= cantidad
                return
            actual = actual.siguiente
    def show(self):
        actual = self.primero
        while actual != None:
            print(f"ID: {actual.articulo.ID}, Nombre: {actual.articulo.nombre}, Cantidad: {actual.articulo.cantidad}")
            actual = actual.siguiente


