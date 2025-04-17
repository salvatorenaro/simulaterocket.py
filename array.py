import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist

(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test, y_test)

v0 = 4390  
g = 9.81   
angle_deg = 45  
angle_rad = np.radians(angle_deg) 
t_max = 2 * v0 * np.sin(angle_rad) / g  
t = np.linspace(0, t_max, 100)  
x = v0 * np.cos(angle_rad) * t  
y = v0 * np.sin(angle_rad) * t - 0.5 * g * t**2  

plt.figure(facecolor="black", figsize=(10, 6))
plt.plot(x, y, color="cyan", linewidth=2)
plt.title('SpaceX Traiettoria Razzo', color="white")
plt.xlabel('Distanza Orizzontale (m)', color="white")
plt.ylabel('Altitudine (m)', color="white")
plt.grid(True, color="gray", linestyle="--", alpha=0.5)
ax = plt.gca()
ax.set_facecolor('black')
ax.tick_params(colors='white')
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
plt.show()