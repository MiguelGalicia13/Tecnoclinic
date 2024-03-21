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
        self.etiqueta_nombre = tk.Label(self.columnas, text="Nombre",width=15)
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
        self.boton_editar = tk.Button(self.botones, text="Editar")
        self.boton_editar.pack(side=tk.LEFT, padx=5)
        self.boton_eliminar = tk.Button(self.botones, text="Eliminar")
        self.boton_eliminar.pack(side=tk.LEFT, padx=5)
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
                    cantidad = productos["cantidad"]
                    precio = productos["precio"]
                    proveedor = productos["proveedor"]
                    descripcion = productos["descripcion"]
                    # agregar estos datos al pack de productos
                    fila = tk.Frame(self.filas)
                    fila.pack(fill=tk.X)
                    etiqueta_id = tk.Label(fila, text=i, width=5)
                    etiqueta_id.pack(side=tk.LEFT, padx=5)
                    etiqueta_nombre = tk.Label(fila, text=nombre, width=15)
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


ventana = Ventana()
ventana.mainloop()