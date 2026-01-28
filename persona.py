"""
Módulo para definir la clase Persona
"""

class Persona:
    """Clase para representar una persona en el sistema de asistencia"""
    
    def __init__(self, nombre, identificacion):
        """
        Inicializa una persona
        
        Args:
            nombre (str): Nombre completo de la persona
            identificacion (str): Número de identificación único
        """
        self.nombre = nombre
        self.identificacion = identificacion
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.identificacion})"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.identificacion}')"
