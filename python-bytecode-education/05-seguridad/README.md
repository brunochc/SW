# Seguridad y Bytecode

Entender el bytecode es vital tanto para proteger tu código como para protegerte de ataques.

## Contenido

1.  **[Mitos de Protección](./mitos-proteccion.md)**
    *   Por qué borrar los `.py` no te salva.
    *   Ejemplo de recuperación de secretos.

2.  **[Ofuscación Real](./ofuscacion.md)**
    *   Qué hace `python -OO`.
    *   Herramientas avanzadas: PyArmor, Cython, Nuitka.

3.  **[Inyección de Bytecode](./inyeccion-bytecode.md)**
    *   Cómo un atacante puede engañar a Python para ejecutar código malicioso.
    *   El problema de confiar en los Timestamps.
    *   La solución: Hash-based .pyc (PEP 552).
