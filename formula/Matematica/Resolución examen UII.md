<div align="center">

#### MATEMÁTICA II

#### EVALUACIÓN DE COMPETENCIAS

#### SEGUNDA UNIDAD

</div>

**Apellidos y Nombres:** Palomino Ricaldi Antony

1. En una empresa textil de Huánuco dedicada a la confección de polos. Se venden 200 polos cuando el precio es de S/ 40 y 160 cuando el precio es de S/ 20.

a) Determina la ecuación de oferta.  

> [!NOTE]
> $m=y_2-y_1/x_2-x_1$

<div align="center">

| Q | P |
|---|---|
|200|40 |
|160|20 |

</div>

La ecuación de oferta tiene la forma
$$y=mx +b$$

Donde $m$:

$$m = \frac{40-20}{200-160}=\frac{20}{40}=\frac{1}{2}$$

Y $b$:
$$b=40-200\cdot\frac{1}{2}=40-100=-60$$

Entonces la ecuación de la oferta es:

$$y= \frac{1}{2}x-60$$

b) Cuando el precio es de s/. 30 cuántos polos pueden vender. 

$$30=\frac{1}{2}x-60$$

$$90=\frac{1}{2}x$$

$$180=x$$


c) Si se determina vender 245 polos cuál sería el precio. 
$$y = \frac{1}{2}(245)-60$$

$$y = 122.5-60$$

$$y = 62.5$$


d) Si el precio de equilibrio del polo fuera 40 soles, qué pasaría si el precio disminuye a 30 soles

Si el precio disminuye a 30 soles la cantidad ofertada se reduce a 180 polos. Lo que ocasionaria deficit en el mercado de polos.

2. Una empresa produce y vende bicicletas en un mercado. La empresa quiere encontrar el punto de equilibrio entre la oferta y la demanda del bien dadas las siguientes ecuaciones: 

$$P_1 = 2q + 50$$

$$P_2 = -5q + 200$$

Por metodo de igualación:

$$2q + 50 = -5q + 200$$

$$7q  = 150$$

$$ q =  21$$

> [!IMPORTANT]
> Para cantidad redondear al entero proximo, debido a que no puedes producir bicicletas en fracciones (dato discreto).

Remplazando para calcular el precio

$$P_1 = 2(21) + 50$$

$$P_1 = 92$$

Halla las pendientes y determina si es perpendicular o paralelo: 
$$2x+8y-32=0 \tag{1}$$

$$-8x+2y-16=0 \tag2$$

Despejando $(1)$

$$8y=32-2x$$

$$y=\frac{32-2x}{8}$$

$$y=4-\frac{x}{4}$$

Despejando $(2)$

$$2y=16+8x $$

$$y=\frac{16+8x}{2}$$

$$y=4x+8$$

Por lo tanto no es **paralelo** por que las pendientes de $(1)$ y $(2)$ son diferentes:

4. Dado el sistema de ecuaciones: 
$$ x + 2y + z = 7 \tag1$$ 

$$ 3x + y + z = 5 \tag2$$

$$ 2x + 3y − z = 3 \tag3$$
Hallar los valores de X, Y y Z por el método de reducción.

Restando (1) - (2):

$$ x + 2y + z = 7 \tag1$$ 

$$ 3x + y + z = 5 \tag2$$

<hr>

$$ -2x + y = 2 \tag4$$

Suamndo (2) a (3):

$$ 3x + y + z = 5 \tag2$$

$$ 2x + 3y − z = 3 \tag3$$

<hr>

$$ 5x + 4y = 8 \tag5$$

Multiplicando (4) veces 4:

$$ -2x + y = 2 \tag4$$
<hr>

$$ -8x + 4y = 8 \tag6$$

Restando (5) - (6):

$$ 5x + 4y = 8 \tag5$$

$$ -8x + 4y = 8 \tag6$$

<hr>

$$ 13x = 0 \tag7$$

**Por lo que $x = 0$** 

Remplazando $x$ en (5):

$$ 5(0) + 4y = 8 \tag5$$

$$ y = 2 \tag5$$

**Por lo que $y = 2$** 

Remplazando en $x$ y $y$ en (1)

$$ 0 + 2(2) + z = 7 \tag1$$ 

$$ z = 3 \tag1$$ 

Comprobar valores $x$, $y$ y $z$ en (2)

$$ 3(0) + 2 + 3 = 5 \tag2$$

Por lo que se concluye que el consjunto solución es:

$$CS=(0, 2, 3)$$

5. Una refinería recibe de Arabia, Venezuela y México, petróleo para destilar crudo y 
obtienen tres productos destilados: keroseno, gasolina y gas-oil en las siguientes 
proporciones: 

|         |GASOLINA | KEROSENE |   GAS-OIL |
|---------|:-------:|:--------:|:---------:|
|ARABIA   |0.4      |0.4       |0.2        |
|MÉXICO   |0.2      |0.6       |0.2        |
|VENEZUELA|0.4      |0.1       |0.5        |

La empresa de refinamiento ha firmado un contrato con una empresa de distribución para suministrar 10000 barriles de gasolina, 5000 barriles de gas-oil y 2000 de barriles de keroseno. 

a) Plantear un modelo matemático que permita obtener el número de barriles que se deben destilar de cada crudo si se desea cumplir el contrato, sin que sobre ningún barril. 

>[!NOTE]
> ARABIA ($x$), MÉXICO ($y$) y VENEZUELA ($z$).

Los modelos para cada tipo de crudo seria.

Gasolina:
$$0.4x+0.2y+0.4z=10000$$

Kerosone:
$$0.4x+0.6y+0.1z=2000$$

Gas-oil:
$$0.2x+0.2y+0.5z=5000$$

b) Encontrar el número de barriles a destilar de cada tipo de crudo por el método de determinantes.


$$
\Delta_s=
\begin{vmatrix}
0.4 & 0.2 & 0.4 \\
0.4 & 0.6 & 0.1 \\
0.2 & 0.2 & 0.5 \\
\end{vmatrix} = 0.06
$$

$$
\Delta_x=
\begin{vmatrix}
10000 & 0.2 & 0.4 \\
2000 & 0.6 & 0.1 \\
5000 & 0.2 & 0.5 \\
\end{vmatrix} = 1660
$$

$$
\Delta_y=
\begin{vmatrix}
0.4 & 10000 & 0.4 \\
0.4 & 2000 & 0.1 &  \\
0.2 & 5000 & 0.5  \\
\end{vmatrix} = -960
$$

$$
\Delta_z=
\begin{vmatrix}
0.4 & 0.2 & 10000 \\
0.4 & 0.6 & 2000 \\
0.2 & 0.2 & 5000 \\
\end{vmatrix} = 320
$$

$$x=\frac{1660}{0.06}=27666.\overline{6}$$
$$x=\frac{-960}{0.06}=-16000$$
$$x=\frac{320}{0.06}=5333.\overline{3}$$

$$CS=(1660, -960, 320)$$


Interpretación de los resultados

Los valores obtenidos indican lo siguiente:
- $ x \approx 27667 $ barriles deben destilarse de Arabia.
- $ y \approx -16000 $ barriles deben destilarse de México (este valor negativo es un problema, ya que no tiene sentido físico).
- $ z \approx 5333 $ barriles deben destilarse de Venezuela.

El valor negativo para $ y $ sugiere que el sistema planteado tiene algún problema. En particular, puede indicar que el conjunto de proporciones o las cantidades exigidas no permiten una solución factible.