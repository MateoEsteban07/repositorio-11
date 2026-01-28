"""
Módulo para gestionar el registro de asistencia
"""

from datetime import datetime
import json
import os


class RegistroAsistencia:
    """Clase para gestionar el registro de asistencia"""
    
    # Constantes de formato
    DATE_FORMAT = "%Y-%m-%d"
    TIME_FORMAT = "%H:%M:%S"
    SEPARATOR_WIDTH = 60
    
    def __init__(self, archivo_datos="asistencia.json"):
        """
        Inicializa el registro de asistencia
        
        Args:
            archivo_datos (str): Nombre del archivo para guardar los datos
        
        Raises:
            ValueError: Si el archivo contiene secuencias de travesía de directorios
        """
        # Validar que el archivo no contenga rutas peligrosas
        if ".." in archivo_datos or archivo_datos.startswith("/"):
            raise ValueError("El nombre del archivo no puede contener rutas absolutas o '..'")
        
        self.archivo_datos = os.path.basename(archivo_datos)
        self.asistencias = []
        self.cargar_datos()
    
    def registrar_asistencia(self, persona, fecha=None):
        """
        Registra la asistencia de una persona
        
        Args:
            persona: Objeto Persona
            fecha: Fecha de la asistencia (datetime). Si es None, usa la fecha actual
        
        Raises:
            AttributeError: Si persona no tiene los atributos requeridos
        """
        if not hasattr(persona, 'nombre') or not hasattr(persona, 'identificacion'):
            raise AttributeError("El objeto persona debe tener atributos 'nombre' e 'identificacion'")
        
        if fecha is None:
            fecha = datetime.now()
        
        registro = {
            "nombre": persona.nombre,
            "identificacion": persona.identificacion,
            "fecha": fecha.strftime(self.DATE_FORMAT),
            "hora": fecha.strftime(self.TIME_FORMAT)
        }
        
        self.asistencias.append(registro)
        print(f"✓ Asistencia registrada: {persona.nombre} - {registro['fecha']} {registro['hora']}")
    
    def obtener_asistencias(self, identificacion=None, fecha=None):
        """
        Obtiene las asistencias filtradas por identificación y/o fecha
        
        Args:
            identificacion (str): Filtrar por identificación de persona
            fecha (str): Filtrar por fecha en formato YYYY-MM-DD
        
        Returns:
            list: Lista de registros de asistencia
        """
        resultados = self.asistencias
        
        if identificacion or fecha:
            resultados = [
                asistencia for asistencia in resultados
                if (not identificacion or asistencia["identificacion"] == identificacion) and
                   (not fecha or asistencia["fecha"] == fecha)
            ]
        
        return resultados
    
    def mostrar_asistencias(self, identificacion=None, fecha=None):
        """
        Muestra las asistencias en formato legible
        
        Args:
            identificacion (str): Filtrar por identificación de persona
            fecha (str): Filtrar por fecha en formato YYYY-MM-DD
        """
        asistencias = self.obtener_asistencias(identificacion, fecha)
        
        if not asistencias:
            print("No se encontraron registros de asistencia.")
            return
        
        print("\n" + "="*self.SEPARATOR_WIDTH)
        print("REGISTROS DE ASISTENCIA")
        print("="*self.SEPARATOR_WIDTH)
        
        for asistencia in asistencias:
            print(f"Nombre: {asistencia['nombre']}")
            print(f"ID: {asistencia['identificacion']}")
            print(f"Fecha: {asistencia['fecha']}")
            print(f"Hora: {asistencia['hora']}")
            print("-"*self.SEPARATOR_WIDTH)
    
    def guardar_datos(self):
        """Guarda los datos de asistencia en un archivo JSON"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(self.asistencias, f, ensure_ascii=False, indent=2)
            print(f"✓ Datos guardados en {self.archivo_datos}")
        except (IOError, OSError) as e:
            print(f"✗ Error al guardar datos: {e}")
        except Exception as e:
            print(f"✗ Error inesperado al guardar datos: {e}")
    
    def cargar_datos(self):
        """Carga los datos de asistencia desde un archivo JSON"""
        if os.path.exists(self.archivo_datos):
            try:
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    self.asistencias = json.load(f)
                print(f"✓ Datos cargados desde {self.archivo_datos}")
            except json.JSONDecodeError as e:
                print(f"✗ Error al decodificar JSON: {e}")
                print(f"⚠ El archivo {self.archivo_datos} está corrupto. Iniciando con datos vacíos.")
                self.asistencias = []
            except (IOError, OSError) as e:
                print(f"✗ Error al leer archivo: {e}")
                self.asistencias = []
            except Exception as e:
                print(f"✗ Error inesperado al cargar datos: {e}")
                self.asistencias = []
        else:
            print(f"ℹ No se encontró archivo de datos. Se creará uno nuevo.")
            self.asistencias = []
    
    def obtener_estadisticas(self):
        """
        Obtiene estadísticas de asistencia
        
        Returns:
            dict: Diccionario con estadísticas
        """
        total_registros = len(self.asistencias)
        
        # Contar personas únicas
        personas_unicas = set(asistencia["identificacion"] for asistencia in self.asistencias)
        total_personas = len(personas_unicas)
        
        # Contar fechas únicas
        fechas_unicas = set(asistencia["fecha"] for asistencia in self.asistencias)
        total_fechas = len(fechas_unicas)
        
        return {
            "total_registros": total_registros,
            "total_personas": total_personas,
            "total_fechas": total_fechas
        }
    
    def mostrar_estadisticas(self):
        """Muestra las estadísticas de asistencia"""
        stats = self.obtener_estadisticas()
        
        print("\n" + "="*self.SEPARATOR_WIDTH)
        print("ESTADÍSTICAS DE ASISTENCIA")
        print("="*self.SEPARATOR_WIDTH)
        print(f"Total de registros: {stats['total_registros']}")
        print(f"Total de personas: {stats['total_personas']}")
        print(f"Total de días con registro: {stats['total_fechas']}")
        print("="*self.SEPARATOR_WIDTH)
