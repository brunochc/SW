# El Módulo `dis`: Tu Estetoscopio para Python

El módulo `dis` (disassembler) es la herramienta más importante para entender qué está haciendo Python internamente. Te permite ver el bytecode de cualquier script, clase o función.

## Uso Básico

### Desde la terminal
Puedes desensamblar un script entero sin modificarlo:

```bash
python -m dis mi_script.py
```

### Desde el código
Puedes importar `dis` y usarlo para inspeccionar funciones específicas:

```python
import dis

def suma(a, b):
    return a + b

dis.dis(suma)
```

## Entendiendo la Salida

La salida de `dis` tiene varias columnas:

```text
  4           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_OP                0 (+)
              6 RETURN_VALUE
```

1.  **Número de línea (4):** La línea de código en tu archivo `.py`.
2.  **Offset (0, 2, 4...):** La dirección de memoria (índice) de la instrucción dentro del objeto de código.
3.  **Opcode (LOAD_FAST):** El nombre de la instrucción (operación) a ejecutar.
4.  **Argumento (0):** El parámetro de la instrucción (si lo tiene).
5.  **Interpretación ((a)):** `dis` amablemente nos dice qué significa ese argumento (ej. la variable `a`).

## Opcodes Comunes

*   `LOAD_FAST`: Carga una variable local en la pila.
*   `LOAD_GLOBAL`: Carga una variable global.
*   `STORE_FAST`: Guarda el valor superior de la pila en una variable local.
*   `BINARY_OP`: Realiza una operación binaria (suma, resta, etc.).
*   `CALL`: Llama a una función.
*   `RETURN_VALUE`: Retorna el resultado.

## Ejercicio
Intenta ejecutar `python -m dis` sobre un script simple con un bucle `for` y observa cómo se traduce a instrucciones `FOR_ITER` y `JUMP_BACKWARD`.
