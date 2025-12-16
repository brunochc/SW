# Decompiladores: Ingeniería Inversa

Así como podemos ir de Código Fuente -> Bytecode, existen herramientas para intentar ir de Bytecode -> Código Fuente.

## ¿Qué es un decompilador?
Es una herramienta que lee los opcodes de un archivo `.pyc` e intenta reconstruir el código Python original que los generó.

## Herramientas Populares

### 1. `uncompyle6`
El estándar de oro para versiones antiguas de Python (hasta 3.8 aprox). Muy preciso.

```bash
pip install uncompyle6
uncompyle6 archivo.pyc > recuperado.py
```

### 2. `pycdc` (Python Bytecode Disassembler and Decompiler)
Una herramienta escrita en C++ que soporta versiones más modernas de Python (3.9+). Es más robusta para nuevas versiones donde `uncompyle6` falla.

### 3. `decompyle3`
Un fork de `uncompyle6` enfocado en Python 3.7+.

## Limitaciones
La decompilación **no es perfecta**. Al compilar a bytecode, se pierde información:
*   **Comentarios:** Se pierden completamente.
*   **Formato:** La indentación y espacios originales se pierden (el decompilador inventa los suyos).
*   **Nombres de variables:** Generalmente se conservan, pero en algunos casos de optimización extrema podrían perderse.
*   **Docstrings:** Se conservan (son objetos constantes).

## Uso Ético y Seguridad
Saber decompilar es útil para:
*   Recuperar tu propio código si borraste el `.py` por accidente.
*   Analizar malware escrito en Python.
*   Auditar qué está haciendo realmente una librería cerrada.

Sin embargo, también demuestra por qué **nunca debes confiar secretos (contraseñas, keys) en tu código**, incluso si solo distribuyes los `.pyc`. ¡Cualquiera puede leerlos!
