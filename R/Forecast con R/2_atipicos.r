install.packages("ggplot2")
library(ggplot2)
install.packages("forecast")
library(forecast)
install.packages("tidyverse")
library(tidyverse)
install.packages("ggfortify")
library(ggfortify)

ventas = ts(ATIPICOS$...2)
boxplot(ventas)
boxplot.stats(ventas)
a = boxplot.stats(ventas)
Index = match(a$out, ventas) 
Index
autoplot(ventas)

ventas = ts(ATIPICOS2$...2) 
boxplot(ventas) 
boxplot.stats(ventas) 
a = boxplot.stats(ventas)
Index = match(a$out, ventas) 
Index
autoplot(ventas)

tsoutliers(ventas) 

Ventas_ajustadas3 =ts(tsclean(ventas))
autoplot(ventas)