## Demostración del exámen

$$
n=\frac{Z_0^2pqN}{e^2(N-1)+Z_0^2pq}
$$

Muestra sin remplazamiento

Nota: consideraciones
$$
d=|μ-\bar{x}|
$$
$$
d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
$$
$$
var(\bar{x})=\frac{\sigma^2}{n}
$$
$$
var(\bar{x})=\frac{\sigma^2}{n}\cdot \left( \frac{N-n}{N-1} \right)
$$
Media poblacional desconocida
$$
\sqrt{\sigma_{\bar{x}}^2}=\sqrt{\frac{\sigma_{μ}^2}{n}\cdot \frac{N-n}{N-1}}
$$
$$
\sigma_{\bar{x}}=\sqrt{\frac{\sigma_{μ}^2}{n}}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
\sigma_{\bar{x}}=\frac{\sigma_{μ}}{\sqrt{n}}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
S.E({\bar{x}})=\frac{\sigma_{μ}}{\sqrt{n}}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
e = S.E({\bar{x}})\cdot Z_0=Z_0\cdot \frac{\sigma_{μ}}{\sqrt{n}}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
e \cdot \sqrt{n} = \sqrt{n} \cdot Z_0\cdot \frac{\sigma_{μ}}{\sqrt{n}}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
e \cdot \sqrt{n} = \cdot Z_0\cdot \sigma_{μ}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
e \cdot \sqrt{n} \cdot \frac{1}{e} =\frac{1}{e} \cdot Z_0\cdot \sigma_{μ}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
\sqrt{n}=\frac{1}{e} \cdot Z_0\cdot \sigma_{μ}\cdot \sqrt{\frac{N-n}{N-1}}
$$
$$
(\sqrt{n})^2=\left( \frac{1}{e} \cdot Z_0\cdot \sigma_{μ}\cdot \sqrt{\frac{N-n}{N-1}} \right)^2
$$
$$
(\sqrt{n})^2=\left( \frac{1}{e} \cdot Z_0\cdot \sigma_{μ}\cdot \sqrt{\frac{N-n}{N-1}} \right)^2
$$
$$
n=Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{N-n}{N-1}
$$
$$
n=Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \left( \frac{N}{N-1} - \frac{n}{N-1} \right)
$$
$$
n=Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{N}{N-1} - Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{n}{N-1} 
$$
$$
n + Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{n}{N-1} =Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{N}{N-1} 
$$
$$
n \left( 1 + Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{1}{N-1} \right) =Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{N}{N-1} 
$$
$$
n =  Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{N}{N-1} \div \left( 1 + Z_0^2\cdot \frac{\sigma_{μ}^2}{e^2} \cdot \frac{1}{N-1} \right)
$$
$$
n = \frac{Z_0^2 \cdot \sigma_{μ}^2}{e^2} \cdot \frac{N}{N-1} \div \left( 1 +  \frac{Z_0^2\cdot\sigma_{μ}^2}{e^2} \cdot \frac{1}{N-1} \right)
$$
$$
n = \frac{Z_0^2 \cdot \sigma_{μ}^2 \cdot N}{e^2 (N -1)} \div \left( 1 +  \frac{Z_0^2\cdot\sigma_{μ}^2 }{e^2 (N-1)} \right)
$$
$$
n = \frac{Z_0^2 \cdot \sigma_{μ}^2 \cdot N}{e^2 (N -1)} \div \left(   \frac{Z_0^2\cdot\sigma_{μ}^2 + e^2 (N-1) }{e^2 ( N-1)} \right)
$$
$$
n = \frac{Z_0^2 \cdot \sigma_{μ}^2 \cdot N}{e^2 (N -1)} \cdot \left(   \frac{e^2 ( N-1)}{Z_0^2\cdot\sigma_{μ}^2 + e^2 (N-1)} \right)
$$
$$
n = \frac{Z_0^2 \cdot \sigma_{μ}^2 \cdot N}{Z_0^2\cdot\sigma_{μ}^2 + e^2 (N-1)} 
$$