# El Mito de la Protección con .pyc

Una creencia común entre desarrolladores nuevos en Python es:
> *"Si borro los archivos .py y solo entrego los .pyc, nadie podrá robar mi código."*

**Esto es FALSO.**

## La Realidad: Ingeniería Inversa Trivial

Como vimos en la sección de Herramientas, los archivos `.pyc` contienen una representación muy fiel de tu código fuente.

### ¿Qué se recupera?
*   Nombres de variables y funciones exactos.
*   Lógica de control de flujo completa.
*   Strings y constantes literales (incluyendo contraseñas hardcodeadas).

### ¿Qué se pierde?
*   Comentarios ( `# esto hace x` ).
*   Formato (espacios, saltos de línea originales).

Para una computadora (y para un humano motivado), la versión decompilada es funcionalmente idéntica a la original.

## Ejemplo Teórico

**Original:**
```python
def verificar_acceso(password):
    # Clave secreta de la empresa
    if password == "SuperSecreto123":
        return True
    return False
```

**Decompilado (desde .pyc):**
```python
def verificar_acceso(password):
    if password == 'SuperSecreto123':
        return True
    return False
```

Como ves, el secreto `"SuperSecreto123"` está expuesto en texto plano dentro del `.pyc`.

## Conclusión
Nunca confíes en la compilación a bytecode como mecanismo de seguridad para ocultar secretos o lógica propietaria sensible.
