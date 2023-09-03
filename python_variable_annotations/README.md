# Variable Annotations
Se refieren a la capacidad de agregar metadatos o información adicional a las variables, especialmente en lo que respecta a su tipo de datos. Esta característica se introdujo en Python 3.6 como parte de las "Anotaciones de tipo" y se utiliza principalmente para proporcionar información sobre el tipo de datos que se espera que una variable contenga. Sin embargo, es importante destacar que estas anotaciones no afectan el comportamiento en tiempo de ejecución del programa y son opcionales.
Las anotaciones de variables se realizan utilizando el operador de dos puntos (:) después del nombre de la variable, seguido del tipo de datos esperado.

```python
import typing
```

La biblioteca typing no afecta el comportamiento en tiempo de ejecución de un programa; en cambio, se utiliza principalmente para mejorar la legibilidad del código y para proporcionar información sobre los tipos de datos esperados.

Algunos de los elementos más comunes proporcionados por la biblioteca typing incluyen:

Annotations: Permite anotar variables, argumentos de funciones y valores de retorno de funciones con información sobre los tipos de datos esperados. Esto ayuda a los desarrolladores a comprender mejor el código y puede ser utilizado por herramientas externas para realizar verificaciones de tipos estáticos.

Tipos Compuestos: Ofrece tipos compuestos como List, Tuple, Dict, Set, Union, Optional, entre otros, que pueden ser útiles para describir estructuras de datos complejas y argumentos de funciones.

Callable: Proporciona el tipo Callable para anotar funciones y objetos que pueden ser llamados como funciones. Esto ayuda a especificar los tipos de argumentos y valores de retorno esperados para funciones.

Type Aliases: Permite crear alias para tipos complejos o nombres de tipo largos, lo que hace que las anotaciones de tipo sean más legibles.

Verificación de Tipos: Aunque Python es un lenguaje de tipado dinámico, algunas herramientas externas como MyPy pueden utilizar las anotaciones de tipo en combinación con la biblioteca typing para realizar verificaciones estáticas de tipos en el código.

