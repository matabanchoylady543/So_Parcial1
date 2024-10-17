from tareas import Tarea

def cargar_tareas(planificador, archivo_entrada):
    with open(archivo_entrada, 'r') as archivo:
        for linea in archivo:
            if not linea.strip() or linea.startswith('#'):
                continue
            datos = linea.strip().split(';')
            tarea = Tarea(datos[0], int(datos[1]), int(datos[2]), int(datos[3]), int(datos[4]))
            planificador.agregar_tarea(tarea)
