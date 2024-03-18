from tkinter import Tk
import vista
from servidor import Servidor
from cliente import Cliente
import threading
from decorador import log_operaciones

if __name__ == "__main__":
    main = Tk()
    vista.VentanaPrincipal(main)
    main.mainloop()


