# Alumno : Sebastian Sanchez Bentolila

# Cliente - Aplicación {gestor de contactos}

# Librerías
import socket
import sys

# Clases 
class Cliente:
    # Cliente 
  
    # Atributos 
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectar()

    # Métodos
    def conectar(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            print("Conexión establecida con el servidor.")
        except Exception as e:
            print(f"Error al conectar con el servidor: {e}")
            sys.exit(1)

    def enviar_mensaje(self, mensaje):
        try:
            self.socket_cliente.sendall(mensaje.encode('utf-8'))
            print("Mensaje enviado al servidor.")
        except Exception as e:
            print(f"Error al enviar mensaje al servidor: {e}")
            
    def recibir_mensaje(self):
        try:
            datos = self.socket_cliente.recv(1024)
            mensaje_recibido = datos.decode('utf-8')
            print(f"Mensaje recibido del servidor: {mensaje_recibido}")
        except Exception as e:
            print(f"Error al recibir mensaje del servidor: {e}")

    def cerrar_conexion(self):
        try:
            self.socket_cliente.close()
            print("Conexión cerrada correctamente.")
        except Exception as e:
            print(f"Error al cerrar la conexión: {e}")