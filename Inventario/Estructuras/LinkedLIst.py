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
        self.verify()
        actual = self.primero
        while actual != None:
            if actual.articulo.ID == ID:
                if actual.articulo.cantidad < cantidad:
                    print("No hay suficiente cantidad de", actual.articulo.nombre, "en el inventario")
                    return
                actual.articulo.cantidad -= cantidad
                return
            actual = actual.siguiente
    def show(self):
        self.verify()
        actual = self.primero
        while actual != None:
            print(f"ID: {actual.articulo.ID}, Nombre: {actual.articulo.nombre}, Cantidad: {actual.articulo.cantidad}")
            actual = actual.siguiente
    def verify(self):
        ids=[]
        actual = self.primero
        while actual != None:
            if actual.articulo.cantidad <= 25:
                print(f"El producto {actual.articulo.nombre} tiene una cantidad baja")
                ids.append(actual.articulo.ID)
            actual = actual.siguiente
        #generar ortden de compra
        return ids
    def getProdcuto(self, idIN):
        actual = self.primero
        while actual != None:
            if actual.articulo.ID == idIN:
                return actual.articulo
            actual = actual.siguiente
        return None
    def getCantidad(self, idin):
        actual = self.primero
        while actual != None:
            if actual.articulo.ID == idin:
                return actual.articulo.cantidad
            actual = actual.siguiente
        return None
    def isEmpty(self):
        return self.primero == None
    def edit(self, idin, nombre, precio, cantidad, proveedor):
        actual = self.primero
        while actual != None:
            if actual.articulo.ID == idin:
                actual.articulo.nombre = nombre
                actual.articulo.precio = precio
                actual.articulo.cantidad = cantidad
                actual.articulo.proveedor = proveedor
                return
            actual = actual.siguiente
    