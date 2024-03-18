import re  
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
from sqlite3 import *
from peewee import *
from decorador import log_operaciones

### Estructura Base de Datos ###
db = SqliteDatabase("Datos.db")
class BaseModel(Model):
    class Meta:
        database = db  
class Datos(BaseModel):
    nombre = CharField()
    apellido = CharField()
    dni = CharField(unique=True)
    correo = CharField()
    filiacion = CharField()
db.connect()
db.create_tables([Datos])
#### Fin Estructura Base de Datos ###
   
class BaseDatos():
    def __init__(self): pass

    @log_operaciones("funcion_alta")
    def funcion_alta(self,nombre,apellido,dni,correo,filiacion,tree):
        patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
        patroncorreo = "^[A-Za-z]+@"
        patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"
        if (re.match(patrondni, dni.get())):
            if (re.match(patroncorreo, correo.get())):
                if (re.match(patron, nombre.get()) and re.match(patron, apellido.get())):
                    #resultadodni = busquedadni(dni)
                    #if (resultadodni ==[]):
                    datos = Datos()
                    datos.nombre = nombre.get()
                    datos.apellido = apellido.get()
                    datos.dni = dni.get()
                    datos.correo = correo.get()
                    datos.filiacion = filiacion.get()
                    datos.save()
                    self.actualizar_treeview(tree) 
                    mensaje = f"Alta realizada con exito, Su nombre y apellido es: {datos.nombre}, {datos.apellido}, con el dni: {datos.dni}. Su correo es: {datos.correo}"
                    #else:
                    #    showwarning("Error", "El dni ingresado ya existe en la base, ingrese otro")
                    return mensaje
                else:
                    showerror("Error", "No es posible guardar")
            else:
                showwarning("Error", "Por favor ingrese un correo electronico correcto")
        else:
            showwarning("Error", "Por favor ingrese un valor numerico en DNI")
        
    @log_operaciones("funcion_baja")
    def funcion_baja(self, dnic,tree):
        patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"
        if (re.match(patrondni, dnic.get())):
            try:
                Datos.select().where(Datos.dni==dnic.get()).get()
                if askyesno("Eliminar persona", "Esta seguro que desea eliminar esta persona"):
                    resultado = Datos.get(Datos.dni==dnic.get())
                    resultado.delete_instance()
                    self.actualizar_treeview(tree) 
                    showinfo("Eliminar", "Usuario eliminado")
                    mensaje = f"La siguiente persona con el dni: {Datos.dni}. Ha sido eliminado/a"
                    return mensaje

                else:
                    showinfo("Salir", "Esta a punto de salir")
            except Exception:
                showerror("Error", "El dni ingresado no existe en la base de datos")
        else:
            showwarning("Error", "Por favor ingrese un valor numerico")

    @log_operaciones("funcion_modificar")  
    def funcion_modificar(self, nombre,apellido,dni,correo,filiacion,dnic,tree):
        patron = "^[A-Za-z]+(?i:[ _-][A-Za-z]+)*$"
        patroncorreo = "^[A-Za-z]+@"
        patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"
        if (re.match(patrondni, dnic.get())):
            if (re.match(patroncorreo, correo.get())):
                if (re.match(patron, nombre.get()) and re.match(patron, apellido.get())):
                    try:
                        Datos.select().where(Datos.dni==dnic.get()).get()
                        if askyesno("Modificar persona", "Esta seguro que desea modificar esta persona"):
                            actualizar=Datos.update(nombre=nombre.get(), apellido=apellido.get(),dni=dnic.get(),correo=correo.get(),filiacion=filiacion.get()).where(Datos.dni==dnic.get())
                            actualizar.execute()
                            self.actualizar_treeview(tree)
                            showinfo("Modificar", "Usuario modificado")
                            mensaje = f"{nombre.get()} {apellido.get()} ha sido modificado"
                            return mensaje
                        else:
                            showinfo("Salir", "Esta a punto de salir")
                    except Exception:
                        showerror("Error", "El dni ingresado no existe en la base de datos")
                else:
                    showerror("Error", "No es posible guardar")
            else:
                showwarning("Error", "Por favor ingrese un correo electronico correcto")
        else:
            showwarning("Error", "Por favor ingrese un valor numerico")
    
    def actualizar_treeview(self, tree):
        # limpieza de tabla
        records = tree.get_children()
        for element in records:
            tree.delete(element)
        # Consiguiendo datos
        for fila in Datos.select():
            tree.insert("", 0, text=fila.id, values=(fila.nombre, fila.apellido,fila.dni,fila.correo,fila.filiacion))
            
    def funcion_consulta(self,dnic):
        patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"
        datos=Datos()
        if (re.match(patrondni, dnic.get())):
            try:
                datos=Datos.select().where(Datos.dni==dnic.get()).get()
                showinfo("Datos", datos.nombre + "--" + datos.apellido + "--" + datos.dni + "--" + datos.correo + "--" + datos.filiacion)
            except Exception:
                showerror("Error", "El dni ingresado no existe en la base de datos")
        else:
            showwarning("Error", "Por favor ingrese un valor valido")

    
