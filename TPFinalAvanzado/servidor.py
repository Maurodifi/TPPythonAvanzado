# Alumno : Sebastian Sanchez Bentolila

# Servidor - Aplicación {gestor de contactos}

# Librerías 
import socket
import threading
import sys

# Clases
class Servidor:
    # Servidor con socket
    
    # Atributos
    def __init__(self, host, port, ):
        self.host = host
        self.port = port
        self.socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_servidor.bind((self.host, self.port))
        self.clientes_conectados = []

    # Métodos 
    def iniciar(self):
        try:
            self.socket_servidor.listen()

            while True:
                cliente = self.socket_servidor.accept()
                self.clientes_conectados.append(cliente)

                # Iniciar un hilo para manejar la comunicación con el cliente
                hilo_cliente = threading.Thread(target=self.atender_cliente, args=(cliente,))
                hilo_cliente.start()
        except Exception as e:
            print(f"Error al iniciar el servidor: {e}")
            sys.exit(1)

    def atender_cliente(self, cliente):
        try:
            print ("Hola Estoy desde cliente")
        finally:
            print ("Mensaje recibido y enviado")

    def detener(self):
        try:
            self.socket_servidor.close()
        except Exception as e:
            print(f"Error al detener el servidor: {e}")
            sys.exit(1)      