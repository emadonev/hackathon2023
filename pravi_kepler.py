import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import PillowWriter
import numpy as np

mass_planet = ['1.05', '1.57', '1.20', '0.39', '25.3', '1.27', '2.21', '1.08', '1.64', '1.74', '1.40', '2.89', '2.96', '0.69', '2.36', '2.54', '35.0', '1.04', '1.11', '2.54', '1.71', '2.54', '1.36', '1.32']
radius_planet = ['1.02', '1.14', '1.06', '0.78', '1.37', '1.08', '1.29', '1.03', '1.15', '1.18', '1.11', '1.51', '1.52', '0.92', '1.35', '1.45', '1.41', '1.04', '1.04', '1.40', '1.17', '1.45', '1.10', '1.13']
semi_major_axis = ['0.00000025', '0.029', '0.085', '0.022', '0.026', '0.05', '0.03', '0.023', '0.023', '0.02', '0.026', '0.038', '0.024', '0.028', '0.052', '0.08', '0.041', '0.037', '0.032', '0.067', '0.12', '0.06', '0.067', '0.045']
orbital_period = ['4.90', '37.4', '19.5', '4.00', '8.50', '11.2', '24.2', '10.3', '13.0', '6.70', '9.90', '18.6', '34.1', '6.10', '112', '38.0', '267', '9.20', '11.4', '86.8', '130', '62.2', '21.2', '12.4']
surface_temperature = ['25', '5', '30', '23', '8', '-16', '34', '-12', '-26', '38', '44', '19', '9', '-15', '-10', '-24', '-43', '-48', '-48', '-56', '-61', '-60', '-68', '-69']
spclass_star = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'K', 'M', 'K', 'M', 'M', 'M', 'M', 'M', 'M']
mass_star = ['0.08', '0.41', '0.09', '0.08', '0.11', '0.12', '0.35', '0.11', '0.11', '0.11', '0.15', '0.26', '0.12', '0.08', '0.39', '0.33', '0.69', '0.08', '0.08', '0.1', '0.19', '0.33', '0.11', '0.08']
eccentricity = ['0.0', '0.062', '-0', '0.039', '-0', '0.11', '0.11', '-0', '0.53', '0.29', '0.12', '0.10', '0.24', '0.005', '0.28', '0.03', '-0', '0.01', '0.1', '-0', '0.16', '0.12', '-0', '0.002']
                
mass_planet = [float(x) for x in mass_planet]
radius_planet = [float(x) for x in radius_planet]
semi_major_axis = [float(x) for x in semi_major_axis]
orbital_period = [float(x) for x in orbital_period]
surface_temperature = [float(x) for x in surface_temperature]
mass_star = [float(x) for x in mass_star]
eccentricity = [float(x) for x in eccentricity]



def create_kepler_animation(rp, ls, sr, sma, ecc, pc, sps, orb, output_filename):
    
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
    ax.set_xlim(-15, 15)
    ax.set_ylim(-15, 15)
    ax.set_aspect('equal')

    # ORBITAL DYNAMICS OF THE PLANET
    # --------
    b = sma * np.sqrt(1 - ecc**2)  # semi-minor axis based on eccentricity
    n = np.sqrt(sma**2 - b**2) # calculating the distance of the focus from the centre of the ellipse
    angle = np.linspace(0, -2*np.pi, orb*10) # making an array of frames (angle values)

    # Calculate the coordinates for the elliptical orbit
    x_orbit = sma * np.cos(angle) # x coordinates governed by cosine
    y_orbit = b * np.sin(angle) # y coordinates governed by sine

    # drawing orbital path
    ellipse = Ellipse((n, 0), 2*sma, 2*b, edgecolor='white', fc='None', lw=0.5) # drawing an elliptical orbital path
    ax.add_patch(ellipse) # add ellipse to plot

    # LUMINOSITY MASK
    e, f = np.meshgrid(np.linspace(-5, 5, 250), np.linspace(-5, 5, 250)) # adding glow to the star to mimic light emission
    z = np.exp(-0.2 * (e**2 + f**2))
    mask = e**2 + f**2 <= ls**2
    z[~mask] = np.nan # making of mask
    cmap_lum = spectral_class[sps][0]
    c = plt.pcolormesh(e, f, z, cmap=cmap_lum, shading='auto') # shading the mesh

    # PLOTTING STAR
    central_circle = plt.Circle((0, 0), sr, fill=True, color=spectral_class[sps][1], linewidth=2) # plotting the host star
    ax.add_artist(central_circle)

    # PLOTTING PLANET ORBIT
    time = 'Time (days) = '
    label = ax.text(-11, 10, time, ha='center', va='center', fontsize=12, color='white') # making the label for counting the number of days passed

    orbiting_circle = plt.Circle((0, 0), rp, fill=True, color=pc, linewidth=2) # add planet

    # ANIMATING MOTION OF THE PLANET
    # ---------

    def animate(i):
        a, x, y = angle[i]*10, x_orbit[i], y_orbit[i] # defining the coordinates
        orbiting_circle.center = (x+n, y) # plotting the circle
        label.set_text(time + str(i//10).zfill(3)) # updating the label
        return orbiting_circle, label # returning the values

    ax.add_artist(orbiting_circle) # adding the circle
    ani = FuncAnimation(fig, animate, frames=len(angle), blit=True, interval=10, repeat=False) # animating the planet's motion
    writer = PillowWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
    ani.save(output_filename, writer=writer, dpi=50)

    plt.grid(False)
    plt.axis('off')
    plt.show()


i = 6
radius_p = radius_planet[i]/15 # in earth radii
if i==0:
    distance_p = semi_major_axis[i]
else:
    distance_p = semi_major_axis[i]*300
spectral_type = spclass_star[i]
orbital_period = round(orbital_period[i])
if eccentricity[i] == -0:
    ecc = 0.0
else:
    ecc = eccentricity[i]

create_kepler_animation(radius_p, 2, 1, distance_p, ecc, 'ivory', spectral_type, orbital_period, 'Exoplanet_'+str(i)+'.gif')