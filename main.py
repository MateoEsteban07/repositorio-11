"""
Programa principal para el sistema de registro de asistencia
"""

from persona import Persona
from asistencia import RegistroAsistencia
from datetime import datetime


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("SISTEMA DE REGISTRO DE ASISTENCIA")
    print("="*60)
    print("1. Registrar asistencia")
    print("2. Ver todas las asistencias")
    print("3. Buscar asistencias por persona")
    print("4. Buscar asistencias por fecha")
    print("5. Ver estadísticas")
    print("6. Guardar y salir")
    print("="*60)


def registrar_nueva_asistencia(registro):
    """
    Registra una nueva asistencia
    
    Args:
        registro: Objeto RegistroAsistencia
    """
    print("\n--- REGISTRAR ASISTENCIA ---")
    nombre = input("Nombre completo: ").strip()
    identificacion = input("Número de identificación: ").strip()
    
    if not nombre or not identificacion:
        print("✗ Error: El nombre y la identificación son obligatorios")
        return
    
    persona = Persona(nombre, identificacion)
    registro.registrar_asistencia(persona)


def buscar_por_persona(registro):
    """
    Busca asistencias por identificación de persona
    
    Args:
        registro: Objeto RegistroAsistencia
    """
    print("\n--- BUSCAR POR PERSONA ---")
    identificacion = input("Número de identificación: ").strip()
    
    if not identificacion:
        print("✗ Error: La identificación es obligatoria")
        return
    
    registro.mostrar_asistencias(identificacion=identificacion)


def buscar_por_fecha(registro):
    """
    Busca asistencias por fecha
    
    Args:
        registro: Objeto RegistroAsistencia
    """
    print("\n--- BUSCAR POR FECHA ---")
    fecha = input("Fecha (YYYY-MM-DD) o presione Enter para hoy: ").strip()
    
    if not fecha:
        fecha = datetime.now().strftime("%Y-%m-%d")
    
    registro.mostrar_asistencias(fecha=fecha)


def main():
    """Función principal del programa"""
    registro = RegistroAsistencia()
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_nueva_asistencia(registro)
        elif opcion == "2":
            registro.mostrar_asistencias()
        elif opcion == "3":
            buscar_por_persona(registro)
        elif opcion == "4":
            buscar_por_fecha(registro)
        elif opcion == "5":
            registro.mostrar_estadisticas()
        elif opcion == "6":
            registro.guardar_datos()
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    main()
