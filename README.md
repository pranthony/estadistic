# estadistic

To install python dependecies for this project
``` bash
poetry install
```

To start poetry .env
``` bash
poetry shell
```

1. Proyecto de estadistica descritiva

a. Componentes de frecuencia.
Para construir una tabla de distribución de frecuencia se deben considerar elementos como *Rango*, *Clase*, *Ancho de Clase*, etc.

- **Rango**: Dado un conjunto de datos *n*, ubicar los valores minimos y maximos.
```mathlab
rango = X_max - X_min
```

- **Intervalo**: En base al tamaño de muestra (n), aplicamos la regla de Sturges 
```matlab
k = 1 + 3.322log(n)
```
Del resultado se debe redondear al entero mayor.

- **Amplitud**: El cociente del `rango` entre la cantidad de intervalos `k`

```
A = rango / k
```

La amplitud nos permitira conocer la amplitud de cada intervalo.

b. Creación de la tabla de frecuéncia.

- **Marca de clase**: Es el punto medio para cada intervalo.
- **Frecuencia absoluta**: Datos de la muetra que pertenencen a un intervalo.
- **Frecuencia relativa**: Es la frecuencia absoluta dividida por el total de datos.
- **Frecuencia porcentual**: Es la frecuencia relativa multiplicada por 100.

c. Creacion de un histogram de frecuencia.
