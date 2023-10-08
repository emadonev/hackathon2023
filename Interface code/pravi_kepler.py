import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import PillowWriter
import numpy as np

mass_planet= ['6.2708e+24', '9.3764e+24', '7.1666e+24', '2.3292e+24', '1.511e+26', '7.5847e+24', '1.3199e+25', '6.45e+24', '9.7944e+24', '1.0392e+25', '8.3611e+24', '1.726e+25', '1.7678e+25', '4.1208e+24', '1.4094e+25', '1.5169e+25', '2.0903e+26', '6.2111e+24', '6.6291e+24', '1.5169e+25', '1.0212e+25', '1.5169e+25', '8.1222e+24', '7.8833e+24']
radius_planet= ['6.4984e+06', '7.2629e+06', '6.7533e+06', '4.9694e+06', '8.7283e+06', '6.8807e+06', '8.2186e+06', '6.5621e+06', '7.3266e+06', '7.5178e+06', '7.0718e+06', '9.6202e+06', '9.6839e+06', '5.8613e+06', '8.6008e+06', '9.238e+06', '8.9831e+06', '6.6258e+06', '6.6258e+06', '8.9194e+06', '7.4541e+06', '9.238e+06', '7.0081e+06', '7.1992e+06']
semi_major_axis= ['37400', '4.3384e+09', '1.2716e+10', '3.2912e+09', '3.8896e+09', '7.48e+09', '4.488e+09', '3.4408e+09', '3.4408e+09', '2.992e+09', '3.8896e+09', '5.6848e+09', '3.5904e+09', '4.1888e+09', '7.7792e+09', '1.1968e+10', '6.1336e+09', '5.5352e+09', '4.7872e+09', '1.0023e+10', '1.7952e+10', '8.976e+09', '1.0023e+10', '6.732e+09']
orbital_period= ['4.2336e+05', '3.2314e+06', '1.6848e+06', '3.456e+05', '7.344e+05', '9.6768e+05', '2.0909e+06', '8.8992e+05', '1.1232e+06', '5.7888e+05', '8.5536e+05', '1.607e+06', '2.9462e+06', '5.2704e+05', '9.7027e+06', '3.2832e+06', '2.3095e+07', '7.9488e+05', '9.8496e+05', '7.4995e+06', '1.1223e+07', '5.3741e+06', '1.8317e+06', '1.0714e+06']
surface_temperature= ['25', '5', '30', '23', '8', '-16', '34', '-12', '-26', '38', '44', '19', '9', '-15', '-10', '-24', '-43', '-48', '-48', '-56', '-61', '-60', '-68', '-69']
spclass_star= ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'K', 'M', 'K', 'M', 'M', 'M', 'M', 'M', 'M']
mass_star= ['1.5912e+29', '8.1549e+29', '1.7901e+29', '1.5912e+29', '2.1879e+29', '2.3868e+29', '6.9615e+29', '2.1879e+29', '2.1879e+29', '2.1879e+29', '2.9835e+29', '5.1714e+29', '2.3868e+29', '1.5912e+29', '7.7571e+29', '6.5637e+29', '1.3724e+30', '1.5912e+29', '1.5912e+29', '1.989e+29', '3.7791e+29', '6.5637e+29', '2.1879e+29', '1.5912e+29']
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


i = 4
radius_p = round(radius_planet[i]/63710000, 2) # in earth radii
if i==0:
    distance_p = round(semi_major_axis[i]/14960, 2)
else:
    distance_p = round(semi_major_axis[i]/1496000000, 2)
spectral_type = spclass_star[i]
orbital_period = round(orbital_period[i]/365)
if eccentricity[i] == -0:
    ecc = 0.0
else:
    ecc = eccentricity[i]

create_kepler_animation(radius_p, 2, 1, distance_p, ecc, 'ivory', spectral_type, orbital_period, 'Exoplanet_'+str(i)+'.gif')