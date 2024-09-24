# estadistic

### To install python dependecies for this project
´´´bash
poetry install
´´´

### To start poetry .env
´´´bash
poetry shell
´´´

1. Proyecto de estadistica descritiva

a. Tabla de distribucion de frecuencias
Para construir una tabla de distribución de frecuencia se deben considerar elementos como *Rango*, *Clase*, *Ancho de Clase*, etc.

- **Rango**: Dado un conjunto de datos *n*, ubicar los valores minimos y maximos.
´´´´matlab
Rango = X_max - X_min
´´´

- **Intervalo**: En base al tamaño de muestra (n), aplicamos la regla de Sturges 
´´´´matlab
k = 1 + 3.322log(n)
´´´