# Control Flow: Bucles y Decisiones

¿Cómo maneja la PVM las estructuras de control como `if` y `for`? Spoiler: Todo son saltos (JUMP).

## 1. El `if` es un salto

```python
def analizar_numero(n):
    if n > 0:
        return "Positivo"
    return "No positivo"
```

### Bytecode (Simplificado)

```text
  2           0 LOAD_FAST                0 (n)
              2 LOAD_CONST               1 (0)
              4 COMPARE_OP               4 (>)
              6 POP_JUMP_IF_FALSE       10 (to 12)  <-- ¡Aquí está la magia!

  3           8 RETURN_CONST             2 ('Positivo')

  4     >>   12 RETURN_CONST             3 ('No positivo')
```

*   `POP_JUMP_IF_FALSE`: Si la comparación es Falsa, salta directamente a la instrucción 12. Si es Verdadera, continúa en la 8.

## 2. Bucles `for` vs List Comprehensions

Las List Comprehensions no son solo "azúcar sintáctico"; tienen su propio opcode optimizado.

### Bucle For Clásico
```python
res = []
for i in range(10):
    res.append(i)
```
Implica: `LOAD_METHOD` (append) y `CALL_METHOD` en cada iteración.

### List Comprehension
```python
res = [i for i in range(10)]
```
Usa la instrucción `LIST_APPEND`.

*   `LIST_APPEND`: Añade un elemento a la lista que se está construyendo directamente en la pila, sin la sobrecarga de buscar el método `.append()` y llamarlo cada vez.

**Conclusión:** Las comprehensions son generalmente más rápidas para crear listas nuevas.
