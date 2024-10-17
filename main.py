from planificador import Planificador
from archivos_gestion import cargar_tareas

planificador = Planificador()
planificador.reiniciar()
cargar_tareas(planificador, 'mlq001.txt')
planificador.ejecutar()
planificador.guardar_resultados('mlq001_out.txt')
print("Archivo 1 realizado")
    
planificador.reiniciar()
cargar_tareas(planificador, 'mlq026.txt')
planificador.ejecutar()
planificador.guardar_resultados('mlq026_out.txt')
print("Archivo 2 realizado")
    
planificador.reiniciar()
cargar_tareas(planificador, 'mlq014.txt')
planificador.ejecutar()
planificador.guardar_resultados('mlq014_out.txt')
print("Archivo 3 realizado")

