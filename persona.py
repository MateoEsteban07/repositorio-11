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
        
        Raises:
            ValueError: Si nombre o identificacion están vacíos
        """
        if not nombre or not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre debe ser una cadena no vacía")
        if not identificacion or not isinstance(identificacion, str) or not identificacion.strip():
            raise ValueError("La identificación debe ser una cadena no vacía")
        
        self.nombre = nombre.strip()
        self.identificacion = identificacion.strip()
    
    def __str__(self):
        return f"{self.nombre} (ID: {self.identificacion})"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', '{self.identificacion}')"
