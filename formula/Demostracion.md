# Cálculo del Tamaño de Muestra sin Reemplazo

El cálculo del tamaño de muestra sin reemplazo para poblaciones finitas se realiza usando la siguiente fórmula:

\[
n = \frac{Z_0^2 \cdot p \cdot q \cdot N}{e^2(N-1) + Z_0^2 \cdot p \cdot q}
\]

## Descripción de la Fórmula

### Elementos

- **\(n\)**: Tamaño de la muestra requerida.
- **\(Z_0\)**: Valor del puntaje Z asociado con el nivel de confianza deseado.
  - Ejemplo: Para un nivel de confianza del 95%, \(Z_0 = 1.96\).
- **\(p\)**: Proporción esperada de éxito en la población.
  - Si no se conoce, se suele usar \(p = 0.5\), lo que maximiza el tamaño de la muestra.
- **\(q = 1 - p\)**: Proporción esperada de fracaso.
- **\(N\)**: Tamaño total de la población.
- **\(e\)**: Margen de error o precisión deseada.

### Explicación de los Factores

1. **\(Z_0^2 \cdot p \cdot q \cdot N\)**: 
   - Este término refleja la variabilidad total de la población en términos de proporciones \(p\) y \(q\), ajustada por el nivel de confianza \(Z_0\) y multiplicada por el tamaño de la población \(N\).

2. **\(e^2(N-1)\)**: 
   - Representa el margen de error cuadrado multiplicado por el tamaño de la población menos uno.
   - Este término controla la precisión de la estimación.

3. **\(Z_0^2 \cdot p \cdot q\)**: 
   - Este término representa la varianza de la proporción en la población multiplicada por el nivel de confianza \(Z_0\).

## Proceso Paso a Paso

### 1. Definición del Tamaño de Muestra en Función del Error Estándar

Partimos de la fórmula para el error estándar de una proporción:

\[
S.E(\bar{p}) = \sqrt{\frac{p \cdot q}{n}} \cdot \sqrt{\frac{N - n}{N - 1}}
\]

Donde:

- **\(S.E(\bar{p})\)** es el error estándar de la proporción en la muestra.
- **\(p\)** y **\(q\)** son las proporciones de éxito y fracaso.
- **\(n\)** es el tamaño de la muestra.
- **\(N\)** es el tamaño de la población.

Luego, el margen de error está dado por:

\[
e = Z_0 \cdot S.E(\bar{p})
\]

Despejando \(S.E(\bar{p})\) de la fórmula:

\[
e = Z_0 \cdot \sqrt{\frac{p \cdot q}{n}} \cdot \sqrt{\frac{N - n}{N - 1}}
\]

### 2. Cuadramos Ambos Lados para Eliminar la Raíz

Para simplificar, elevamos ambos lados al cuadrado:

\[
e^2 = Z_0^2 \cdot \frac{p \cdot q}{n} \cdot \frac{N - n}{N - 1}
\]

Multiplicamos ambos lados por \(n\) para despejar el denominador:

\[
e^2 \cdot n = Z_0^2 \cdot p \cdot q \cdot \frac{N - n}{N - 1}
\]

### 3. Aislamiento del Tamaño de Muestra \(n\)

Multiplicamos ambos lados por \(\frac{1}{e^2}\):

\[
n = \frac{Z_0^2 \cdot p \cdot q (N - n)}{e^2 (N - 1)}
\]

Aislar \(n\) en términos de proporciones da lugar a:

\[
\frac{n}{N - n} = \frac{Z_0^2 \cdot p \cdot q}{e^2 (N - 1)}
\]

Simplificando, obtenemos:

\[
\frac{N}{n} = \frac{e^2(N - 1) + Z_0^2 \cdot p \cdot q}{Z_0^2 \cdot p \cdot q}
\]

Despejando el tamaño de la muestra \(n\):

\[
n = \frac{Z_0^2 \cdot p \cdot q \cdot N}{e^2 (N - 1) + Z_0^2 \cdot p \cdot q}
\]

## Consideraciones Adicionales

### Varianza de la Media Muestral

Cuando calculamos la varianza de la media muestral, se utiliza la siguiente fórmula:

\[
\text{var}(\bar{x}) = \frac{\sigma^2}{n} \cdot \frac{N - n}{N - 1}
\]

Este ajuste se debe al muestreo sin reemplazo, que introduce dependencia entre las observaciones y reduce la varianza muestral.

### Fórmula del Error Estándar

El error estándar de una proporción se ajusta considerando el tamaño finito de la población:

\[
S.E(\bar{p}) = \sqrt{\frac{p \cdot q}{n}} \cdot \sqrt{\frac{N - n}{N - 1}}
\]

Y el margen de error está dado por:

\[
e = Z_0 \cdot S.E(\bar{p})
\]

Esto se usa para calcular el tamaño de muestra necesario para una precisión deseada en la estimación de una proporción.

### Relación Entre los Parámetros

La fórmula muestra que:

- Un **mayor nivel de confianza** (mayor \(Z_0\)) **aumenta el tamaño de la muestra**.
- Un **margen de error más pequeño** \(e\) también **incrementa el tamaño de la muestra**.
- El **tamaño de la población \(N\)** afecta el tamaño de la muestra a través del factor de corrección finita \(\frac{N-n}{N-1}\).

## Conclusión

El tamaño de muestra \(n\) requerido depende de la variabilidad en la proporción (\(p\) y \(q\)), el nivel de confianza deseado (\(Z_0\)), el margen de error aceptable (\(e\)) y el tamaño de la población (\(N\)). La fórmula incluye una corrección por el tamaño finito de la población, lo que reduce el tamaño de la muestra en comparación con una población infinita.
