# Investigación: Cifrado de Vigenère

## 1. Introducción

El cifrado de Vigenère es uno de los sistemas de cifrado clásico más importantes en la historia de la criptografía. Fue creado con el objetivo de superar las debilidades de los cifrados por sustitución simple, como el cifrado César, los cuales podían ser fácilmente vulnerados mediante análisis de frecuencia. El uso de una clave secreta que modifica el patrón de cifrado en cada carácter permitió aumentar significativamente el nivel de seguridad de los mensajes.

Este método fue considerado durante siglos como un cifrado prácticamente indescifrable y representa un paso fundamental hacia los sistemas criptográficos modernos.

---

## 2. Origen e historia

El cifrado de Vigenère fue descrito formalmente en 1586 por el criptógrafo francés Blaise de Vigenère, aunque su base fue desarrollada previamente por otros criptógrafos. Debido a su resistencia frente a los ataques conocidos de la época, fue ampliamente utilizado en comunicaciones diplomáticas y militares.

Durante más de 300 años, el cifrado de Vigenère se mantuvo como uno de los métodos más seguros de cifrado hasta que en el siglo XIX fue vulnerado mediante técnicas matemáticas, como el análisis de patrones repetidos y el estudio de frecuencias.

---

## 3. ¿Qué es el cifrado de Vigenère?

El cifrado de Vigenère es un cifrado polialfabético, lo que significa que utiliza múltiples alfabetos para cifrar un mensaje. En lugar de usar un solo desplazamiento para todas las letras, como en el cifrado César, este método usa una clave que determina un desplazamiento distinto para cada carácter del mensaje.

De esta manera, una misma letra puede cifrarse de diferentes formas, lo que dificulta enormemente el descifrado sin conocer la clave.

---

## 4. Funcionamiento del cifrado

El proceso de cifrado se basa en una tabla llamada tabla de Vigenère, que contiene el alfabeto desplazado en cada fila.

El procedimiento es el siguiente:

1. Se elige una palabra clave.
2. La clave se repite hasta tener la misma longitud que el mensaje.
3. Cada letra del mensaje se combina con la letra correspondiente de la clave.
4. La intersección de ambas letras en la tabla determina el carácter cifrado.

Este proceso se repite para todo el mensaje.

---

## 5. Ejemplo de aplicación

Mensaje original: ATAQUE
Clave: CLAVE

Como la clave tiene menos caracteres que el mensaje original, se repiten caracteres

ATAQUE
CLAVECL


Proceso de cifrado:

| Texto | A | T | A | Q | U | E |
|-------|---|---|---|---|---|---|
| Clave | C | L | A | V | E | C |
| Cifrado | C | E | A | L | Y | G |

Resultado cifrado: CEALYG


Este texto solo puede ser descifrado correctamente por quien conozca la clave utilizada.

---

## 6. Razones para elegir el cifrado de Vigenère

Se eligió el cifrado de Vigenère porque representa uno de los avances más importantes en la historia de la criptografía. Introduce el concepto de una clave dinámica y demuestra cómo un sistema puede volverse mucho más seguro sin necesidad de tecnología avanzada.

Además, es un cifrado ideal para fines educativos, ya que permite comprender los principios básicos de la criptografía moderna.

---

## 7. Ventajas

- Utiliza una clave secreta que protege la información.
- Una misma letra no se cifra siempre de la misma manera.
- Es mucho más seguro que los cifrados por sustitución simple.
- Fue considerado irrompible durante siglos.
- Es fácil de implementar en programas informáticos.

---

## 8. Vulnerabilidades

- Si la clave es corta, puede ser descubierta.
- Es vulnerable al ataque de Kasiski, que permite encontrar la longitud de la clave.
- El análisis estadístico puede romperlo con suficiente texto cifrado.
- No es seguro frente a los métodos criptográficos modernos.

---

## 9. Razón de elección

Elegí este cifrado pues utiliza métodos bastante interesantes para cifrar la información y durante mucho tiempo se le considero indescifrable.

---

## 10. Referencias

- Wikipedia. *Cifrado de Vigenère*.  
  https://es.wikipedia.org/wiki/Cifrado_de_Vigen%C3%A8re  
- Encyclopaedia Britannica. *Vigenère cipher*.  
  https://www.britannica.com/topic/Vigenere-cipher  
- Khan Academy. *Cryptography*.  
  https://www.khanacademy.org/computing/computer-science/cryptography


