from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from modelo import *
from cliente import Cliente
from servidor import Servidor
import threading

class VentanaPrincipal():
    def __init__(self,master):
        self.base=BaseDatos()
        master.title("System UTNBA")
        master.configure(bg='#F0F7DA')
        titulo = Label(master, text="System UTNBA", width=80, foreground='#F0F7DA', bg='#1F192F', font='Arial 15 bold').grid(pady=10, row=0, columnspan=6)
        fuentetit = 'Mooli 12'
        fuentecue = 'Roboto-Medium 10'
        patrondni = "^[0-9]+(?i:[ _-][0-9]+)*$"
        # VARIABLES
        var_nombre = StringVar()
        var_apellido = StringVar()
        var_dni = StringVar()
        var_correo = StringVar()
        var_dnic = StringVar()


        # ---------- ALTA DE REGISTRO ---------------------------
        registrasetitulo = Label(master, text="Registrarse", bg='#F0F7DA', font=fuentetit).grid(pady=10,row=1, column=1, columnspan=2)
        nombre = Label(master, text="Nombre", bg='#F0F7DA', font=fuentecue).grid(column=1, row=2)
        nombreentry = Entry(master, textvariable=var_nombre).grid(column=2, row=2)

        apellido = Label(master, text="Apellido", bg='#F0F7DA', font=fuentecue).grid(column=1, row=3)
        apellidoentry = Entry(master,textvariable=var_apellido).grid(column=2, row=3)

        dni = Label(master, text="Dni", bg='#F0F7DA', font=fuentecue).grid(column=1, row=4)
        dnientry = Entry(master,textvariable=var_dni).grid(column=2, row=4)

        correo = Label(master, text="Correo", bg='#F0F7DA', font=fuentecue).grid(column=1, row=5)
        correoentry = Entry(master,textvariable=var_correo).grid(column=2, row=5)

        filiacion = Label(master, text="Filiacion",bg='#F0F7DA', font=fuentecue).grid(column=1, row=6, pady=3)
        #filiacionentry = Entry(main,textvariable=var_filiacion).grid(column=1, row=6)

        boton_reg = Button(master, text="Registrar", bg='#65B8A6', command=lambda:self.vista_alta(var_nombre,var_apellido,var_dni,var_correo,combo,self.tree), font=fuentecue).grid(pady=10, row=7, column=1, columnspan=2)

        combo = ttk.Combobox(
            state="readonly",
            values=["Docente", "No Docente", "Alumno", "Monotributista"]
        )
        combo.grid(column=2,row=6)

        # INPUT MODIFICACION/CONSULTA
        consultatitulo = Label(master, text="Consulta", bg='#F0F7DA', font=fuentetit).grid(pady=10, row=1, column=3, columnspan=2)
        dniconsulta = Label(master, text="Ingrese Documento", bg='#F0F7DA', font=fuentecue).grid(column=3, row=2)
        dniconsultaentry = Entry(master, textvariable=var_dnic).grid(column=4, row=2 )
        

        boton_con = Button(master, text="Consultar", bg='#8BE83F', command=lambda:self.vista_consulta(var_dnic), font=fuentecue).grid(column=3, row=4, columnspan=2)
        boton_mod = Button(master, text="Modificar", bg='#66E8CA', command=lambda:self.vista_modificar(var_nombre,var_apellido,var_dni,var_correo,combo,var_dnic,self.tree), font=fuentecue).grid(row=3, column=3)
        boton_eli = Button(master, text="Eliminar", bg='#FF542B', command=lambda:self.vista_baja(var_dnic,self.tree), font=fuentecue).grid(row=3, column=4)

        boton_servidor = Button(master, text="Encender Servidor", bg='#8BE83F', command=lambda:self.levantar_servidor(), font=fuentecue).grid(column=3, row=6, columnspan=1)
        boton_cliente = Button(master, text="Conectar desde cliente", bg='#8BE83F',command=lambda:self.clientemsj(), font=fuentecue).grid(column=4, row=6, columnspan=1)
         # MUESTRA DE BASE
        
        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("2", "3", "4", "5", "6")
        self.tree.column("#1", minwidth=40, anchor="n")  # no tiene encabezado porque ya existe
        self.tree.column("2", minwidth=80, anchor="n")
        self.tree.column("3", minwidth=80, anchor="n")
        self.tree.column("4", minwidth=60, anchor="n")
        self.tree.column("5", minwidth=60, anchor="n")
        self.tree.column("6", minwidth=60, anchor="n")

        # Encabezado de las columnas del Treeview
        self.tree.heading("#1", text="ID", anchor="n")
        self.tree.heading("2", text="Nombre", anchor="n")
        self.tree.heading("3", text="Apellido", anchor="n")
        self.tree.heading("4", text="Dni", anchor="n")
        self.tree.heading("5", text="Correo", anchor="n")
        self.tree.heading("6", text="Filiacion", anchor="n")

        self.tree.grid(row=9, columnspan=6, pady=5)
        self.vista_actualizar()
        
        master.mainloop()
    
    def vista_actualizar(self,):
        self.base.actualizar_treeview(self.tree)
    
    def vista_consulta(self,dnic):
        self.base.funcion_consulta(dnic)
    
    def vista_alta(self,nombre,apellido,dni,correo,filiacion,tree):
        self.base.funcion_alta(nombre,apellido,dni,correo,filiacion,tree)
    
    def vista_baja(self,dnic, tree):
        self.base.funcion_baja(dnic,tree)
    
    def vista_modificar(self, nombre,apellido,dni,correo,filiacion,dnic,tree):
        self.base.funcion_modificar(nombre,apellido,dni,correo,filiacion,dnic,tree)
    
    def levantar_servidor(self):
        servidor = Servidor('192.168.1.47', 8080)
        hilo_servidor = threading.Thread(target=servidor.iniciar)
        hilo_servidor.start()
    
    def clientemsj(self):
        cliente = Cliente('192.168.1.47', 8080)
        mensaje_inicio = "Cliente conectado"
        cliente.enviar_mensaje(mensaje_inicio)

