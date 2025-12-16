# Anatomía de un Archivo .pyc

En esta sección, vamos a diseccionar un archivo real: `base_command.cpython-312.pyc`.

## Datos del Caso de Estudio
*   **Archivo:** `base_command.cpython-312.pyc`
*   **Tamaño Total:** 10,437 bytes
*   **Versión Python:** 3.12

## 1. El Encabezado (Header)

Los primeros 16 bytes del archivo son metadatos cruciales para la Máquina Virtual.

```text
| Offset | Tamaño | Descripción          | Valor Hex (Ejemplo) | Interpretación |
|--------|--------|----------------------|---------------------|----------------|
| 0      | 4      | **Magic Number**     | `cb 0d 0d 0a`       | Python 3.12    |
| 4      | 4      | **Bitfield**         | `00 00 00 00`       | Standard       |
| 8      | 4      | **Timestamp**        | `...`               | Fecha modif.   |
| 12     | 4      | **Tamaño Fuente**    | `...`               | Bytes del .py  |
```

### Magic Number (`cb 0d 0d 0a`)
*   `0xcb 0x0d` (Little Endian) = 3531. Este es el ID único de Python 3.12.
*   `0x0d 0x0a` = `\r\n`. Esto asegura que si abres el archivo en modo texto, se rompa de forma "segura" sin corromper la terminal.

## 2. El Cuerpo (Marshalled Code Object)

A partir del byte 16, comienza el objeto de código serializado usando el formato `marshal` de Python.

En nuestro archivo `base_command.pyc`, este objeto contiene:

### Estadísticas Internas
*   **Bytecode Puro:** 364 bytes. Estas son las instrucciones reales (`LOAD_FAST`, `CALL`, etc.).
*   **Constantes:** 19 objetos (números, strings, tuplas usadas en el código).
*   **Nombres:** 57 identificadores (nombres de variables, funciones, atributos).

### ¿Por qué el archivo pesa 10KB si el bytecode son solo 364 bytes?
¡Buena pregunta!
El archivo `.pyc` no solo guarda las instrucciones de la función principal, sino que guarda **recursivamente** todo:
1.  Docstrings (pueden ser largos).
2.  Nombres de todas las variables y métodos importados.
3.  Objetos de código de todas las clases y funciones definidas dentro del archivo.

En `base_command.py`, seguramente hay una clase `Command` grande. El bytecode de esa clase y todos sus métodos están empaquetados dentro de este archivo.

## Visualización

```text
[ HEADER (16 bytes) ]
[ TYPE_CODE (1 byte) ] -> Indica que sigue un objeto de código ('c')
[ ARGCOUNT (4 bytes) ]
[ ... otros metadatos ... ]
[ BYTECODE (364 bytes) ] -> Las instrucciones de nivel superior
[ CONSTANTS (Lista) ]
    |-> [ String "Hola" ]
    |-> [ Code Object "Clase Command" ] -> ¡Recursión!
            |-> [ Bytecode de Command ]
            |-> [ Constantes de Command ]
```

## Conclusión
Un `.pyc` es básicamente un "dump" de memoria de los objetos internos de Python, listo para ser cargado directamente a la RAM sin necesidad de parsear texto.
