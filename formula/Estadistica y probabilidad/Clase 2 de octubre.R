# ------------------------------------------------------------------------------
# UNIVERSIDAD NACIONAL HERMILIO VALDIZÁN
# FACULTAD DE ECONOMIA 
# ESTADISTICA PROBABILIDADES 
# PROF: J CUEVA
# ------------------------------------------------------------------------------
# TEMA: MEDIDAS DE TENDENCIA CENTRAL (OCTUBRE - UNIDAD 2)
# ------------------------------------------------------------------------------

# Registro de datos cuantitativos. 

edad=c(17, 18, 19, 20, 22, 21, 18, 17, 19, 20,
       23, 22, 21, 18, 19, 20, 17, 16, 18, 19,
       22, 23, 21, 20, 18, 17, 19, 21, 20, 22,
       23, 19, 18, 21, 20, 22, 23, 18, 17, 19,
       20, 18, 21, 22, 23, 19, 17, 20, 21, 18)

# Ordenando de menor a mayor
edad_ordanada_ascedente=sort(edad)
cat("Edades ordenados de menor a mayor:\n")
print(edad_ordanada_ascedente)

# Ordenamiento de los datos de mayor a menor
edad_ordanada_ascedente=sort(edad, decreasing = TRUE)
cat("Edades ordenados de MAYOR A MENOR:\n")
print(edad_ordanada_ascedente)

# Calculos de las medidas de tendencia central

# -------------------------------------------
# MEDIA
# -------------------------------------------

media_edad=mean(edad)
cat("Media de la varibale EDAD:", media_edad,"\n")

# -------------------------------------------
# MEDIANA
# -------------------------------------------

mediana_edad=median(edad)
cat("Mediana de la varibale EDAD:", mediana_edad,"\n")

# -------------------------------------------
# MODA
# -------------------------------------------

moda_edad=as.numeric(names(sort(table(edad),decreasing = TRUE)[2]))
cat("Moda de la variable EDAD:", mediana_edad,"\n")

# -------------------------------------------
# CUARTILES
# -------------------------------------------


cuartilles_edad<-quantile(edad)
cat("Los cuartiles de la Variable EDAD:",cuartilles_edad,"\n")
print(cuartilles_edad)


# -------------------------------------------
# VARIANZA
# -------------------------------------------

varianza_edad<-var(edad)
cat("La varianza de la variable EDAD:",varianza_edad,"\n")


# -------------------------------------------
# DESVIACIÓN TIPICA O ESTANDAR
# -------------------------------------------


desviacion_edad<-sd(edad)
cat("La desviación estandar (s) de la variable EDAD:",desviacion_edad,"\n")