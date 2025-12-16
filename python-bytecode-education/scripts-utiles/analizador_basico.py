#!/usr/bin/env python3
"""
Analizador básico de archivos .pyc
"""

import struct
import marshal
import dis
import sys
import argparse
from pathlib import Path

# Magic numbers para diferentes versiones de Python
PYTHON_VERSIONS = {
    b'\x6f\x0d\x0d\x0a': 'Python 3.12',
    b'\x6e\x0d\x0d\x0a': 'Python 3.11',
    b'\x6d\x0d\x0d\x0a': 'Python 3.10',
    b'\x6c\x0d\x0d\x0a': 'Python 3.9',
    b'\x6b\x0d\x0d\x0a': 'Python 3.8',
    b'\x63\x0d\x0d\x0a': 'Python 3.7',
    b'\x42\x0d\x0d\x0a': 'Python 3.6',
}

def analizar_pyc(archivo_pyc, mostrar_bytecode=False):
    """
    Analiza un archivo .pyc y muestra información básica
    """
    try:
        with open(archivo_pyc, 'rb') as f:
            # Leer magic number (4 bytes)
            magic = f.read(4)
            
            # Leer timestamp (4 bytes, little-endian)
            timestamp_bytes = f.read(4)
            if len(timestamp_bytes) == 4:
                timestamp = struct.unpack('<I', timestamp_bytes)[0]
            else:
                timestamp = 0
            
            # El resto es el objeto de código marshalled
            try:
                # Skip header padding if necessary (some versions have more header)
                # Python 3.7+ has 16 bytes header (magic 4 + flags 4 + timestamp 4 + size 4)
                # But let's try standard load first or adjust
                f.seek(16) 
                codigo = marshal.load(f)
            except Exception:
                # Fallback for older versions or if seek failed
                f.seek(8)
                try:
                    codigo = marshal.load(f)
                except Exception:
                     # Fallback for very old or different structure
                    f.seek(12) # Python 3.3+
                    codigo = marshal.load(f)

        
        print("🔍 ANÁLISIS DE ARCHIVO .PYC")
        print("=" * 60)
        
        # Información del archivo
        print(f"\n📁 Archivo: {archivo_pyc}")
        print(f"📏 Tamaño: {Path(archivo_pyc).stat().st_size} bytes")
        
        # Versión de Python
        version = PYTHON_VERSIONS.get(magic, f'Desconocida: {magic.hex()}')
        print(f"🐍 Versión Python: {version}")
        
        # Timestamp
        from datetime import datetime
        if timestamp > 0:
            fecha = datetime.fromtimestamp(timestamp)
            print(f"🕐 Compilado: {fecha.strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("🕐 Timestamp: (no disponible en este formato)")
        
        # Información del objeto de código
        print(f"\n📦 Objeto de código:")
        print(f"   Nombre: {codigo.co_name}")
        print(f"   Argumentos: {codigo.co_argcount}")
        try:
            print(f"   Variables locales: {codigo.co_nlocals}")
        except AttributeError:
             pass
        print(f"   Tamaño pila: {codigo.co_stacksize}")
        print(f"   Flags: {codigo.co_flags}")
        
        # Mostrar bytecode si se solicita
        if mostrar_bytecode:
            print(f"\n💻 Bytecode desensamblado:")
            print("-" * 40)
            dis.dis(codigo)
        
        # Estadísticas básicas
        print(f"\n📊 Estadísticas:")
        print(f"   Bytes de bytecode: {len(codigo.co_code)}")
        print(f"   Constantes: {len(codigo.co_consts)}")
        print(f"   Nombres: {len(codigo.co_names)}")
        print(f"   Variables: {len(codigo.co_varnames)}")
        
        print("\n" + "=" * 60)
        print("✅ Análisis completado")
        
    except Exception as e:
        print(f"❌ Error analizando archivo: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Analizador de archivos .pyc')
    parser.add_argument('archivo', help='Archivo .pyc a analizar')
    parser.add_argument('-d', '--dis', action='store_true', 
                       help='Mostrar bytecode desensamblado')
    parser.add_argument('-o', '--output', help='Archivo de salida')
    
    args = parser.parse_args()
    
    # Verificar que el archivo existe
    if not Path(args.archivo).exists():
        print(f"Error: El archivo {args.archivo} no existe")
        sys.exit(1)
    
    # Redirigir salida si se especificó archivo de salida
    if args.output:
        with open(args.output, 'w') as f:
            old_stdout = sys.stdout
            sys.stdout = f
            analizar_pyc(args.archivo, args.dis)
            sys.stdout = old_stdout
        print(f"✓ Reporte guardado en: {args.output}")
    else:
        analizar_pyc(args.archivo, args.dis)

if __name__ == "__main__":
    main()
