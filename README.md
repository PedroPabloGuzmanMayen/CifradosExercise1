# Ejercicio de Criptografía

Un conjunto completo de herramientas criptográficas que incluye cifrados históricos, conversiones de codificación y generación de claves. Este proyecto implementa desde métodos clásicos como César y Vigenère hasta operaciones modernas con XOR y Base64.

---

## 📚 Tabla de Contenidos

- [Características](#-características)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Instalación](#-instalación)
- [Uso](#-uso)
  - [Cifrados Históricos](#cifrados-históricos)
  - [Conversiones de Codificación](#conversiones-de-codificación)
  - [Generación de Claves](#generación-de-claves)
- [Ejemplos](#-ejemplos)
- [Documentación](#-documentación)
- [Requisitos](#-requisitos)
- [Contribuir](#-contribuir)

---

## Características

### Cifrados Históricos
- **Cifrado César**: Cifrado por desplazamiento clásico
- **ROT13**: Variante específica del cifrado César
- **Cifrado Vigenère**: Cifrado polialfabético con clave
- **Análisis de Frecuencia**: Herramienta para criptoanálisis

### Conversiones de Codificación
- Conversión ASCII ↔ Binario
- Conversión Binario ↔ Base64
- Conversión Base64 → ASCII (vía binario)
- Operaciones XOR sobre cadenas binarias

### Generación de Claves
- Generación de claves aleatorias
- Cifrado XOR dinámico (clave del tamaño del mensaje)
- Cifrado XOR estático (clave repetida)

---

##  Estructura del Proyecto

```
.
├── Cryptography/
│   ├── Investigación.md          # Documentación sobre el cifrado Vigenère
│   ├── utils.py                  # Funciones auxiliares
│   ├── binario_ascci.py          # Conversión ASCII → Binario
│   ├── binary_ascii.py           # Conversión Binario → ASCII
│   ├── binary_to_base64.py       # Conversión Binario → Base64
│   ├── base64_binary.py          # Conversión Base64 → Binario
│   ├── base64_ascii.py           # Conversión Base64 → ASCII
│   └── xor.py                    # Operación XOR binaria
│
├── Historical_Ciphers/
│   ├── caesar.py                 # Cifrado César
│   ├── rot13.py                  # Cifrado ROT13
│   ├── vigenere.py              # Cifrado Vigenère
│   └── frequency.py              # Análisis de frecuencia
│
└── Keys/
    ├── dynamic_key.py            # Generación y cifrado con claves
    ├── xor.py                    # Operación XOR
    ├── binario_ascci.py          # Conversión ASCII → Binario
    ├── binary_ascii.py           # Conversión Binario → ASCII
    └── utils.py                  # Funciones auxiliares
```

---

## Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-proyecto>
   ```

2. **Instalar dependencias**
   ```bash
   pip install matplotlib
   ```

3. **Verificar instalación**
   ```bash
   python Historical_Ciphers/caesar.py
   ```

---

## Uso

### Cifrados Históricos

#### Cifrado César
```bash
cd Historical_Ciphers
python caesar.py
```

**Funciones disponibles:**
```python
from caesar import cipher_caesar, decipher_caesar

# Cifrar mensaje
mensaje_cifrado = cipher_caesar("HOLA MUNDO", 3)
# Resultado: "KROD PXQGR"

# Descifrar mensaje
mensaje_original = decipher_caesar("KROD PXQGR", 3)
# Resultado: "HOLA MUNDO"
```

#### Cifrado ROT13
```bash
python rot13.py
```

**Funciones disponibles:**
```python
from rot13 import cipher_rot13, decihper_rot13

# Cifrar/Descifrar (ROT13 es simétrico)
cifrado = cipher_rot13("MENSAJE SECRETO")
original = decihper_rot13(cifrado)
```

#### Cifrado Vigenère
```bash
python vigenere.py
```

**Funciones disponibles:**
```python
from vigenere import cipher_vigenere, decipher_vigenere

# Cifrar con clave
mensaje_cifrado = cipher_vigenere("ATAQUE", "CLAVE")
# Resultado: "CEALYG"

# Descifrar con clave
mensaje_original = decipher_vigenere("CEALYG", "CLAVE")
# Resultado: "ATAQUE"
```

#### Análisis de Frecuencia
```bash
python frequency.py
```

**Funcionalidad:**
- Analiza la frecuencia de letras en un mensaje
- Genera un gráfico de barras (guardado en `./images/`)
- Útil para criptoanálisis de cifrados por sustitución

### Conversiones de Codificación

#### ASCII ↔ Binario
```bash
cd Cryptography
python binario_ascci.py  # ASCII → Binario
python binary_ascii.py   # Binario → ASCII
```

#### Binario ↔ Base64
```bash
python binary_to_base64.py  # Binario → Base64
python base64_binary.py     # Base64 → Binario
```

#### Base64 → ASCII
```bash
python base64_ascii.py
```

#### Operación XOR
```bash
python xor.py
```

**Funciones disponibles:**
```python
from xor import binary_xor

# XOR entre dos cadenas binarias
resultado = binary_xor("11010110", "10101100")
# Resultado: "01111010"
```

### Generación de Claves

```bash
cd Keys
python dynamic_key.py
```

**Opciones disponibles:**
1. **Cifrado dinámico**: Genera una clave del mismo tamaño que el mensaje
2. **Cifrado estático**: Usa una clave de tamaño fijo que se repite

**Funciones disponibles:**
```python
from dynamic_key import generate_key, dynamic_cipher, static_cipher

# Generar clave aleatoria
clave = generate_key(16)  # Clave de 16 caracteres

# Cifrado dinámico (clave = tamaño del mensaje)
cifrado = dynamic_cipher("MENSAJE SECRETO")

# Cifrado estático (clave de tamaño fijo)
cifrado = static_cipher("MENSAJE SECRETO", 8)
```

---

## Ejemplos

### Ejemplo 1: Cifrado César completo
```python
from Historical_Ciphers.caesar import cipher_caesar, decipher_caesar

mensaje = "¡Hola Mundo! Este es un mensaje secreto."
shift = 5

# Cifrar
cifrado = cipher_caesar(mensaje, shift)
print(f"Cifrado: {cifrado}")
# Salida: ¡Mtrñ Rzsiñ! Jxyj jx zs rjsxfoj xjhwjyt.

# Descifrar
descifrado = decipher_caesar(cifrado, shift)
print(f"Descifrado: {descifrado}")
# Salida: ¡Hola Mundo! Este es un mensaje secreto.
```

### Ejemplo 2: Pipeline de conversión completo
```python
from Cryptography.binario_ascci import ascii_binary
from Cryptography.binary_to_base64 import binary_to_base64
from Cryptography.base64_ascii import base64_ascii

mensaje = "Hola"

# ASCII → Binario
binario = ascii_binary(mensaje)
print(f"Binario: {binario}")

# Binario → Base64
base64 = binary_to_base64(binario)
print(f"Base64: {base64}")

# Base64 → ASCII (vía binario)
original = base64_ascii(base64)
print(f"Original: {original}")
```

### Ejemplo 3: Cifrado Vigenère
```python
from Historical_Ciphers.vigenere import cipher_vigenere, decipher_vigenere

mensaje = "DEFIENDE EL CASTILLO ORIENTAL"
clave = "FORTALEZA"

# Cifrar
cifrado = cipher_vigenere(mensaje, clave)
print(f"Mensaje cifrado: {cifrado}")

# Descifrar
original = decipher_vigenere(cifrado, clave)
print(f"Mensaje original: {original}")
```

### Ejemplo 4: Análisis de frecuencia
```python
from Historical_Ciphers.frequency import frequency_analysis

mensaje_cifrado = "KROD PXQGR JX ZQ RJQXÑLJ HLIGÑNR"

# Analizar frecuencias
frequency_analysis(mensaje_cifrado)
# Genera un gráfico y muestra la tabla de frecuencias
```

---

## Documentación

### Cifrado de Vigenère

Para información detallada sobre el cifrado de Vigenère, consulta el documento [Investigación.md](Cryptography/Investigación.md), que incluye:

- Historia y origen
- Funcionamiento detallado
- Ejemplos prácticos
- Ventajas y vulnerabilidades
- Referencias adicionales

### Funciones Auxiliares

El módulo `utils.py` contiene funciones fundamentales:

- `number_to_binary(number)`: Convierte decimal a binario
- `cast_binary(base, bin_number)`: Agrega padding a números binarios
- `binary_string_to_decimal(binary)`: Convierte binario a decimal
- `divide_binary_string(binary, division)`: Divide cadenas binarias en fragmentos

---

## Requisitos

- Python 3.6+
- matplotlib (para análisis de frecuencia)

```bash
pip install matplotlib
```

---

## Características Técnicas

### Alfabeto Español
Los cifrados históricos utilizan el alfabeto español completo:
```python
ALPHABET = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'  # 27 letras
```

### Alfabeto Base64
```python
BASE64_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
```

### Manejo de Caracteres
- Los cifrados preservan espacios y caracteres especiales
- Mantienen mayúsculas y minúsculas
- Solo cifran caracteres alfabéticos

---


## 📝 Notas Importantes

### Seguridad
⚠️ **Advertencia**: Los cifrados implementados en este proyecto son de naturaleza educativa. Los métodos históricos (César, Vigenère, ROT13) NO son seguros para proteger información sensible en la actualidad.

### Uso Educativo
Este proyecto está diseñado para:
- Aprender conceptos básicos de criptografía
- Entender la evolución de los sistemas de cifrado
- Practicar conversiones entre diferentes sistemas de numeración
- Experimentar con técnicas de criptoanálisis

---

## Referencias

- [Cifrado de Vigenère - Wikipedia](https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re)
- [Vigenère cipher - Britannica](https://www.britannica.com/topic/Vigenere-cipher)
- [Cryptography - Khan Academy](https://www.khanacademy.org/computing/computer-science/cryptography)

---

**Desarrollado con fines educativos** 