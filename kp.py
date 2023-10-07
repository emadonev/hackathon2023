# IMPORTING LIBRARIES
# -----------
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import PillowWriter
import numpy as np
#import imageio as im

# Colormaps
colors_b=["black","blue","white"]
colors_lb=["black","lightsteelblue","white"]
colors_ly=["black","cornsilk","white"]
colors_g=["black","goldenrod","white"]
colors_o=["black","darkorange","white"]
colors_r=["black","orangered","white"]

nodes = [0.0, 0.5, 1.0]

blue_cmap = LinearSegmentedColormap.from_list("blue_cmap", list(zip(nodes, colors_b)))
lb_cmap = LinearSegmentedColormap.from_list("lb_cmap", list(zip(nodes, colors_lb)))
y_cmap = LinearSegmentedColormap.from_list("y_cmap", list(zip(nodes, colors_ly)))
g_cmap = LinearSegmentedColormap.from_list("gold_cmap", list(zip(nodes, colors_g)))
o_cmap = LinearSegmentedColormap.from_list("orange_cmap", list(zip(nodes, colors_o)))
r_cmap = LinearSegmentedColormap.from_list("red_cmap", list(zip(nodes, colors_r)))


spectral_class = {
    'O': [blue_cmap, 'cornflowerblue'],
    'B': [lb_cmap, 'lightblue'],
    'A': ['Greys_r', 'ghostwhite'],
    'F': [y_cmap, 'lemonchiffon'],
    'G': [g_cmap, 'gold'],
    'K': [o_cmap, 'orange'],
    'M': [r_cmap, 'tomato']
}

# PLOT INITIALIZATION
# --------
# setting up the plot
fig, ax = plt.subplots(facecolor='black')
fig.patch.set_facecolor('black')
ax.set_facecolor('black')
# setting plot dimensions
ax.set_xlim(-14, 14)
ax.set_ylim(-12, 12)
ax.set_aspect('equal')

# PARAMETERS
radius_planet = 0.5
radius_sun = 1
lumino = 2 
a = 9
ecc = 0.3 # limit 0.3
planet_color = 'ivory'
spclass = 'K'
cmap_lum = spectral_class[spclass][0]
color_star = spectral_class[spclass][1]
orb_per = 200

# ORBITAL DYNAMICS OF THE PLANET
# --------
b = a * np.sqrt(1 - ecc**2)  # semi-minor axis based on eccentricity
n = np.sqrt(a**2 - b**2) # calculating the distance of the focus from the centre of the ellipse
angle = np.linspace(0, -2*np.pi, orb_per*10) # making an array of frames (angle values)

# Calculate the coordinates for the elliptical orbit
x_orbit = a * np.cos(angle) # x coordinates governed by cosine
y_orbit = b * np.sin(angle) # y coordinates governed by sine

# drawing orbital path
ellipse = Ellipse((n, 0), 2*a, 2*b, edgecolor='white', fc='None', lw=0.5) # drawing an elliptical orbital path
ax.add_patch(ellipse) # add ellipse to plot

# LUMINOSITY MASK
e, f = np.meshgrid(np.linspace(-5, 5, 250), np.linspace(-5, 5, 250)) # adding glow to the star to mimic light emission
z = np.exp(-0.2 * (e**2 + f**2))
mask = e**2 + f**2 <= lumino**2
z[~mask] = np.nan # making of mask
c = plt.pcolormesh(e, f, z, cmap=cmap_lum, shading='auto') # shading the mesh

# PLOTTING STAR
central_circle = plt.Circle((0, 0), 1, fill=True, color=color_star, linewidth=2) # plotting the host star
ax.add_artist(central_circle)

# PLOTTING PLANET ORBIT
time = 'Time (days) = '
label = ax.text(-11, 10, time, ha='center', va='center', fontsize=12, color='white') # making the label for counting the number of days passed

orbiting_circle = plt.Circle((0, 0), 0.5, fill=True, color=planet_color, linewidth=2) # add planet

# ANIMATING MOTION OF THE PLANET
# ---------

def animate(i):
    a, x, y = angle[i]*10, x_orbit[i], y_orbit[i] # defining the coordinates
    orbiting_circle.center = (x+n, y) # plotting the circle
    label.set_text(time + str(i//10).zfill(3)) # updating the label
    return orbiting_circle, label # returning the values

ax.add_artist(orbiting_circle) # adding the circle
ani = FuncAnimation(fig, animate, frames=len(angle), blit=True, interval=10, repeat=False) # animating the planet's motion

#f = r"/Users/emadonev/Library/Mobile Documents/com~apple~CloudDocs/PROJECTS/HACKATHON 2023/kepler.gif" 
#writer = PillowWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
#ani.save(f, writer='pillow',dpi=50)

# SHOWING PLOT
plt.grid(False)
plt.axis('off')
plt.show()