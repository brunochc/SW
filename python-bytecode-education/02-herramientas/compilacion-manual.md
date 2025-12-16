# Compilación Manual: `py_compile` y `compileall`

Aunque Python compila tu código automáticamente cuando lo importas, a veces necesitas hacerlo manualmente.

## ¿Por qué compilar manualmente?
1.  **Verificar sintaxis:** Puedes comprobar si hay errores de sintaxis en todo tu proyecto sin ejecutarlo.
2.  **Distribución:** Puedes enviar solo los archivos `.pyc` (sin el código fuente `.py`) para dificultar (ligeramente) la lectura del código.
3.  **Optimización de inicio:** Pre-compilar todo para evitar que el usuario final tenga que esperar la compilación en la primera ejecución (especialmente en sistemas embebidos o grandes aplicaciones).

## Herramienta 1: `py_compile` (Un solo archivo)

Para compilar un script específico:

```bash
python -m py_compile mi_script.py
```

Esto generará el archivo `.pyc` en la carpeta `__pycache__`.

## Herramienta 2: `compileall` (Directorios completos)

Para compilar recursivamente todos los archivos Python en un directorio:

```bash
python -m compileall .
```

### Opciones útiles
*   `-b`: Escribe los archivos `.pyc` en su ubicación original (legacy) en lugar de `__pycache__`.
*   `-f`: Fuerza la recompilación incluso si los timestamps no han cambiado.
*   `-l`: No recurre en subdirectorios.

## Ejemplo de Distribución "Solo Bytecode"

Si quisieras distribuir tu programa sin código fuente:
1.  Compila todo: `python -m compileall .`
2.  Copia los `.pyc` y renómbralos para quitar la parte de la versión (ej. `script.cpython-312.pyc` -> `script.pyc`).
3.  Ejecuta directamente: `python script.pyc`.

> **Nota:** Esto no es seguridad real. El bytecode es fácilmente reversible (ver sección de Decompiladores).
