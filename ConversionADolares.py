import tensorflow as tf

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(units=1, input_shape=[1]))
model.compile(
    optimizer=tf.optimizers.Adam(0.1),
    loss='mean_squared_error')

pesos = [17.59, 35.06, 52.59, 70.12, 87.65, 105.57, 123.16, 140.75, 158.36, 175.65]
dolares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Comenzando Entrenmiento!")
model.fit(pesos, dolares, epochs=1000)
print("Modelo Entrenado!")

resultado = model.predict([17.53])# pesos mexicanos
print("El resultado es: "+ str (resultado) + " dolares")