import tkinter as tk
from tkinter import *
import json
from tkinter.filedialog import askopenfilename
from Estructuras.LinkedLIst import lista
inv = lista()
i=0
class Ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana
        self.title("Tecnoclinic")
        self.geometry("800x600")
        self.resizable(False, False)
        # Creación de widgets
        self.tabla = tk.Frame(self)
        self.tabla.pack()
        # Encabezado de la tabla
        self.encabezado = tk.LabelFrame(self.tabla, text="Lista de Productos")
        self.encabezado.pack()
        # Columnas de la tabla
        self.columnas = tk.Frame(self.encabezado)
        self.columnas.pack()
        self.etiqueta_id = tk.Label(self.columnas, text="ID", width=5)
        self.etiqueta_id.pack(side=tk.LEFT, padx=5)
        self.etiqueta_nombre = tk.Label(self.columnas, text="Nombre",width=30)
        self.etiqueta_nombre.pack(side=tk.LEFT, padx=5)
        self.etiqueta_cantidad = tk.Label(self.columnas, text="Cantidad", width=10)
        self.etiqueta_cantidad.pack(side=tk.LEFT, padx=5)
        self.etiqueta_proveedor = tk.Label(self.columnas, text="Proveedor", width=20)
        self.etiqueta_proveedor.pack(side=tk.LEFT, padx=5)
        self.etiqueta_precio = tk.Label(self.columnas, text="Precio" , width=10)
        self.etiqueta_precio.pack(side=tk.LEFT, padx=5)
        # Filas de la tabla
        self.filas = tk.Frame(self.tabla)
        self.filas.pack()
        # Botones
        self.botones = tk.Frame(self)
        self.botones.pack()
        self.boton_nuevo = tk.Button(self.botones, text="Importar", command=self.importar)
        self.boton_nuevo.pack(side=tk.LEFT, padx=5)
        self.boton_editar = tk.Button(self.botones, text="Editar", command=self.edit)
        self.boton_editar.pack(side=tk.LEFT, padx=5)
        self.boton_eliminar = tk.Button(self.botones, text="Eliminar", command=self.eliminar)
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)
        self.boton_insertar = tk.Button(self.botones, text="Insertar", command=self.insertar)
        self.boton_insertar.pack(side=tk.LEFT, padx=5)
        self.boton_exportar = tk.Button(self.botones, text="Exportar", command=self.exportar)
        self.boton_exportar.pack(side=tk.LEFT, padx=5)
        
    def importar(self):
        global i
        print("Cargando archivo")
        #? Se Carga el Archivo
        route = askopenfilename(filetypes=[("Archivo JSON", "*.json")])
        if not route:
            #? Mensaje de Error si no se carga el archivo
            tk.messagebox.showerror(title="Error", message="No se hay archivo seleccionado aun")
            return
        try:
            
            with open(route, "r") as archivo:
                datos = json.load(archivo)
                for productos in datos:
                    nombre = productos["nombre"]
                    nombre = nombre.encode('latin1').decode('utf-8')
                    cantidad = productos["cantidad"]
                    precio = productos["precio"]
                    proveedor = productos["proveedor"]
                    descripcion = productos["descripcion"]
                    # agregar estos datos al pack de productos
                    fila = tk.Frame(self.filas)
                    fila.pack(fill=tk.X)
                    etiqueta_id = tk.Label(fila, text=i, width=5)
                    etiqueta_id.pack(side=tk.LEFT, padx=5)
                    etiqueta_nombre = tk.Label(fila, text=nombre, width=30)
                    etiqueta_nombre.pack(side=tk.LEFT, padx=5)
                    etiqueta_cantidad = tk.Label(fila, text=cantidad, width=10)
                    etiqueta_cantidad.pack(side=tk.LEFT, padx=5)
                    etiqueta_proveedor = tk.Label(fila, text=proveedor, width=20)
                    etiqueta_proveedor.pack(side=tk.LEFT, padx=5)
                    etiqueta_precio = tk.Label(fila, text=precio, width=10)
                    etiqueta_precio.pack(side=tk.LEFT, padx=5)
                    inv.add(nombre, descripcion, precio, cantidad, proveedor)
                    i+=1
        except Exception as e:
            tk.messagebox.showerror(title="Error", message="Error al leer el archivo JSON: " + str(e))
            return
        # Mostrar mensaje de éxito
        tk.messagebox.showinfo(title="Éxito", message="Archivo cargado exitosamente.")
        inv.show()
    def edit(self):
        if inv.isEmpty():
            tk.messagebox.showerror(title="Error", message="No hay productos en el inventario")
            return
        # Abrir una ventana emergente para solicitar el ID
        ventana_id = tk.Toplevel(self)
        ventana_id.geometry("200x150")
        ventana_id.title("Editar producto")
        # Crear un marco para la ventana emergente
        marco_id = tk.Frame(ventana_id)
        marco_id.pack()
        # Etiqueta para el ID
        etiqueta_id = tk.Label(marco_id, text="ID del producto:")
        etiqueta_id.pack()
        # Entrada para el ID
        entrada_id = tk.Entry(marco_id)
        entrada_id.pack()
        # Botón para confirmar el ID
        boton_confirmar = tk.Button(marco_id, text="Confirmar", command=lambda: self.confirmar_id(ventana_id, entrada_id.get(),boton_confirmar))
        boton_confirmar.pack()
        # Función para confirmar el ID y cerrar la ventana emergente
        #Redimensiona la venana a 600x400 
    def confirmar_id(self, ventana_id, id_producto, boton_confirmar):
        # Buscar el producto con el ID especificado
        producto = inv.getProdcuto(int(id_producto))
        #Pasar el String a int del ID
        # Si el producto no se encuentra, mostrar un mensaje de error
        if not producto:
            tk.messagebox.showerror(title="Error", message="No se encontró un producto con el ID " + id_producto)
            return
        boton_confirmar.config(state="disabled")
        # Cerrar la ventana emergente
        #redimensiona la ventana a 600x400 y la coloca en el centro  de la pantalla
        ventana_id.geometry("600x400")
        ventana_id.update_idletasks()  # Asegura que las actualizaciones de diseño se realicen antes de centrar
        # Centrar la ventana en la pantalla
        ancho_ventana = ventana_id.winfo_width()
        altura_ventana = ventana_id.winfo_height()
        pantalla_ancho = ventana_id.winfo_screenwidth()
        pantalla_altura = ventana_id.winfo_screenheight()
        x_pos = (pantalla_ancho / 2) - (ancho_ventana / 2)
        y_pos = (pantalla_altura / 2) - (altura_ventana / 2)
        ventana_id.geometry("+%d+%d" % (x_pos, y_pos))
        # Crear un marco para la ventana emergente y en ellos la informacion del producto de manera horizontal
        marco_datos = tk.Frame(ventana_id)
        marco_datos.pack(pady=20)
        # Matriz de datos
        datos = [("Nombre:", producto.nombre),
                ("Cantidad:", producto.cantidad),
                ("Proveedor:", producto.proveedor),
                ("Precio:", producto.precio)]
        # Crear marcos secundarios y organizarlos en una disposición de cuadrícula 3x2
        for i, (label_text, value) in enumerate(datos):
            fila = i // 2
            columna = i % 2
            marco_info = tk.Frame(marco_datos)
            marco_info.grid(row=fila, column=columna, padx=10, pady=5)
            etiqueta_nombre = tk.Label(marco_info, text=label_text)
            etiqueta_nombre.pack(side=tk.LEFT)
            etiqueta_valor = tk.Label(marco_info, text=value)
            etiqueta_valor.pack(side=tk.LEFT)
        # Botón para guardar los cambios
        boton_editar = tk.Button(marco_datos, text="Editar", command=lambda: self.editar_producto(int(id_producto), ventana_id))
        boton_editar.grid(row=2, column=0, columnspan=2)
    def editar_producto(self,idIn,window):
        print("Editar producto")
        # Abrir una ventana emergente para editar los datos del producto
        ventana_editar = tk.Toplevel(self)
        ventana_editar.geometry("600x400")
        ventana_editar.title("Editar producto")
        # Crear un marco para la ventana emergente
        marco_editar = tk.Frame(ventana_editar)
        marco_editar.pack()
        # Etiqueta para el nombre
        etiqueta_nombre = tk.Label(marco_editar, text="Nombre:")
        etiqueta_nombre.pack()
        # Entrada para el nombre
        entrada_nombre = tk.Entry(marco_editar)
        entrada_nombre.insert(0, inv.getProdcuto(idIn).nombre)
        entrada_nombre.pack()
        # Etiqueta para la cantidad
        etiqueta_cantidad = tk.Label(marco_editar, text="Cantidad:")
        etiqueta_cantidad.pack()
        # Entrada para la cantidad
        entrada_cantidad = tk.Entry(marco_editar)
        entrada_cantidad.insert(0, inv.getProdcuto(idIn).cantidad)
        entrada_cantidad.pack()
        # Etiqueta para el proveedor
        etiqueta_proveedor = tk.Label(marco_editar, text="Proveedor:")
        etiqueta_proveedor.pack()
        # Entrada para el proveedor
        entrada_proveedor = tk.Entry(marco_editar)
        entrada_proveedor.insert(0, inv.getProdcuto(idIn).proveedor)
        entrada_proveedor.pack()
        # Etiqueta para el precio
        etiqueta_precio = tk.Label(marco_editar, text="Precio:")
        etiqueta_precio.pack()
        # Entrada para el precio
        entrada_precio = tk.Entry(marco_editar)
        entrada_precio.insert(0, inv.getProdcuto(idIn).precio)
        entrada_precio.pack()
        # Botón para guardar los cambios
        boton_guardar = tk.Button(marco_editar, text="Guardar", command= lambda: self.guardarCambios(idIn, entrada_nombre.get(), int(entrada_precio.get()), int(entrada_cantidad.get()), entrada_proveedor.get(),window))
        boton_guardar.pack()
    def guardarCambios(self, idIn, nombre, precio, cantidad, proveedor,ventana):
        inv.edit(idIn, nombre, precio, cantidad, proveedor)
        # Mostrar mensaje de éxito
        tk.messagebox.showinfo(title="Éxito", message="Producto editado exitosamente.")
        # Cerrar la ventana emergente
        # Actualizar la tabla
        self.actualizar_tabla()
        ventana.destroy()
    def actualizar_tabla(self):
        # Eliminar todas las filas de la tabla
        for widget in self.filas.winfo_children():
            widget.destroy()
        # Agregar las filas actualizadas
        actual = inv.primero
        while actual != None:
            fila = tk.Frame(self.filas)
            fila.pack(fill=tk.X)
            etiqueta_id = tk.Label(fila, text=actual.articulo.ID, width=5)
            etiqueta_id.pack(side=tk.LEFT, padx=5)
            etiqueta_nombre = tk.Label(fila, text=actual.articulo.nombre, width=30)
            etiqueta_nombre.pack(side=tk.LEFT, padx=5)
            etiqueta_cantidad = tk.Label(fila, text=actual.articulo.cantidad, width=10)
            etiqueta_cantidad.pack(side=tk.LEFT, padx=5)
            etiqueta_proveedor = tk.Label(fila, text=actual.articulo.proveedor, width=20)
            etiqueta_proveedor.pack(side=tk.LEFT, padx=5)
            etiqueta_precio = tk.Label(fila, text=actual.articulo.precio, width=10)
            etiqueta_precio.pack(side=tk.LEFT, padx=5)
            actual = actual.siguiente
    def insertar(self):
        #Crea una ventana de 600x400 en el centro de la pantalla
        ventana_insertar = tk.Toplevel(self)
        ventana_insertar.geometry("600x400")
        ventana_insertar.title("Insertar producto")
        ventana_insertar.update_idletasks()
        ancho_ventana = ventana_insertar.winfo_width()
        altura_ventana = ventana_insertar.winfo_height()
        pantalla_ancho = ventana_insertar.winfo_screenwidth()
        pantalla_altura = ventana_insertar.winfo_screenheight()
        x_pos = (pantalla_ancho / 2) - (ancho_ventana / 2)
        y_pos = (pantalla_altura / 2) - (altura_ventana / 2)
        ventana_insertar.geometry("+%d+%d" % (x_pos, y_pos))
        # Crear un marco para la ventana emergente
        marco_insertar = tk.Frame(ventana_insertar)
        marco_insertar.pack()
        # Etiqueta para el nombre
        etiqueta_nombre = tk.Label(marco_insertar, text="Nombre:")
        etiqueta_nombre.pack()
        # Entrada para el nombre
        entrada_nombre = tk.Entry(marco_insertar)
        entrada_nombre.pack()
        # Etiqueta para la cantidad
        etiqueta_cantidad = tk.Label(marco_insertar, text="Cantidad:")
        etiqueta_cantidad.pack()
        # Entrada para la cantidad
        entrada_cantidad = tk.Entry(marco_insertar)
        entrada_cantidad.pack()
        # Etiqueta para el proveedor
        etiqueta_proveedor = tk.Label(marco_insertar, text="Proveedor:")
        etiqueta_proveedor.pack()
        # Entrada para el proveedor
        entrada_proveedor = tk.Entry(marco_insertar)
        entrada_proveedor.pack()
        # Etiqueta para el precio
        etiqueta_precio = tk.Label(marco_insertar, text="Precio:")
        etiqueta_precio.pack()
        # Entrada para el precio
        entrada_precio = tk.Entry(marco_insertar)
        entrada_precio.pack()
        # Etiqueta para la descripcion
        etiqueta_descripcion = tk.Label(marco_insertar, text="Descripcion:")
        etiqueta_descripcion.pack()
        # Entrada para la descripcion
        entrada_descripcion = tk.Entry(marco_insertar)
        entrada_descripcion.pack()
        # Botón para guardar los cambios
        boton_guardar = tk.Button(marco_insertar, text="Guardar", command=lambda: self.guardarProducto(entrada_nombre.get(), int(entrada_precio.get()), int(entrada_cantidad.get()), entrada_proveedor.get(),entrada_descripcion.get(),ventana_insertar))
        boton_guardar.pack()
    def guardarProducto(self, nombre, precio, cantidad, proveedor, descripcion, ventana):
        inv.add(nombre, descripcion, precio, cantidad, proveedor)
        # Mostrar mensaje de éxito
        tk.messagebox.showinfo(title="Éxito", message="Producto insertado exitosamente.")
        # Cerrar la ventana emergente
        ventana.destroy()
        # Actualizar la tabla
        self.actualizar_tabla()
    def eliminar(self):
        # Abrir una ventana emergente para solicitar el ID
        ventana_eliminar = tk.Toplevel(self)
        ventana_eliminar.geometry("200x150")
        ventana_eliminar.title("Eliminar producto")
        ventana_eliminar.update_idletasks()
        ancho_ventana = ventana_eliminar.winfo_width()
        altura_ventana = ventana_eliminar.winfo_height()
        pantalla_ancho = ventana_eliminar.winfo_screenwidth()
        pantalla_altura = ventana_eliminar.winfo_screenheight()
        x_pos = (pantalla_ancho / 2) - (ancho_ventana / 2)
        y_pos = (pantalla_altura / 2) - (altura_ventana / 2)
        ventana_eliminar.geometry("+%d+%d" % (x_pos, y_pos))
        # Crear un marco para la ventana emergente
        marco_id = tk.Frame(ventana_eliminar)
        marco_id.pack()
        # Etiqueta para el ID
        etiqueta_id = tk.Label(marco_id, text="ID del producto:")
        etiqueta_id.pack()
        # Entrada para el ID
        entrada_id = tk.Entry(marco_id)
        entrada_id.pack()
        # Botón para confirmar el ID
        boton_confirmar = tk.Button(marco_id, text="Confirmar", command=lambda: self.confirmar_eliminar(ventana_eliminar, int(entrada_id.get())))
        boton_confirmar.pack()
    def confirmar_eliminar(self, ventana_eliminar, id_producto):
        # Buscar el producto con el ID especificado
        ventana_eliminar.geometry("600x400")
        ventana_eliminar.update_idletasks()
        producto = inv.getProdcuto(id_producto)
        # Si el producto no se encuentra, mostrar un mensaje de error
        if not producto:
            tk.messagebox.showerror(title="Error", message="No se encontró un producto con el ID " + str(id_producto))
            return
        #crear un marco adicional en la ventana que muestre los datos del producto
        marco_datos = tk.Frame(ventana_eliminar)
        marco_datos.pack(pady=20)
        # Matriz de datos
        datos = [("Nombre:", producto.nombre),
                ("Cantidad:", producto.cantidad),
                ("Proveedor:", producto.proveedor),
                ("Precio:", producto.precio)]
        # Crear marcos secundarios y organizarlos en una disposición de cuadrícula 3x2
        for i, (label_text, value) in enumerate(datos):
            fila = i // 2
            columna = i % 2
            marco_info = tk.Frame(marco_datos)
            marco_info.grid(row=fila, column=columna, padx=10, pady=5)
            etiqueta_nombre = tk.Label(marco_info, text=label_text)
            etiqueta_nombre.pack(side=tk.LEFT)
            etiqueta_valor = tk.Label(marco_info, text=value)
            etiqueta_valor.pack(side=tk.LEFT)
        # Botón para eliminar el producto
        boton_eliminar = tk.Button(marco_datos, text="Eliminar", command=lambda: self.eliminar_producto(id_producto, ventana_eliminar))
        boton_eliminar.grid(row=2, column=0, columnspan=2)
    def eliminar_producto(self, id_producto, ventana_eliminar):
        inv.delete(id_producto)
        # Mostrar mensaje de éxito
        tk.messagebox.showinfo(title="Éxito", message="Producto eliminado exitosamente.")
        # Cerrar la ventana emergente
        ventana_eliminar.destroy()
        # Actualizar la tabla
        self.actualizar_tabla()
    def exportar(self):
        inv.exportar()
        # Mostrar mensaje de éxito
        
ventana = Ventana()
ventana.mainloop()