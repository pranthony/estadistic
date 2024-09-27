La Regla de Sturges es una fórmula utilizada para determinar el número óptimo de clases en las que se debe dividir un conjunto de datos para construir un histograma. La fórmula es:

$$ k = 1 + \log_{2}(n) $$

donde ( k ) es el número de clases y ( n ) es el número de observaciones o datos.

Vamos a interpretar detalladamente la demostración que lleva a esta fórmula.

Paso 1: Combinaciones
La demostración comienza con la fórmula de combinaciones:

$$ C_n^{m} = \frac{m!}{(m-n)! \cdot n!} $$

Paso 2: Suma de combinaciones
Luego, se suma una serie de combinaciones:

$$ n = \sum_{i=0}^{k-1} C_i^{k-1} = C_0^{k-1} + C_1^{k-1} + C_2^{k-1} \dots C_{k-1}^{k-1} $$

Paso 3: Evaluación de cada término de la suma
Cada término de la suma se evalúa utilizando la fórmula de combinaciones:

$$ n = \frac{(k-1)!}{(k-1-0)! \cdot 0!} + \frac{(k-1) \cdot (k-2)!}{(k-1-1)! \cdot 1!} + \frac{(k-1)\cdot (k-2)\cdot (k-3)!}{(k-1-2)! \cdot 2!}+ \dots +\frac{(k-1)!}{(k-1)!} $$

Paso 4: Simplificación de términos
Simplificando los términos de la suma:

$$ n = (1) + (k-1) + \frac{(k-1)\cdot(k-2)}{2} + \frac{(k-1)\cdot(k-2)\cdot(k-3)}{3!} + \dots + \frac{(k-1)!}{(k-1)!} $$

Paso 5: Evaluación para valores específicos de ( k )
Evaluamos la suma para algunos valores específicos de ( k ):

Para ( k = 1 ): $$ n = 1 = 2^{1-1} $$
Para ( k = 2 ): $$ n = 1 + 1 = 2 = 2^{2-1} $$
Para ( k = 3 ): $$ n = 1 + 2 + 1 = 4 = 2^{3-1} $$
Para ( k = 4 ): $$ n = 1 + 3 + 3 + 1 = 8 = 2^{4-1} $$
Paso 6: Generalización
Observamos un patrón en los resultados, que se puede generalizar como:

$$ n = 2^{k-1} $$

Paso 7: Despeje de ( k )
Para encontrar ( k ), tomamos el logaritmo base 2 de ambos lados de la ecuación:

$$ \log_{2}(n) = \log_{2}(2^{k-1}) $$

Usando las propiedades de los logaritmos:

$$ \log_{2}(n) = k - 1 $$

Paso 8: Solución final
Finalmente, despejamos ( k ):

$$ k = 1 + \log_{2}(n) $$

Conclusión
Hemos derivado la fórmula de la Regla de Sturges, que nos permite calcular el número óptimo de clases ( k ) para un histograma dado el número de observaciones ( n ). Esta fórmula es útil para construir histogramas que representen adecuadamente la distribución de los datos.