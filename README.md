# Actividad-02-Python_y_VS

### Objetivo

El alumno desarrollará soluciones utilizando el lenguaje de programación *Python* usando condiciones, ciclos y funciones.

### Instrucciones

1. Haz lo siguiente usando el lenguaje de programación *Python*:
    1. Programa 3 funciones para calcular el área del las figuras: cuadrado, triángulo y círculo. Usa input() para pedir al usuario las variables para calcular el área de cada figura. Una función por figura. Prueba las funciones y toma capturas de pantalla de la salida de las pruebas realizadas a las funciones.
    2. Haz un script para pedirle al usuario el día y mes de nacimiento, y de acuerdo a su día y mes de nacimiento mostrar en pantalla su signo zodiacal. El día debe ser leído como entero (1-31) al igual el mes (1-12). No validar la entrada, suponemos que el usuario siempre ingresará día y mes correctos. Prueba tu script tres veces con diferentes fechas  y toma capturas de pantalla de estas pruebas.
    3. Haz un script que haga el cálculo del [Número e](https://es.wikipedia.org/wiki/Número_e): $e = \displaystyle \sum_{n=0}^\infty \frac{1}{n!}$, donde $\infty$ es el límite del ciclo, por lo que entre mayor sea el límite del ciclo, mayor precisión del número $e$. Recomiendo crear una función para calcular el factorial y hacer algo así:
        
        ```python
        limite = 4
        n = 0
        e = 0
        while n < limite:
        	e += 1/fatorial(n) # se llama a la función factorial creada por ti
        	n = n + 1
        ```
        
        Prueba tu script con tres diferentes límites en donde demuestres con capturas de pantalla que entre más grande el límite es más preciso el valor del [Número e](https://es.wikipedia.org/wiki/Número_e).
