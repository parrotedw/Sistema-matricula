import tkinter as tk
import csv
import tkinter.messagebox as messagebox

root = tk.Tk()  # Crear una instancia de la clase Tk
root.geometry("900x600")
root.title("Sistema de Matrículas Escolares")

# Etiqueta
label = tk.Label(root, text="Institución Educativa Pública General Emilio Soyer Cabero", font=("Helvetica", 20, "bold"))
label.pack(pady=30)

# Contenedor de secciones
secciones_matricula = tk.Frame(root)
secciones_matricula.pack()

# Función para mostrar la sección de matrícula
def matricula():
    # Crear una nueva ventana secundaria para la sección de matrícula
    ventana_matricula = tk.Toplevel()
    ventana_matricula.geometry("900x600")
    ventana_matricula.title("Sección de Matrícula")
    
    # Variables de tipo StringVar para obtener los datos de los Entries
    nombre_var = tk.StringVar()
    dni_var = tk.StringVar()
    fecha_nacimiento_var = tk.StringVar()
    nombre_padre_var = tk.StringVar()
    direccion_var = tk.StringVar()
    telefono_padre_var = tk.StringVar()
    
    # Contenido de la sección de matrícula
    label = tk.Label(ventana_matricula, text="Estás en la sección de matrículas")
    label.pack()
    
    #nombre
    label = tk.Label(ventana_matricula, text="Nombre del alumno")
    label.pack()
    entry_nombre = tk.Entry(ventana_matricula, width=40, textvariable=nombre_var)
    entry_nombre.pack()
    
    #dni
    label = tk.Label(ventana_matricula, text="DNI del alumno")
    label.pack()
    entry_dni = tk.Entry(ventana_matricula, width=40, textvariable=dni_var)
    entry_dni.pack()
    
    #fecha de nacimiento
    label = tk.Label(ventana_matricula, text="Fecha de nacimiento del alumno")
    label.pack()
    entry_fecha_nacimiento = tk.Entry(ventana_matricula, width=40, textvariable=fecha_nacimiento_var)
    entry_fecha_nacimiento.pack()
    
    #nombre del padre
    label = tk.Label(ventana_matricula, text="Nombre del padre o apoderado")
    label.pack()
    entry_nombre_padre = tk.Entry(ventana_matricula, width=40, textvariable=nombre_padre_var)
    entry_nombre_padre.pack()
    
    #direccion
    label = tk.Label(ventana_matricula, text="Dirección")
    label.pack()
    entry_direccion = tk.Entry(ventana_matricula, width=40, textvariable=direccion_var)
    entry_direccion.pack()
    
    #telefono
    label = tk.Label(ventana_matricula, text="Teléfono del apoderado")
    label.pack()
    entry_telefono_padre = tk.Entry(ventana_matricula, width=40, textvariable=telefono_padre_var)
    entry_telefono_padre.pack()
    
    # Botón para registrar alumno
    button_registrar = tk.Button(ventana_matricula, text="Registrar alumno", command=lambda: accion_matricula(nombre_var, dni_var, fecha_nacimiento_var, nombre_padre_var, direccion_var, telefono_padre_var))
    button_registrar.pack()

    
def accion_matricula(nombre, dni, fecha_nacimiento, nombre_padre, direccion, telefono_padre):
    nombre = nombre.get()
    dni = dni.get()
    fecha_nacimiento = fecha_nacimiento.get()
    nombre_padre = nombre_padre.get()
    direccion = direccion.get()
    telefono_padre = telefono_padre.get()
    
    datos=[nombre, dni, fecha_nacimiento, nombre_padre, direccion, telefono_padre]
    archivo = "base_matricula.csv"
    with open(archivo, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(datos)
    messagebox.showinfo("Matriculación Exitosa", "El alumno se ha matriculado correctamente.")
    
    
    
    

# Contenedor para los botones
seccion_botones = tk.Frame(root)
seccion_botones.pack()

# Botones
button1 = tk.Button(seccion_botones, text="Matricular alumno", command=matricula)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(seccion_botones, text="Base de alumnos registrados")
button2.pack(side=tk.LEFT, padx=10)

button3 = tk.Button(seccion_botones, text="Buscar alumnos")
button3.pack(side=tk.LEFT, padx=10)

button4 = tk.Button(seccion_botones, text="Eliminar alumnos")
button4.pack(side=tk.LEFT, padx=10)

root.mainloop()
