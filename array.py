import numpy as np
import matplotlib.pyplot as plt


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