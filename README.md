# Sistema de Registro de Asistencia

Un sistema simple y eficiente para registrar y gestionar la asistencia de personas (estudiantes, empleados, etc.).

## Características

- ✅ Registro de asistencia con fecha y hora automática
- ✅ Búsqueda por persona o fecha
- ✅ Estadísticas de asistencia
- ✅ Persistencia de datos en formato JSON
- ✅ Interfaz de línea de comandos fácil de usar

## Requisitos

- Python 3.6 o superior

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/MateoEsteban07/repositorio-11.git
cd repositorio-11
```

## Uso

### Ejecutar el programa principal

```bash
python main.py
```

### Menú principal

El sistema ofrece las siguientes opciones:

1. **Registrar asistencia**: Ingresa el nombre e identificación de una persona para registrar su asistencia
2. **Ver todas las asistencias**: Muestra todos los registros guardados
3. **Buscar asistencias por persona**: Filtra los registros por número de identificación
4. **Buscar asistencias por fecha**: Filtra los registros por fecha específica
5. **Ver estadísticas**: Muestra un resumen de los registros
6. **Guardar y salir**: Guarda los datos y cierra el programa

### Ejemplo de uso

```python
from persona import Persona
from asistencia import RegistroAsistencia

# Crear instancia del registro
registro = RegistroAsistencia()

# Crear una persona
persona = Persona("Juan Pérez", "12345678")

# Registrar asistencia
registro.registrar_asistencia(persona)

# Ver todas las asistencias
registro.mostrar_asistencias()

# Guardar datos
registro.guardar_datos()
```

## Estructura del Proyecto

```
repositorio-11/
│
├── main.py           # Programa principal con interfaz de usuario
├── persona.py        # Clase Persona
├── asistencia.py     # Clase RegistroAsistencia
├── ejemplo.py        # Script de demostración del sistema
├── .gitignore        # Archivos a ignorar en git
├── asistencia.json   # Archivo de datos (generado automáticamente)
└── README.md         # Este archivo
```

## Almacenamiento de Datos

Los datos se guardan automáticamente en el archivo `asistencia.json` en formato JSON. Cada registro contiene:

- Nombre de la persona
- Número de identificación
- Fecha (YYYY-MM-DD)
- Hora (HH:MM:SS)

## Características Técnicas

- **Orientado a objetos**: Utiliza clases para representar personas y el sistema de registro
- **Persistencia**: Los datos se guardan en formato JSON
- **Fecha/hora automática**: El sistema registra automáticamente la fecha y hora actual
- **Búsquedas y filtros**: Permite filtrar registros por persona o fecha
- **Estadísticas**: Calcula y muestra estadísticas básicas del sistema

## Autor

Mateo Esteban

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo.