#!/usr/bin/env python3
"""
Demo básico de generación y análisis de bytecode
"""

import dis
import py_compile
import os
import tempfile

def crear_ejemplo():
    """Crea un ejemplo simple y muestra su bytecode"""
    
    # Código fuente de ejemplo
    codigo_fuente = '''
def factorial(n):
    """Calcula factorial recursivamente"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def factorial_iterativo(n):
    """Calcula factorial iterativamente"""
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

# Uso
if __name__ == "__main__":
    print(f"Factorial recursivo de 5: {factorial(5)}")
    print(f"Factorial iterativo de 5: {factorial_iterativo(5)}")
    '''
    
    # Guardar en archivo temporal
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(codigo_fuente)
        archivo_temp = f.name
    
    print("=" * 60)
    print("📄 ANÁLISIS DE BYTECODE - DEMO")
    print("=" * 60)
    
    # 1. Compilar a bytecode
    print("\n1️⃣  Compilando archivo...")
    archivo_pyc = archivo_temp + 'c'
    py_compile.compile(archivo_temp, cfile=archivo_pyc)
    print(f"   Archivo fuente: {archivo_temp}")
    print(f"   Bytecode generado: {archivo_pyc}")
    
    # 2. Mostrar bytecode de funciones
    print("\n2️⃣  Bytecode de factorial() recursivo:")
    print("-" * 40)
    
    # Ejecutar el código para definir las funciones
    ns = {}
    with open(archivo_temp) as f:
        exec(f.read(), ns)
    
    # Analizar bytecode de factorial recursivo
    print("factorial (recursivo):")
    dis.dis(ns['factorial'])
    
    print("\n3️⃣  Bytecode de factorial_iterativo():")
    print("-" * 40)
    print("factorial_iterativo:")
    dis.dis(ns['factorial_iterativo'])
    
    # 3. Comparar tamaños de bytecode
    print("\n4️⃣  Comparación de tamaños:")
    size_recursivo = len(dis.Bytecode(ns['factorial']).codeobj.co_code)
    size_iterativo = len(dis.Bytecode(ns['factorial_iterativo']).codeobj.co_code)
    
    print(f"   Recursivo: {size_recursivo} bytes")
    print(f"   Iterativo: {size_iterativo} bytes")
    print(f"   Diferencia: {abs(size_recursivo - size_iterativo)} bytes")
    
    # 4. Ejecutar para demostrar funcionamiento
    print("\n5️⃣  Ejecutando funciones...")
    print(f"   factorial(5) = {ns['factorial'](5)}")
    print(f"   factorial_iterativo(5) = {ns['factorial_iterativo'](5)}")
    
    # Limpiar
    os.unlink(archivo_temp)
    if os.path.exists(archivo_pyc):
        os.unlink(archivo_pyc)
    
    print("\n" + "=" * 60)
    print("✅ Demo completado")
    print("=" * 60)

if __name__ == "__main__":
    crear_ejemplo()
