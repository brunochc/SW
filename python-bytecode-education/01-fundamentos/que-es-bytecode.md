# ¿Qué es el Bytecode?

El bytecode es una representación intermedia de tu código: más abstracta que el código máquina, pero más simple que el código fuente.

## Definición
Es un conjunto de instrucciones de bajo nivel diseñadas para ser ejecutadas por un intérprete de software (la Máquina Virtual), en lugar de directamente por el hardware (CPU).

Se llama "byte"-code porque históricamente cada código de operación (opcode) ocupaba un solo byte.

## Archivos .pyc y `__pycache__`

Seguro has visto esa carpeta `__pycache__` que aparece automáticamente. Ahí es donde Python guarda el bytecode compilado.

### Estructura de un archivo .pyc
Un archivo `.pyc` no es solo código; contiene metadatos importantes para asegurar que es válido:

1.  **Magic Number (4 bytes):** Identifica la versión de Python (ej. 3.10 vs 3.12). Si intentas correr un `.pyc` de Python 3.12 en Python 3.8, fallará gracias a esto.
2.  **Bitfield (4 bytes):** Flags de compilación (ej. optimización).
3.  **Timestamp (4 bytes):** Fecha de modificación del archivo `.py` original. Si el `.py` es más nuevo que el `.pyc`, Python recompila.
4.  **Tamaño (4 bytes):** Tamaño del archivo fuente.
5.  **Code Object:** El bytecode real (instrucciones, constantes, nombres de variables).

## Ejemplo Visual

Si tienes este código:
```python
def hola():
    return "Mundo"
```

El bytecode se ve así (simplificado):

```text
  2           0 LOAD_CONST               1 ('Mundo')
              2 RETURN_VALUE
```

*   `LOAD_CONST`: Instrucción para cargar un valor en la pila.
*   `RETURN_VALUE`: Instrucción para devolver el valor superior de la pila.

## ¿Es código máquina?
**No.**
*   Código máquina (x86): `0x55 0x48 0x89 0xe5` (Instrucciones binarias reales).
*   Bytecode Python: `LOAD_FAST`, `BINARY_OP` (Instrucciones para la PVM).

La PVM toma ese `BINARY_OP` y ejecuta el código máquina real necesario para sumar dos números (que es mucho más complejo porque debe manejar tipos dinámicos, conteo de referencias, etc.).
