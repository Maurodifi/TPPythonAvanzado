from functools import wraps
from datetime import datetime


def log_operaciones(operacion):

    """
    Registra en un archivo txt las operaciones realizadas.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open("log_operaciones.txt", "a") as log_file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp} - Operaciovn {operacion}: {result}\n"
                log_file.write(log_entry)
            return result
        return wrapper
    return decorator
