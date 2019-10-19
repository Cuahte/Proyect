import matplotlib.pyplot as plt
lista1 = [11,2,3,15,8,13,21,34]
plt.plot(lista1)
plt.show()
"""
# Generamos los datos para el gráfico
x = np.array(range(500))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Creamos el gráfico
plt.ion()
plt.plot(x,y)"""