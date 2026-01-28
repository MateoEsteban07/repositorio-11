"""
Script de ejemplo para demostrar el uso del sistema de registro de asistencia
"""

from persona import Persona
from asistencia import RegistroAsistencia
from datetime import datetime, timedelta

# Constante para el ancho del separador
SEPARATOR_WIDTH = 60


def demo():
    """Ejecuta una demostración del sistema"""
    print("="*SEPARATOR_WIDTH)
    print("DEMOSTRACIÓN DEL SISTEMA DE REGISTRO DE ASISTENCIA")
    print("="*SEPARATOR_WIDTH)
    print()
    
    # Crear instancia del registro
    print("1. Creando instancia del registro de asistencia...")
    registro = RegistroAsistencia("demo_asistencia.json")
    print()
    
    # Crear personas
    print("2. Creando personas...")
    personas = [
        Persona("María García", "11111111"),
        Persona("Carlos López", "22222222"),
        Persona("Ana Martínez", "33333333"),
        Persona("Pedro Sánchez", "44444444"),
        Persona("Laura Torres", "55555555")
    ]
    
    for persona in personas:
        print(f"   - {persona}")
    print()
    
    # Registrar asistencias
    print("3. Registrando asistencias...")
    # Nota: Se usan diferentes tiempos para demostrar el historial
    for i, persona in enumerate(personas):
        # Simular diferentes tiempos (solo para propósitos de demostración)
        fecha = datetime.now() - timedelta(seconds=i*5)
        registro.registrar_asistencia(persona, fecha)
    print()
    
    # Registrar algunas asistencias adicionales para el mismo día
    print("4. Registrando asistencias adicionales...")
    registro.registrar_asistencia(personas[0])
    registro.registrar_asistencia(personas[1])
    print()
    
    # Mostrar todas las asistencias
    print("5. Mostrando todas las asistencias:")
    registro.mostrar_asistencias()
    print()
    
    # Mostrar estadísticas
    print("6. Mostrando estadísticas:")
    registro.mostrar_estadisticas()
    print()
    
    # Buscar asistencias de una persona específica
    print("7. Buscando asistencias de María García (ID: 11111111):")
    registro.mostrar_asistencias(identificacion="11111111")
    print()
    
    # Guardar datos
    print("8. Guardando datos...")
    registro.guardar_datos()
    print()
    
    print("="*SEPARATOR_WIDTH)
    print("DEMOSTRACIÓN COMPLETADA")
    print("="*SEPARATOR_WIDTH)
    print()
    print("Los datos se han guardado en 'demo_asistencia.json'")
    print("Puede cargarlos nuevamente ejecutando este script otra vez.")


if __name__ == "__main__":
    demo()
