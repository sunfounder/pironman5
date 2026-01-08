#!/bin/bash

set -euo pipefail
trap 'echo "Error occurred. Exiting..." >&2; exit 1' ERR

echo "=== LGPIO Installation Script (Universal Compatibility) ==="

# 1. Check for root privileges
if [ "$EUID" -ne 0 ]; then
  echo "Error: Please run as root (use sudo)"
  exit 1
fi

# 2. Try to install via package manager first (fastest & cleanest)
echo "- Attempting to install via apt..."
if apt-get install -y liblgpio-dev python3-lgpio 2>/dev/null; then
    echo "✓ LGPIO installed successfully via apt."
    exit 0
else
    echo "! apt package not found. Proceeding with source compilation."
fi

# 3. Install build dependencies
echo "- Installing build dependencies..."
apt-get update
apt-get install -y swig python3-dev python3-setuptools unzip wget make gcc

# 4. Download and extract source
echo "- Downloading LGPIO source..."
rm -rf lg lg.zip*
wget -q http://abyz.me.uk/lg/lg.zip
unzip -q lg.zip
cd lg

# 5. Apply compatibility patches for modern GCC (GCC 14+)
echo "- Patching source and Makefile for GNU89 compatibility..."

# Modify the callback definition to accept variable arguments (...) 
# This prevents "too many arguments" errors in modern C standards
sed -i 's/typedef void (\*callbk_t) ();/typedef void (*callbk_t) (...);/' lgpio.h

# Force the Makefile to use the gnu89 standard and suppress strict type errors
# -std=gnu89: Allows old-style function declarations
# -fpermissive: Downgrades some errors to warnings
# -Wno-everything: Suppresses the flood of warnings for cleaner output
sed -i 's/^gcc/gcc -std=gnu89 -fpermissive -Wno-everything/' Makefile
sed -i 's/CFLAGS +=/CFLAGS += -std=gnu89 -fpermissive -Wno-everything /' Makefile

# 6. Compile and Install C Library
echo "- Compiling and installing C library..."
make clean || true
export CFLAGS="-std=gnu89 -fpermissive -Wno-everything"
make
make install

# 7. Update shared library cache
ldconfig

# 8. Install Python Bindings (rpi.lgpio dependency)
echo "- Installing Python bindings..."
if [ -d "PY_LGPIO" ]; then
    cd PY_LGPIO
    # Pass compatibility flags to the Python extension compiler
    export CFLAGS="-std=gnu89 -fpermissive -Wno-everything"
    python3 setup.py install
    cd ..
fi

# 9. Cleanup
echo "- Cleaning up temporary files..."
cd ..
rm -rf lg lg.zip

echo "=== LGPIO Installation Finished ==="