install.packages("ggplot2")
library(ggplot2)
install.packages("forecast")
library(forecast)
install.packages("tidyverse")
library(tidyverse)
install.packages("ggfortify")
library(ggfortify)
install.packages("imputeTS")      
library(imputeTS)  

View(VENTAS_CON_FALTANTES)
# del dataset VENTAS_CON_FALTANTES nueva variable ventas2
ventas2 = ts(VENTAS_CON_FALTANTES$ventas)
autoplot(ventas2) # autoplot sugerencia de la mejor grafica
ventas_ajustadas = na.interp(ventas2)
ventas_ajustadas
autoplot(ventas_ajustadas, series = "interpolada") + 
autolayer(ventas2, series = "original")+
scale_colour_manual(values = c('interpolada'="red", 'original'="blue"))

ggplot_na_distribution(ventas2)
statsNA(ventas2)
ventas_ajustadas2 = na_interpolation(ventas2)
autoplot(ventas_ajustadas2, series = "interpolada") + 
autolayer(ventas2, series = "original")+
scale_colour_manual(values = c('interpolada'="red", 'original'="blue"))
