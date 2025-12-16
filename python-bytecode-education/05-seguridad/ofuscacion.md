# Ofuscación: ¿Qué funciona realmente?

Si los `.pyc` no protegen el código, ¿qué opciones tenemos?

## 1. Eliminación de Metadatos (`python -OO`)

Python tiene flags de optimización que eliminan cierta información del bytecode.

*   `python -O`: Elimina las sentencias `assert`.
*   `python -OO`: Elimina `assert` y **todos los docstrings**.

```bash
python -OO -m py_compile mi_script.py
```

Esto reduce el tamaño del archivo y elimina la documentación interna, pero la lógica sigue siendo legible.

## 2. Ofuscadores de Código (Ej. PyArmor)

Herramientas como **PyArmor** van un paso más allá. No solo compilan, sino que:
1.  **Encriptan el bytecode:** El archivo en disco está cifrado.
2.  **Modifican el Runtime:** Inyectan una librería dinámica (DLL/.so) que intercepta la carga del módulo en memoria, lo desencripta al vuelo y se lo pasa a la PVM.

Esto hace que herramientas como `dis` o `uncompyle6` fallen, porque no pueden leer el archivo encriptado.

### ¿Es infalible?
No. Al final, el código debe desencriptarse en memoria para ejecutarse. Un atacante experto con un debugger de memoria podría volcar el bytecode desencriptado. Pero eleva la barrera de entrada significativamente.

## 3. Compilación a C (Cython / Nuitka)

La opción más robusta es traducir tu Python a C y compilarlo a código máquina real.
*   **Cython:** Traduce `.py` a `.c`.
*   **Nuitka:** Compila todo el programa a un ejecutable binario.

Esto hace que la ingeniería inversa sea tan difícil como analizar cualquier programa en C++ (mucho más difícil que decompilar un `.pyc`).
