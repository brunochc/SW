# Inyección de Bytecode: El Enemigo en Casa

Esta es una vulnerabilidad sutil pero peligrosa que afecta a servidores y entornos compartidos.

## El Escenario de Ataque

Imagina que tienes un servidor web donde un usuario (o un proceso comprometido) tiene permiso de escritura en la carpeta `__pycache__`, pero NO en los archivos `.py` fuente.

1.  **El archivo fuente:** `login.py` (Seguro, revisado por ti).
2.  **El ataque:** El atacante crea un `login.cpython-312.pyc` malicioso que contiene una puerta trasera, y lo coloca en `__pycache__`.
3.  **El truco:** El atacante modifica el **Timestamp** dentro del `.pyc` para que coincida exactamente con la fecha de modificación de `login.py`.

## ¿Qué hace Python?

Cuando Python importa `login`, ve que existe un `.pyc`.
1.  Lee el Timestamp del `.pyc`.
2.  Lo compara con el Timestamp del `.py`.
3.  **¡Coinciden!** Python asume que el `.pyc` es válido y lo ejecuta, ignorando completamente el contenido real de `login.py`.

Resultado: Estás ejecutando código que no ves.

## La Solución: PEP 552

Para mitigar esto, Python introdujo la validación basada en Hash (en lugar de Timestamp).

Si compilas tus archivos usando la opción `--invalidation-mode=checked-hash`:

```bash
python -m py_compile --invalidation-mode=checked-hash login.py
```

Python incrustará un **Hash SIP** del contenido del archivo fuente dentro del `.pyc`.
Al importar, Python recalculará el hash del `.py` y lo comparará. Si el atacante cambia el `.pyc` pero no puede modificar el `.py` (para que coincida el hash), Python detectará la discrepancia y recompilará el archivo legítimo.
