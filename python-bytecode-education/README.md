# 🐍 Python Bytecode Education

> "Python es un lenguaje interpretado... pero primero es compilado."

Este repositorio es una guía práctica para entender qué pasa realmente cuando ejecutas un script de Python. Desde los archivos `.pyc` hasta la Máquina Virtual de Python (PVM).

## ⚡ Caso de Estudio: `base_command.pyc`

Para entender la anatomía de un archivo compilado, hemos analizado el archivo `base_command.cpython-312.pyc` incluido en este repo.

### ¿Qué hay dentro de esos 10KB?

Aunque el código fuente original puede parecer simple, el archivo binario `.pyc` es una estructura compleja.

**1. El Encabezado (Header)**
Los primeros 16 bytes definen la identidad del archivo:

```text
| Offset | Valor Hex       | Significado          |
|--------|-----------------|----------------------|
| 0-3    | `cb 0d 0d 0a`   | **Magic Number** (Python 3.12) |
| 4-7    | `00 00 00 00`   | Flags (Standard)     |
| 8-11   | `...`           | Timestamp (Modificación) |
| 12-15  | `...`           | Tamaño del fuente    |
```

**2. El Cuerpo (Recursivo)**
El archivo pesa **10,437 bytes** pero solo contiene **364 bytes** de instrucciones de bytecode puro. ¿Por qué?

Porque un `.pyc` guarda **objetos completos**, no solo texto.
*   Si defines una clase, el `.pyc` guarda el objeto de código de la clase.
*   Si esa clase tiene métodos, guarda los objetos de código de los métodos dentro de la clase.
*   Incluye todos los docstrings, nombres de variables y constantes.

👉 **[Ver el análisis completo paso a paso aquí](./03-analisis/estructura-pyc.md)**

---

## 📚 Contenido del Curso

Este repositorio está organizado en módulos progresivos:

### 1. [Fundamentos](./01-fundamentos/README.md)
*   Compilación vs Interpretación.
*   Qué es exactamente el Bytecode.

### 2. [Herramientas](./02-herramientas/README.md)
*   Uso del módulo `dis` (disassembler).
*   Compilación manual (`py_compile`).
*   Decompiladores (Ingeniería Inversa).

### 3. [Análisis Profundo](./03-analisis/README.md)
*   **Disección de archivos .pyc** (Nivel avanzado).
*   Magic Numbers y versiones de Python.

### 4. [Ejemplos Prácticos](./04-ejemplos-practicos/README.md)
*   Optimizaciones: Por qué `[]` es más rápido que `list()`.
*   Control Flow: Cómo funcionan los `if` y `for` por dentro.

### 5. [Seguridad](./05-seguridad/README.md)
*   Mitos: Por qué los `.pyc` NO protegen tu código.
*   Ataques de inyección de bytecode.

---

## 🛠️ Uso Rápido

Hemos incluido scripts para que experimentes por ti mismo.

**1. Ver el bytecode de un ejemplo:**
```bash
python3 demos/ejemplo_simple.py
```

**2. Analizar cualquier archivo .pyc:**
```bash
python3 scripts-utiles/analizador_basico.py __pycache__/tu_archivo.cpython-312.pyc
```

## 📄 Licencia
MIT License. Siéntete libre de usar este material para aprender y enseñar.
