import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.compile(
    optimizer = tf.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
pesos = [19.09, 38.19, 57.29, 76.39, 95.49, 114.61, 133.71, 152.82, 171.91, 191.02]
euros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Comenzando Entrenmiento!")
model.fit(pesos, euros, epochs=1000)
print("Modelo Entrenado!")

resultado = model.predict([100])# pesos mexicanos
print("El resultado es: "+ str (resultado) + " euros")