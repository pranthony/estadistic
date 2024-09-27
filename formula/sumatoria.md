## Demostración de la formula de calculo de tamaño de la muestra finita

**The Cauchy-Schwarz Inequality**

$$
 \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right)
$$

$$
k=1+3.322log_{10}(n)
$$

## Representación matematica de sumatoria

**a. Primer caso**
$$
\sum_{i=1}^k =1+2+3+...+k=\frac{k(k+1)}{2}
$$
Ejemplo:
$$
\sum_{i=1}^{12} =1+2+3+...+12=\frac{12(12+1)}{2}
$$
**b. Segundo caso**
$$
\sum_{i=1}^k a = k \times a
$$
Ejemplo:
$$
\sum_{i=1}^{90} 5 = 90 \times 5
$$
**c. Tercer caso**
$$
\sum_{i=1}^k ai=a(i)+a(2)+a(3)+...+a(k)=a\left(\frac{k(k+1)}{2}\right)
$$
Ejemplo:
$$
\sum_{i=1}^{20} 3i=3(1)+3(2)+3(3)+...+3(20)=3\left(\frac{20(20+1)}{2}\right)
$$

\[ f(n) =
  \begin{cases}
    n/2       & \quad \text{if } n \text{ is even}\\
    -(n+1)/2  & \quad \text{if } n \text{ is odd}
  \end{cases}
\]