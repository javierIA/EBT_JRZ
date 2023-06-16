# 13 mandamientos PEP8

- 1. No codificarás en tinieblas; utiliza la sangría de cuatro espacios para guiar tus bloques de código.
- 2. Santifica la longitud de tus líneas, no permitas que excedan los límites establecidos.
- 3. Amarás a tus variables y les darás nombres descriptivos y en minúsculas, separando las palabras con guiones bajos.
- 4. No codificarás en vanidad; utiliza espacios en blanco para separar tus operadores y mejorar la legibilidad.
- 5. Benditos sean los comentarios que aclaren el propósito de tu código y guíen a los perdidos en su comprensión.
- 6. Honra tus importaciones y organízalas en un orden lógico, para que el poder de los módulos esté a tu disposición.
- 7. No robarás nombres sagrados de otros módulos; respeta su existencia y evita la confusión entre los fieles.
- 8. No levantarás falsos testimonios; utiliza guiones bajos para separar palabras en tus nombres de variables.
- 9. Guarda tus clases y métodos, y dales nombres que reflejen su propósito divino y su funcionalidad clara.
- 10. No codificarás con avaricia; deja espacios alrededor de tus operadores para mantener una armonía visual.
- 11. No te olvides de dar gracias a tus bibliotecas y módulos, importándolos con gratitud en el orden apropiado.
- 12. No codificarás en silencio; explícita será mejor que implícita, y la claridad vencerá a la ambigüedad.
- 13. No cometerás el pecado de descuidar el estilo; sigue estas convenciones para que tu código sea legible y apreciado.
¡Por supuesto! Aquí tienes ejemplos con código que muestra la diferencia entre seguir y no seguir las convenciones de estilo de PEP-8, basado en los 13 mandamientos anteriores:

1. Ejemplo del mandamiento: "Honra la sangría y mantén tus bloques de código alineados."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
def mi_funcion():
   if condicion:
      print("Bloque anidado")
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
def mi_funcion():
    if condicion:
        print("Bloque anidado")
```

2. Ejemplo del mandamiento: "No codificarás en vanidad; utiliza espacios en blanco para separar tus operadores y mejorar la legibilidad."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
resultado=variable1+variable2

# Sin seguir PEP-8
resultado =  variable1   +  variable2
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
resultado = variable1 + variable2
```

3. Ejemplo del mandamiento: "Amarás a tus variables y les darás nombres descriptivos y en minúsculas, separando las palabras con guiones bajos."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
MI_VARIABLE = 10

# Sin seguir PEP-8
x = 5
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
mi_variable = 10

# Siguiendo PEP-8
x = 5
```

4. Ejemplo del mandamiento: "Benditos sean los comentarios que aclaren el propósito de tu código y guíen a los perdidos en su comprensión."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
# Establecer valor a la variable
x = 10
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
# Establece el valor de la variable x
x = 10
```

5. Ejemplo del mandamiento: "Honra tus importaciones y organízalas en un orden lógico, para que el poder de los módulos esté a tu disposición."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
import sys
import os
import numpy as np
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
import os
import sys
import numpy as np
```

6. Ejemplo del mandamiento: "No levantarás falsos testimonios; utiliza guiones bajos para separar palabras en tus nombres de variables."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
nombreCompleto = "John Doe"
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
nombre_completo = "John Doe"
```

7. Ejemplo del mandamiento: "No te olvides de dar gracias a tus bibliotecas y módulos, importándolos con gratitud en el orden apropiado."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
import os
import numpy as np
import mi_modulo
import sys


```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
import os
import sys
import numpy as np
import mi_modulo
```

8. Ejemplo del mandamiento: "No codificarás en silencio; explícita será mejor que implícita, y la claridad vencerá a la ambigüedad."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
# Suma dos números
def suma(a, b):
    return a + b
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
def suma(a, b):
    """Suma dos números."""
    return a + b
```

9. Ejemplo del mandamiento: "No cometerás el pecado de descuidar el estilo; sigue estas convenciones para que tu código sea legible y apreciado."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
resultado=10*(2+3)

# Sin seguir PEP-8
Resultado= 10 * ( 2 + 3 )
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
resultado = 10 * (2 + 3)
```

10. Ejemplo del mandamiento: "Guarda tus clases y métodos, y dales nombres que reflejen su propósito divino y su funcionalidad clara."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
class Miclase:
    def mimetodo(self):
        pass
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
class MiClase:
    def mi_metodo(self):
        pass
```

11. Ejemplo del mandamiento: "No codificarás en tinieblas; utiliza la sangría de cuatro espacios para guiar tus bloques de código."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
if condicion == True:
    pass
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
if condicion:
    pass
```

12. Ejemplo del mandamiento: "Santifica la longitud de tus líneas, no permitas que excedan los límites establecidos."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
resultado = variable1 + variable2 + variable3 + variable4
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
resultado = variable1 + variable2 + \
            variable3 + variable4
```

13. Ejemplo del mandamiento: "No codificarás con avaricia; deja espacios alrededor de tus operadores para mantener una armonía visual."

Sin seguir PEP-8:
```python
# Sin seguir PEP-8
resultado=10*(2+3)
```

Siguiendo PEP-8:
```python
# Siguiendo PEP-8
resultado = 10 * (2 + 3)
```
