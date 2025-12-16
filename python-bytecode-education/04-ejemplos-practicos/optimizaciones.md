# Optimizaciones: Bytecode en Acción

Python puede parecer lento, pero su compilador hace algunos trucos inteligentes. Entenderlos te ayuda a escribir código más eficiente.

## 1. El caso de `[]` vs `list()`

Es un clásico de las entrevistas de Python: "¿Por qué `[]` es más rápido que `list()`?"

### Análisis con `dis`

```python
import dis

def usar_literal():
    return []

def usar_funcion():
    return list()

print("--- Literal [] ---")
dis.dis(usar_literal)

print("\n--- Función list() ---")
dis.dis(usar_funcion)
```

### El Resultado

**Literal `[]`:**
```text
  0 BUILD_LIST               0
  2 RETURN_VALUE
```
*   `BUILD_LIST`: Es una instrucción específica del bytecode. La PVM reserva memoria y crea la lista en un solo paso de C.

**Función `list()`:**
```text
  0 LOAD_GLOBAL              0 (list)
  2 CALL_FUNCTION            0
  4 RETURN_VALUE
```
*   `LOAD_GLOBAL`: Tiene que buscar el nombre "list" en el scope global (podrías haberlo sobreescrito).
*   `CALL_FUNCTION`: Tiene que preparar la pila para una llamada a función, saltar, ejecutar y volver.

**Conclusión:** `[]` es mucho más rápido porque evita la sobrecarga de llamar a una función.

## 2. Constant Folding (Plegado de Constantes)

Python intenta calcular expresiones constantes durante la compilación, no en la ejecución.

### Ejemplo

```python
def segundos_dia():
    return 24 * 60 * 60
```

### Bytecode

```text
  0 LOAD_CONST               1 (86400)
  2 RETURN_VALUE
```

¡Sorpresa! No hay instrucciones de multiplicación (`BINARY_OP`). Python vio que eran constantes y calculó `86400` al crear el `.pyc`.

**Tip:** Escribe `24 * 60 * 60` para que tu código sea legible. No pierdes rendimiento porque Python lo optimiza por ti.

## 3. Concatenación de Strings

Históricamente, hacer `s += "a"` en un bucle era terrible (cuadrático). Hoy en día, Python tiene una optimización especial para esto, pero `"".join()` sigue siendo el rey.

El bytecode de `join` es más eficiente para grandes cantidades de datos porque pre-calcula el tamaño final del string, mientras que `+=` (aunque optimizado) a veces tiene que realocar memoria repetidamente.
