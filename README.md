# Generador de Contraseñas Seguras 🔐

## Configuración del entorno

- Se configuró el repositorio en GitHub para cargar el desarrollo.
- Se diseñaron diagramas de flujo de las principales funcionalidades:
  - Generar contraseña aleatoria.
  - Selección de longitud de la contraseña.
  - Inclusión de mayúsculas, números y símbolos.
- Se preparó el ambiente de desarrollo en **Python (VS Code)**.
- Se subió un primer avance de la codificación del generador de contraseñas.

###  Estructura del repositorio
- `/src`: contiene el código fuente en Python.
- `/diagramas`: contiene los diagramas de flujo.
- `README.md`: documentación del proyecto.

###  Avance de la codificación
Ejemplo de funcionamiento actual del programa:

```python
import random
import string

# Función para generar la contraseña
def generar_contrasena(longitud=12):
    # Caracteres disponibles: letras, dígitos y símbolos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    # Selección aleatoria de caracteres
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

# Ejecución de ejemplo
print("Tu contraseña generada es:", generar_contrasena(12))
