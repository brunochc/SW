# Análisis Profundo de Bytecode

Aquí es donde nos ponemos la bata de laboratorio y diseccionamos los archivos binarios.

## Contenido

1.  **[Anatomía de un .pyc](./estructura-pyc.md)**
    *   Análisis detallado usando `base_command.pyc` como ejemplo.
    *   Entendiendo el Header y el Body.
    *   Por qué el tamaño del archivo es mayor que el bytecode.

2.  **[Versiones y Magic Numbers](./versiones-python.md)**
    *   Cómo identificar la versión de Python de un `.pyc`.
    *   Por qué cambia el formato entre versiones.
    *   Builds reproducibles (PEP 552).

## Herramientas recomendadas
Para seguir esta sección, te recomendamos usar el script `scripts-utiles/analizador_basico.py` que incluimos en este repositorio.
