import sys, os
import tkinter as tk

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
    def delete(self, idin):
        actual = self.primero
        if actual.articulo.ID == idin:
            self.primero = actual.siguiente
            return
        while actual.siguiente != None:
            if actual.siguiente.articulo.ID == idin:
                actual.siguiente = actual.siguiente.siguiente
                return
            actual = actual.siguiente
    def exportar(self):
        #Crea una variable llamada f donde se crea un archivo en la carpeta Inventario con el nombre de aa.dot
        try:
            with open('c:/aa.dot', 'w+',encoding='utf-8') as f:
                f.write('digraph G {\n fontname="Helvetica,Arial,sans-serif" \n node [fontname="Helvetica,Arial,sans-serif"] \n edge [fontname="Helvetica,Arial,sans-serif"] \n')
                f.write('a0 [shape=none label=< ')
                f.write('<TABLE border="1"> \n <TR>')
                f.write('<TD> ID </TD> \n <TD> Nombre </TD>\n <TD> Descripcion </TD>\n <TD> Precio </TD>\n <TD> Cantidad </TD>\n <TD> Proveedor </TD> \n </TR>\n')
                actual = self.primero
                while actual != None:
                    f.write('<TR> \n <TD>'+str(actual.articulo.ID)+'</TD> \n <TD>'+
                            actual.articulo.nombre+'</TD> \n <TD>'+
                            actual.articulo.descripcion+'</TD> \n <TD>'+
                            str(actual.articulo.precio)+'</TD> \n <TD>'+
                            str(actual.articulo.cantidad)+'</TD> \n <TD>'+
                            actual.articulo.proveedor+'</TD> \n </TR>\n'
                            )
                    actual = actual.siguiente
                    f.write('\n')
                f.write('</TABLE>>];\n}')
            os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
            os.system('dot -Tpng c:/aa.dot -o c:/aa.png')
            os.system('c:/aa.png')
            tk.messagebox.showinfo(title="Éxito", message="Inventario exportado exitosamente.")
        except Exception as e:
            print(e)
            return
            

