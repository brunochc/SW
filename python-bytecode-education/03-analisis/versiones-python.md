# Versiones de Python y Magic Numbers

Cada versión de Python cambia ligeramente (o drásticamente) su bytecode. Para evitar desastres, Python usa un "Magic Number" al inicio de cada `.pyc`.

## Tabla de Magic Numbers

| Versión Python | Magic Number (Hex) | Valor Decimal |
|----------------|--------------------|---------------|
| **3.13**       | `bb 0d 0d 0a`      | 3515          |
| **3.12**       | `cb 0d 0d 0a`      | 3531          |
| **3.11**       | `a7 0d 0d 0a`      | 3495          |
| **3.10**       | `6f 0d 0d 0a`      | 3439          |
| **3.9**        | `61 0d 0d 0a`      | 3425          |
| **3.8**        | `55 0d 0d 0a`      | 3413          |
| **3.7**        | `42 0d 0d 0a`      | 3394          |

> Nota: Los bytes `0d 0a` al final son constantes (`\r\n`). Lo que cambia son los dos primeros bytes.

## ¿Por qué cambia?

El bytecode de Python **no es estable**.
*   Se agregan nuevos opcodes (ej. para mejorar `f-strings`).
*   Se eliminan opcodes obsoletos.
*   Se cambia el significado de argumentos.

Por ejemplo, en Python 3.11 se introdujo el "Specializing Adaptive Interpreter", lo que cambió radicalmente cómo funcionan ciertas instrucciones para hacerlas más rápidas. Un `.pyc` de 3.10 sería basura ininteligible para la PVM de 3.11.

## PEP 552: Bytecode Determinista

Históricamente, los `.pyc` incluían un timestamp. Esto significaba que si compilabas el mismo archivo dos veces, obtenías dos binarios diferentes (por la fecha).

El [PEP 552](https://peps.python.org/pep-0552/) introdujo la opción de usar un **hash** del archivo fuente en lugar del timestamp. Esto permite "Builds Reproducibles": compilar el mismo código siempre genera el mismo bit-a-bit `.pyc`.
