# IMPORTANJE MODULA
# -----------
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
import numpy as np

# dictionaries
spectral_class = {
    'O': ['Blues_r', 'cornflowerblue'],
    'B': ['PuBu_r', 'lightblue'],
    'A': ['Greys_r', 'ghostwhite'],
    'F': ['YlOrBr_r', 'lemonchiffon'],
    'G': ['YlOrRd_r', 'gold'],
    'K': ['OrRd_r', 'orange'],
    'G': ['gist_heat', 'tomato']
}


# INICIJALIZACIJA PLOTA
# --------
# postavljanje pozadinske boje
fig, ax = plt.subplots(facecolor='black')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
# postavljanje dimenzija plota
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)
ax.set_aspect('equal')

# POSTAVLJANJE PARAMETARA (in progress)
radius_planet = 0.5
radius_sun = 1
lumino = 1.5 
a = 9
ecc = 0.1
planet_color = 'ivory'
spclass = 'O'
cmap_lum = spectral_class[spclass][0]
color_star = spectral_class[spclass][1]

# ORBITAL DYNAMICS OF PLANET
# --------
b = a * np.sqrt(1 - ecc**2)  # semi-minor axis based on eccentricity
n = np.sqrt(a**2 - b**2)
angle = np.linspace(0, -2*np.pi, 10000)

# Calculate the coordinates for the elliptical orbit
x_orbit = a * np.cos(angle)
y_orbit = b * np.sin(angle)

# drawing orbital path
ellipse = Ellipse((n, 0), 2*a, 2*b, edgecolor='white', fc='None', lw=0.5)
ax.add_patch(ellipse)

# LUMINOSITY MASK
x, y = np.meshgrid(np.linspace(-5, 5, 250), np.linspace(-5, 5, 250))
z = np.exp(-0.2 * (x**2 + y**2))
mask = x**2 + y**2 <= lumino**2
z[~mask] = np.nan
c = plt.pcolormesh(x, y, z, cmap=cmap_lum, shading='auto')

# PLOTTING STAR
central_circle = plt.Circle((0, 0), 1, fill=True, color=color_star, linewidth=2)
ax.add_artist(central_circle)

# PLOTTING PLANET ORBIT
#for a, x, y in zip(angle, x_orbit, y_orbit):
  #  orbiting_circle = plt.Circle((x+n, y), 0.5, fill=True, color=planet_color, linewidth=2)
   # ax.add_artist(orbiting_circle)
   # plt.pause(0.0001)  # Pause for a short period
  #  orbiting_circle.remove()

time = 'Time (days) = '
label = ax.text(-11, 10, time,
            ha='center', va='center',
            fontsize=12, color='white')

orbiting_circle = plt.Circle((0, 0), 0.5, fill=True, color=planet_color, linewidth=2)

def animate(i):
    label.set_text(time + str(i//100).zfill(3))
    a, x, y = angle[i], x_orbit[i], y_orbit[i]
    orbiting_circle.center = (x+n, y)
    return orbiting_circle, label

ax.add_artist(orbiting_circle)

ani = FuncAnimation(fig, animate, frames=len(angle), blit=True, interval=6) 
# SHOWING PLOT
plt.grid(False)
plt.axis('off')
plt.show()