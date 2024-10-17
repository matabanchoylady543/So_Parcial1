class Tarea:
    def __init__(self, nombre, duracion, llegada, tipo_cola, prioridad):
        self.nombre = nombre  # ID de tarea
        self.duracion = duracion  # 
        self.llegada = llegada  # Tiempo de llegada
        self.tipo_cola = tipo_cola  # 
        self.prioridad = prioridad  # Prioridad de la tarea
        self.duracion_inicial = duracion  # Guardar duracion
        self.espera = 0  # TW
        self.finalizacion = 0  # Tiempo fin
        self.respuesta = -1  # Tiempo de resp
        self.retorno = 0  #  turnaround
        self.completada = False  # estado
