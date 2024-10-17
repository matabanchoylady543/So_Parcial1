from collections import deque
from tareas import Tarea

class Planificador:
    def __init__(self):
        self.tareas = []  # Lista de tareas
        self.cola1 = deque()  # Cola 1 para Round Robin con quantum3
        self.cola2 = deque()  # Cola 2 para Round Robin con quantum 5
        self.cola_fcfs = []  # Cola FCFS 
        self.tiempo_actual = 0  # total time

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def actualizar_tarea(self, tarea_modificada):
        for i, tarea in enumerate(self.tareas):
            if tarea.nombre == tarea_modificada.nombre:
                self.tareas[i] = tarea_modificada

    def ejecutar(self):
        # Distribuir tareas en las colas
        for tarea in self.tareas:
            if tarea.tipo_cola == 1:
                self.cola1.append(tarea)
            elif tarea.tipo_cola == 2:
                self.cola2.append(tarea)
            elif tarea.tipo_cola == 3:
                self.cola_fcfs.append(tarea)

        # Ejecutar tareas en Round Robin y FCFS
        self.ejecutar_round_robin(self.cola1, 3)  # Quantum 3 para la cola 1
        self.ejecutar_round_robin(self.cola2, 5)  # Quantum 5 para la cola 2
        self.ejecutar_fcfs()  # Cola FCFS

    def ejecutar_round_robin(self, cola, quantum):
        while cola:
            tarea = cola.popleft()  # Sacar tarea de la cola
            
            if tarea.llegada > self.tiempo_actual:
                self.tiempo_actual = tarea.llegada

            if tarea.respuesta == -1:
                tarea.respuesta = self.tiempo_actual

            tiempo_uso = min(tarea.duracion, quantum)
            tarea.duracion -= tiempo_uso
            self.tiempo_actual += tiempo_uso

            if tarea.duracion == 0:
                tarea.finalizacion = self.tiempo_actual
                tarea.retorno = tarea.finalizacion - tarea.llegada
                tarea.espera = tarea.retorno - tarea.duracion_inicial
                tarea.completada = True
                self.actualizar_tarea(tarea)
            else:
                cola.append(tarea)

    def ejecutar_fcfs(self):
        # Ordenar tareas respecto a como llegan
        self.cola_fcfs.sort(key=lambda x: x.llegada)

        for tarea in self.cola_fcfs:
            if tarea.llegada > self.tiempo_actual:
                self.tiempo_actual = tarea.llegada

            if tarea.respuesta == -1:
                tarea.respuesta = self.tiempo_actual

            tarea.espera = self.tiempo_actual - tarea.llegada
            self.tiempo_actual += tarea.duracion
            tarea.finalizacion = self.tiempo_actual
            tarea.retorno = tarea.finalizacion - tarea.llegada
            tarea.completada = True
            self.actualizar_tarea(tarea)

    def guardar_resultados(self, archivo_salida):
        with open(archivo_salida, 'w') as archivo:
            archivo.write(f"# Archivo: {archivo_salida}\n")
            archivo.write("# etiqueta; BT; AT; Q; Pr; WT; CT; RT; TAT\n")
            total_espera = total_finalizacion = total_respuesta = total_retorno = 0

            for tarea in self.tareas:
                archivo.write(f"{tarea.nombre};{tarea.duracion_inicial};{tarea.llegada};{tarea.tipo_cola};"
                              f"{tarea.prioridad};{tarea.espera};{tarea.finalizacion};"
                              f"{tarea.respuesta};{tarea.retorno}\n")
                
                total_espera += tarea.espera
                total_finalizacion += tarea.finalizacion
                total_respuesta += tarea.respuesta
                total_retorno += tarea.retorno

            num_tareas = len(self.tareas)
            archivo.write(f"WT={total_espera / num_tareas:.1f}; "
                          f"CT={total_finalizacion / num_tareas:.1f}; "
                          f"RT={total_respuesta / num_tareas:.1f}; "
                          f"TAT={total_retorno / num_tareas:.1f};\n")

    def reiniciar(self):
        self.tareas.clear()
        self.cola1.clear()
        self.cola2.clear()
        self.cola_fcfs.clear()
        self.tiempo_actual = 0
