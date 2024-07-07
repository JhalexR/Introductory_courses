library(ggplot2)
library(forecast)
library(tidyverse)
library(ggfortify)

chocolate = ts(CHOCOLATE_SEMANAL)
autoplot(chocolate)
mstl(chocolate)#Descomponer una serie de tiempo en componentes estacionales, de tendencia y de resto
autoplot(mstl(chocolate))#grafica Descompuesta
ggAcf (chocolate) #grafica de autocorrelacion 

demanda = ts(ATIPICOS2$...2)
autoplot(demanda)
autoplot(mstl(demanda))
ggAcf (demanda)

cafe = ts(CAFE_DIARIO)
autoplot(cafe)
autoplot(mstl(cafe))
ggAcf (cafe)

cafe = ts(CAFE_DIARIO, frequency = 7)
autoplot(mstl(cafe))

ggseasonplot(cafe)

ggseasonplot(cafe, polar = T)

ggsubseriesplot(cafe)
