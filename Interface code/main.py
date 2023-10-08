from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageSequence
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import PillowWriter
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from itertools import product
import noise_gen as ng
import body_gen as bg
from scipy.constants import G as G
from PIL import Image
import noise_gen as ng
import body_gen as bg
from itertools import product
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from itertools import product
from scipy.constants import G as G
import random
import noise
import numpy as np
from noise import pnoise2


color="white"
persistence = 0.7
octaves = 7
resolution = 1920
lista=[]


#PODACI
#----------------------
name_planet = ["Teegarden's Star b", "TOI-700 d", "Kepler-1649 c", "TRAPPIST-1 d", "LP 890-9 c", "Proxima Cen b", "K2-72 e", "GJ 1002 b", "GJ 1061 d", "GJ 1061 c", "Ross 128 b", "GJ 273 b", "Kepler-296 e", "TRAPPIST-1 e", "Kepler-442 b", "GJ 667 C f", "Kepler-62 f", "TRAPPIST-1 f", "Teegarden's Star c", "Kepler-1229 b", "Kepler-186 f", "GJ 667 C e", "GJ 1002 c", "TRAPPIST-1 g"]
mass_planet = ['1.05', '1.57', '1.20', '0.39', '25.3', '1.27', '2.21', '1.08', '1.64', '1.74', '1.40', '2.89', '2.96', '0.69', '2.36', '2.54', '35.0', '1.04', '1.11', '2.54', '1.71', '2.54', '1.36', '1.32']
radius_planet = ['1.02', '1.14', '1.06', '0.78', '1.37', '1.08', '1.29', '1.03', '1.15', '1.18', '1.11', '1.51', '1.52', '0.92', '1.35', '1.45', '1.41', '1.04', '1.04', '1.40', '1.17', '1.45', '1.10', '1.13']
semi_major_axis = ['0.00000025', '0.029', '0.085', '0.022', '0.026', '0.05', '0.03', '0.023', '0.023', '0.02', '0.026', '0.038', '0.024', '0.028', '0.052', '0.08', '0.041', '0.037', '0.032', '0.067', '0.12', '0.06', '0.067', '0.045']
orbital_period = ['4.90', '37.4', '19.5', '4.00', '8.50', '11.2', '24.2', '10.3', '13.0', '6.70', '9.90', '18.6', '34.1', '6.10', '112', '38.0', '267', '9.20', '11.4', '86.8', '130', '62.2', '21.2', '12.4']
surface_temperature = ['25', '5', '30', '23', '8', '-16', '34', '-12', '-26', '38', '44', '19', '9', '-15', '-10', '-24', '-43', '-48', '-48', '-56', '-61', '-60', '-68', '-69']
spclass_star = ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'K', 'M', 'K', 'M', 'M', 'M', 'M', 'M', 'M']
mass_star = ['0.08', '0.41', '0.09', '0.08', '0.11', '0.12', '0.35', '0.11', '0.11', '0.11', '0.15', '0.26', '0.12', '0.08', '0.39', '0.33', '0.69', '0.08', '0.08', '0.1', '0.19', '0.33', '0.11', '0.08']
eccentricity = ['0.0', '0.062', '-0', '0.039', '-0', '0.11', '0.11', '-0', '0.53', '0.29', '0.12', '0.10', '0.24', '0.005', '0.28', '0.03', '-0', '0.01', '0.1', '-0', '0.16', '0.12', '-0', '0.002']
flux_planet=[1.15, 8.70e-01, 1.23, 1.12, 9.10e-01, 7.00e-01, 1.30, 6.70e-01, 6.90e-01, 1.45, 1.48, 1.06, 1.00, 6.50e-01, 7.00e-01, 5.60e-01, 4.10e-01, 3.70e-01, 3.70e-01, 3.20e-01, 2.90e-01, 3.00e-01, 2.60e-01, 2.50e-01]
                
mass_planet = [float(x) for x in mass_planet]
radius_planet = [float(x) for x in radius_planet]
semi_major_axis = [float(x) for x in semi_major_axis]
orbital_period = [float(x) for x in orbital_period]
surface_temperature = [float(x) for x in surface_temperature]
mass_star = [float(x) for x in mass_star]
eccentricity = [float(x) for x in eccentricity]
flux_planet=[float(x) for x in flux_planet]
spclass_star_lower=[x.lower() for x in spclass_star]

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Hackathon program")

#KEPLER ANIMACIJA
#-----------------------
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
    max_radius = max(sr, sma)

    # Set plot dimensions based on the maximum radius
    ax.set_xlim(-max_radius-1, max_radius+1)
    ax.set_ylim(-max_radius-1, max_radius+1)

    ax.set_aspect('equal')

    # ORBITAL DYNAMICS OF THE PLANET
    # --------
    b = sma * np.sqrt(1 - ecc**2)  # semi-minor axis based on eccentricity
    n = np.sqrt(sma**2 - b**2) # calculating the distance of the focus from the centre of the ellipse
    angle = np.linspace(0, -2*np.pi, int(orb*10))

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
  
#PLANET GENERATION
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from itertools import product
from scipy.constants import G as G
import random
import noise
import numpy as np
from noise import pnoise2

persistence = 0.7
octaves = 7
resolution = 1920

def generate_planet(t, m, r, flux, star_type, filename):
    water_normalized_noise, land_normalized_noise = NoiseGen.generate_noise(resolution, t, m, r, flux, octaves, persistence, star_type)
    clouds_noise_map = NoiseGen.generate_clouds_noise(resolution, t, m, r, flux, octaves, persistence)
    water_map, land_map = BodyGen.generate_colors(t, star_type, m, r, flux)
    cloud_map = BodyGen.generate_clouds(t, star_type, m, r, flux)

    land_image = Image.new("RGBA", (resolution, resolution))
    clouds_image = Image.new("RGBA", (resolution, resolution))
    water_image = Image.new("RGBA", (resolution, resolution))

    land_array = land_image.load()
    clouds_array = clouds_image.load()
    water_array = water_image.load()

    for y, x in product(range(resolution), repeat=2):
        planet_noise_value = land_normalized_noise[y, x]
        land_array[x, y] = find_color(planet_noise_value, land_map)

        cloud_noise_value = clouds_noise_map[y, x]
        clouds_array[x, y] = find_color(cloud_noise_value, cloud_map)

        water_noise_value = water_normalized_noise[y, x]
        water_array[x, y] = find_color(water_noise_value, water_map)

    shadow_image = Image.open("./resources/shadow.png").resize((resolution, resolution), Image.LANCZOS)
    output_image = Image.alpha_composite(water_image, land_image)
    output_image = Image.alpha_composite(output_image, clouds_image)
    output_image = Image.alpha_composite(output_image, shadow_image)

    save_planet(output_image, filename)

@staticmethod
def find_color(noise_value, color_map):
    for (lower, upper), color in color_map.items():
        if lower <= noise_value <= upper:
            return color
    return 0, 0, 0, 0

def save_planet(output_image, file_path):
    if file_path:
        output_image.save(file_path)


class NoiseGen:
    @staticmethod
    def generate_clouds_noise(resolution, t, mass, radius, flux, octaves, persistence):
        center = resolution // 2 # where the centre of the array is
        scale = 0.3 * resolution # scaling factor for noise
        # octaves = 6 # parameter which affects the detailedness of the clouds: rounder or more refined
        # persistence = 0.45 # amplitude of the octaves
        # lacunarity = 2.0 # frequency of the octaves
        seed = random.randint(0, 100) # seed for the noise
        noise_array = np.zeros((resolution, resolution)) # preliminary empty array which we fill in later with noise
        for y in range(resolution): # for every y value
            for x in range(resolution): # for every x value in y column
                squared_distance_to_center = (x - center) ** 2 + (y - center) ** 2 # calculate the squared distance from the center
                if squared_distance_to_center <= center ** 2: # if it is within a radius from the center
                    # generate the random noise for that point
                    noise_value = noise.pnoise2(x / scale,
                                                y / scale,
                                                octaves=octaves,
                                                persistence=persistence,
                                                repeatx=resolution,
                                                repeaty=resolution,
                                                base=seed)
                    noise_array[y, x] = noise_value # save the noise value for that coordinate

        normalized_cloud_noise = (noise_array - np.min(noise_array)) / \
                                 (np.max(noise_array) - np.min(noise_array)) # normalize the cloud noise
        return normalized_cloud_noise

    @staticmethod
    def generate_noise(resolution, t, mass, radius, flux, octaves, persistence, star_type):  # t = average surface temeperature
        g = (G*mass*(5.972*(10**24)))/(radius**2)
        center = resolution // 2  # Calculate the center of the noise map
        scale = 0.2 * resolution  # Set the scaling factor for noise generation

        # octaves = 6 # parameter which affects the detailednesss: rounder or more refined
        # persistence = 0.45 # amplitude of the octaves
        # lacunarity = 2.0 # frequency of the octaves

        seed = random.randint(0, 100)  # Generate a random seed for the noise

        # Initialize arrays to store noise values for the entire map, water, and land
        noise_array = np.zeros((resolution, resolution))
        water_noise_array = np.zeros((resolution, resolution))
        land_noise_array = np.zeros((resolution, resolution))

        sea_level = abs((1 / (1.6 * 10 ** 8)) * t * (t + 30) * (t - 60) * (t - 50) * (t + 60)) + PlanetType.WaterLevelIncrease(star_type) # Calculate the sea level threshold based on average temperature (t)

        # Generate Perlin noise for the entire map
        for y in range(resolution):
            for x in range(resolution):
                squared_distance_to_center = (x - center) ** 2 + (y - center) ** 2
                if squared_distance_to_center <= center ** 2:
                    noise_value = pnoise2(x / scale,
                                        y / scale,
                                        octaves=octaves,
                                        persistence=persistence,
                                        repeatx=resolution,
                                        repeaty=resolution,
                                        base=seed)
                    noise_array[y, x] = noise_value

        # Normalize the entire noise map to the range [0, 1]
        normalized_noise = (noise_array - np.min(noise_array)) / \
                        (np.max(noise_array) - np.min(noise_array))

        # Determine the background value from the top-left corner of the normalized noise
        background = normalized_noise[0, 0]

        # Set all background values to -0.1 to create variation
        for y in range(resolution):
            for x in range(resolution):
                if normalized_noise[y, x] == background:
                    normalized_noise[y, x] = -0.1

        # Classify noise values into water and land based on sea level
        for y in range(resolution):
            for x in range(resolution):
                if normalized_noise[y, x] <= sea_level:
                    water_noise_array[y, x] = normalized_noise[y, x]
                else:
                    land_noise_array[y, x] = normalized_noise[y, x]

        # Normalize the water and land noise maps to the range [0, 1]
        water_normalized = (water_noise_array - np.min(water_noise_array)) / \
                        (np.max(water_noise_array) - np.min(water_noise_array))
        land_normalized = (land_noise_array - np.min(land_noise_array)) / \
                        (np.max(land_noise_array) - np.min(land_noise_array))

        # Adjust land heights based on distance from the center and average temperature
        for y in range(resolution):
            for x in range(resolution):
                if land_normalized[y, x] > 0:
                    z = abs(y - center)  # Distance from center
                    land_normalized[y, x] += (z/(resolution//2)) - 3*abs(t)/100
                    land_normalized[y, x] = min(0.98, land_normalized[y, x])
                    land_normalized[y, x] = max(0.1, land_normalized[y, x])

        # Return the normalized water and land noise maps
        return water_normalized, land_normalized

class BodyGen:
    @staticmethod
    def generate_colors(avg_temperature, star_type, mass, radius, flux):
        g = (G*mass*(5.972*(10**24)))/(radius**2)
        depth_increase = PlanetType.WaterDepthIncrease(g)

        # Temperature - biomes relations
        if avg_temperature < -30:
            biomes = PlanetType.frozen_world
            water_map = PlanetType.frozen_ocean
        elif avg_temperature < 0:
            biomes_attr = f"{star_type}_boreal_world"
            biomes = getattr(PlanetType, biomes_attr)
            water_map = PlanetType.frozen_ocean
        elif avg_temperature < 10:
            biomes_attr = f"{star_type}_cold_temperate_world"
            biomes = getattr(PlanetType, biomes_attr)
            water_map = PlanetType.standard_ocean
        elif avg_temperature < 22:
            biomes_attr = f"{star_type}_temperate_world"
            biomes = getattr(PlanetType, biomes_attr)
            water_map = PlanetType.standard_ocean
        elif avg_temperature < 36:
            biomes_attr = f"{star_type}_tropical_world"
            biomes = getattr(PlanetType, biomes_attr)
            water_map = PlanetType.warm_ocean
        else:
            biomes_attr = f"{star_type}_dune_world"
            biomes = getattr(PlanetType, biomes_attr)
            water_map = PlanetType.warm_ocean

        water_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Backgroud
            (0., 0.6+depth_increase): water_map[0],  # Deep ocean
            (0.6+depth_increase, 0.8-depth_increase): water_map[1],  # Ocean
            (0.8+depth_increase, 0.97-depth_increase): water_map[2],  # Coastal
            (0.97+depth_increase, 1): water_map[3],
        }

        # Painting biomes
        land_map = {
            (-1.0, 0.0): (0, 0, 0, 0),
            (0.0, 0.16): biomes[0],
            (0.16, 0.2): biomes[1],
            (0.2, 0.24): biomes[2],
            (0.24, 0.32): biomes[3],
            (0.32, 0.4): biomes[4],
            (0.4, 0.48): biomes[5],
            (0.48, 0.64): biomes[6],
            (0.64, 0.8): biomes[7],
            (0.8, 0.86): biomes[8],
            (0.86, 0.92): biomes[9],
            (0.92, 0.95): biomes[10],
            (0.95, 1): biomes[11],
        }
        return water_map, land_map

    @staticmethod
    def generate_clouds(t, star_type, mass, radius, flux):
        g = (G*mass*(5.972*(10**24)))/(radius**2)
        cloud_variable = PlanetType.CloudVariation(t, flux, g)
        clouds = PlanetType.clouds
        cloud_map = {
            (-1.0, 0.0): (0, 0, 0, 0),  # Transparent layer
            (0.6-cloud_variable, 0.8-cloud_variable): clouds[0],
            (0.8-cloud_variable, 0.85-cloud_variable): clouds[1],
        }
        return cloud_map

class PlanetType:
    # Biome list
    # Water layers
    __deep_ocean = (0, 0, 70)
    __warm_deep_ocean = (0, 160, 192) #0 160 192    #0, 162, 177
    __ocean = (0, 0, 80) #0 0 80   #0, 0, 100
    __warm_ocean = (0, 170, 210) #0 170 210     #0, 190, 196
    __coastal = (0, 10, 90) #0 10 90         #84, 180, 238
    __warm_coastal = (0, 190, 230 ) #0 190 230         #107, 211, 225
    __coast = (190, 180, 70) #190 180 70        #234, 155, 59
    __cold_coast = (80, 75, 50) #80 75 50       #88, 75, 50
    __frozen_coast = (190, 225, 250) #190 225 250   #189, 206, 219
    __frozen = (225, 255, 245) 
    __frozen2 = (225, 250, 245) #225 250 245    #219, 218, 235
    __frozen3 = (210, 230, 230)

    # Vegetation layers
    __m_tundra = (105, 90, 90) #105 90 90   #
    __k_tundra = (140, 110, 80)
    __g_tundra = (0, 100, 90) #0 100 90     #191, 164, 160
    __f_tundra = (23, 68, 103) #0, 80, 140
    __a_tundra = (0, 110, 200)

    __m_taiga = (94, 73, 73) #56 20 20      #94, 73, 73
    __k_taiga = (70, 40, 0) 
    __g_taiga = (0, 80, 60) 
    __f_taiga = (4, 59, 98) #0, 70, 120
    __a_taiga = (0, 90, 160)


    __m_continental_forest = (101, 7, 46)  #105, 10, 20     #101, 7, 46
    __k_continental_forest = (110, 55, 0)
    __g_continental_forest = (29, 108, 74) #0 105 60    #29, 108, 74
    __f_continental_forest = (0, 100, 90)
    __a_continental_forest = (0, 130, 110)


    __m_continental_steppe = (125, 10, 16)  #135, 20, 25    #125 10 16  
    __k_continental_steppe = (130, 60, 0)
    __g_continental_steppe = (138, 168, 76) #90 180 80  #138, 168, 76
    __f_continental_steppe = (0, 110, 100)
    __a_continental_steppe = (0, 150, 130)


    __m_mediterranean = (143, 22, 11)   #150, 35, 25        #143 22 11
    __k_mediterranean = (130, 50, 10)
    __g_mediterranean = (148, 191, 55) #135 200 20  #148, 191, 55
    __f_mediterranean = (0, 120, 110)
    __a_mediterranean = (0, 170, 150) 


    __m_subtropical = (83, 2, 51)   #70, 2, 30      #83, 2, 51
    __k_subtropical = (150, 50, 0)
    __g_subtropical = (50, 110, 20) 
    __f_subtropical = (0, 130, 120)
    __a_subtropical = (0, 190, 170) 


    __m_tropical = (70, 1, 28)    #110, 10, 50       #70, 1, 28
    __k_tropical = (175, 65, 10)
    __g_tropical = (0, 100, 0) #20 80 20    #0, 100, 0
    __f_tropical = (0, 140, 130)
    __a_tropical = (0, 210, 190) 


    __m_savanna = (117, 57, 37)     #130, 70, 50       #117, 57, 37
    __k_savanna = (120, 80, 15)
    __g_savanna = (172, 172, 11) #115 130 40    #172, 172, 11
    __f_savanna = (0, 150, 140)
    __a_savanna = (0, 230, 210)  


    # Land layers
    __semi_arid = (194, 152, 61) #190, 140, 36      #194 152 61
    __arid_desert = (173, 156, 45) #174, 155, 36    #173, 156, 45
    __snow_biome = (255, 255, 255)
    __mountains = (20, 30, 45)
    __rocks = (53, 53, 53)
    __rocky = (96, 96, 96)
    # Clouds
    __cloud_body = (255, 255, 255, 160)
    __cloud_shape = (220, 255, 255, 150)

    clouds = (
        (255, 255, 255, 190),
        (255, 255, 235, 200),
    )

    # Water maps
    standard_ocean = (
        __deep_ocean,
        __ocean,
        __coastal,
        __coast,
    )

    frozen_ocean = (
        __frozen,
        __frozen2,
        __frozen3,
        __frozen_coast,
    )

    warm_ocean = (
        __warm_deep_ocean,
        __warm_ocean,
        __warm_coastal,
        __coast,
    )

    # Land Maps
    noise_world = (
        (0, 0, 0),
        (21, 21, 21),
        (42, 42, 42),
        (63, 63, 63),
        (84, 84, 84),
        (105, 105, 105),
        (126, 126, 126),
        (147, 147, 147),
        (168, 168, 168),
        (189, 189, 189),
        (210, 210, 210),
        (231, 231, 231),
    )

    frozen_world = [__snow_biome]*12

    m_boreal_world = (
        __frozen,
        __m_taiga,
        __m_tundra,
        __m_taiga,
        __m_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    k_boreal_world = (
        __frozen,
        __k_taiga,
        __k_tundra,
        __k_taiga,
        __k_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    g_boreal_world = (
        __frozen,
        __g_taiga,
        __g_tundra,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
        __frozen,
    )

    a_boreal_world = (
        __frozen,
        __a_taiga,
        __a_tundra,
        __frozen,
        __a_tundra,
        __mountains,
        __mountains,
        __rocky,
        __rocks,
        __frozen,
        __frozen,
        __frozen,
    )

    f_boreal_world = (
        __frozen,
        __f_taiga,
        __f_tundra,
        __f_taiga,
        __rocky,
        __mountains,
        __rocks,
        __mountains,
        __rocky,
        __frozen,
        __frozen,
        __frozen,
    )


    m_cold_temperate_world = (
        __m_mediterranean,
        __m_savanna,
        __m_continental_steppe,
        __m_continental_forest,
        __m_continental_forest,
        __m_taiga,
        __m_taiga,
        __m_taiga,
        __m_tundra,
        __m_tundra,
        __mountains,
        __frozen,
    )

    k_cold_temperate_world = (
        __k_mediterranean,
        __k_savanna,
        __k_continental_steppe,
        __k_continental_forest,
        __k_continental_forest,
        __k_taiga,
        __k_taiga,
        __k_taiga,
        __k_tundra,
        __k_tundra,
        __mountains,
        __frozen,
    )

    g_cold_temperate_world = (
        __g_mediterranean,
        __g_savanna,
        __g_continental_steppe,
        __g_continental_forest,
        __g_continental_forest,
        __g_taiga,
        __g_taiga,
        __g_taiga,
        __g_tundra,
        __g_tundra,
        __mountains,
        __frozen,
    )

    a_cold_temperate_world = (
        __a_mediterranean,
        __a_savanna,
        __a_continental_steppe,
        __a_continental_forest,
        __mountains,
        __a_taiga,
        __rocks,
        __rocky,
        __rocks,
        __a_tundra,
        __mountains,
        __frozen,
    )

    f_cold_temperate_world = (
        __f_mediterranean,
        __f_savanna,
        __f_continental_steppe,
        __f_continental_forest,
        __f_continental_forest,
        __f_taiga,
        __mountains,
        __f_taiga,
        __rocky,
        __f_tundra,
        __mountains,
        __frozen,
    )



    m_temperate_world = (
        __m_tropical,
        __arid_desert,
        __semi_arid,
        __m_subtropical,
        __m_savanna,
        __m_mediterranean,
        __m_continental_steppe,
        __m_continental_forest,
        __m_taiga,
        __m_tundra,
        __mountains,
        __frozen,
    )

    k_temperate_world = (
        __k_tropical,
        __arid_desert,
        __semi_arid,
        __k_subtropical,
        __k_savanna,
        __k_mediterranean,
        __k_continental_steppe,
        __k_continental_forest,
        __k_taiga,
        __k_tundra,
        __mountains,
        __frozen,
    )

    g_temperate_world = (
        __g_tropical,
        __arid_desert,
        __semi_arid,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_continental_forest,
        __g_taiga,
        __g_tundra,
        __mountains,
        __frozen,
    )

    a_temperate_world = (
        __a_tropical,
        __arid_desert,
        __semi_arid,
        __a_subtropical,
        __a_savanna,
        __mountains,
        __a_continental_steppe,
        __rocks,
        __a_taiga,
        __a_tundra,
        __mountains,
        __frozen,
    )

    f_temperate_world = (
        __f_tropical,
        __arid_desert,
        __semi_arid,
        __f_subtropical,
        __f_savanna,
        __f_mediterranean,
        __arid_desert,
        __semi_arid,
        __f_continental_steppe,
        __f_continental_forest,
        __mountains,
        __frozen,
    )



    m_tropical_world = (
        __semi_arid,
        __arid_desert,
        __m_tropical,
        __m_subtropical,
        __m_savanna,
        __m_mediterranean,
        __m_continental_steppe,
        __m_subtropical,
        __m_tropical,
        __m_continental_forest,
        __m_continental_steppe,
        __m_tropical,
    )

    k_tropical_world = (
        __semi_arid,
        __arid_desert,
        __k_tropical,
        __k_subtropical,
        __k_savanna,
        __k_mediterranean,
        __k_continental_steppe,
        __k_subtropical,
        __k_tropical,
        __k_continental_forest,
        __k_continental_steppe,
        __k_tropical,
    )

    g_tropical_world = (
        __semi_arid,
        __arid_desert,
        __g_tropical,
        __g_subtropical,
        __g_savanna,
        __g_mediterranean,
        __g_continental_steppe,
        __g_subtropical,
        __g_tropical,
        __g_continental_forest,
        __g_continental_steppe,
        __g_tropical,
    )

    a_tropical_world = (
        __semi_arid,
        __arid_desert,
        __a_tropical,
        __rocky,
        __a_savanna,
        __a_mediterranean,
        __rocks,
        __a_subtropical,
        __mountains,
        __rocky,
        __a_continental_steppe,
        __mountains,
    )

    f_tropical_world = (
        __semi_arid,
        __arid_desert,
        __f_tropical,
        __f_subtropical,
        __f_savanna,
        __f_mediterranean,
        __f_continental_steppe,
        __f_subtropical,
        __f_tropical,
        __f_continental_forest,
        __rocky,
        __f_tropical,
    )



    m_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __m_savanna,
        __m_savanna,
        __semi_arid,
        __m_subtropical,
        __m_tropical,
        __semi_arid,
        __m_mediterranean,
        __mountains,
    )

    k_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __k_savanna,
        __k_savanna,
        __semi_arid,
        __k_subtropical,
        __k_tropical,
        __semi_arid,
        __k_mediterranean,
        __mountains,
    )

    g_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __g_savanna,
        __g_savanna,
        __semi_arid,
        __g_subtropical,
        __g_tropical,
        __semi_arid,
        __g_mediterranean,
        __mountains,
    )

    a_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __a_savanna,
        __arid_desert,
        __semi_arid,
        __a_subtropical,
        __a_tropical,
        __semi_arid,
        __a_mediterranean,
        __mountains,
    )

    f_dune_world = (
        __arid_desert,
        __semi_arid,
        __arid_desert,
        __semi_arid,
        __f_savanna,
        __rocky,
        __semi_arid,
        __f_subtropical,
        __f_tropical,
        __semi_arid,
        __f_mediterranean,
        __mountains,
    )

    @staticmethod
    def WaterLevelIncrease(s):
        return (s=="k")*0.2 + (s=="f")*(-0.2) + (s=="a")*(-0.4)
    
    @staticmethod
    def WaterDepthIncrease(g):
        depth = 0
        if g < 1 and g >= 0.5:
            return 0.1
        elif g >= 0 and g < 0.5:
            return 0.25
        elif g == 1:
            return 1
        elif g > 1 and g < 1.5:
            return -0.1
        elif g>=1.5 and g<2:
            return -0.25
        else:
            return -0.5
        
    @staticmethod
    def CloudVariation(t, flux, g):
        cloud_variation = 0

        if t < -30:
            cloud_variation += 0.2
        elif t < 0:
            cloud_variation += 0.1
        elif t < 10:
            cloud_variation += 0
        elif t < 22:
            cloud_variation -= 0.1
        elif t < 36:
            cloud_variation -= 0.2
        
        if g < 1 and g >= 0.5:
            cloud_variation -= 0.05
        elif g >= 0 and g < 0.5:
            cloud_variation -= 0.1
        elif g == 1:
            cloud_variation += 0
        elif g > 1 and g < 1.5:
            cloud_variation += 0.05
        elif g>=1.5 and g<2:
            cloud_variation += 0.1

        if flux>=1.5:
            cloud_variation -= 0.05
        elif flux<=0.5:
            cloud_variation += 0.05


        return cloud_variation

t, m, r, flux, star_type = 10, 1.5, 1, 1, 'f' 
filename = 'planet_presentation_2.png'
generate_planet(t, m, r, flux, star_type, filename)

def find_color(noise_value, color_map):
    for (lower, upper), color in color_map.items():
        if lower <= noise_value <= upper:
            return color
    return (0, 0, 0, 0)


#MAIN PAGE
def pocetna_stranica():
    global main_frame
    global new_page
    global new_page2

    for i in range(2):
        column = tk.Frame(root, bg=color)  
        column.grid(row=0, column=i, sticky="nsew")
        root.grid_columnconfigure(i, weight=1)

    main_frame = tk.Frame(root, bg=color)
    main_frame.grid(row=0, column=1, sticky="nsew")

    title_label = tk.Label(main_frame, text="Exoplanet Simulator 2000", font=("Arial", 48, 'bold'), fg='green', bg='white')
    title_label.grid(row=0, column=0, padx=20, pady=(20, 0), columnspan=2)

    subtitle_label = tk.Label(main_frame, text="NASA SpaceApps Hackathon 2023", font=("Arial", 24, 'bold'), fg='red', bg='white')
    subtitle_label.grid(row=1, column=0, columnspan=2, pady=10)

    subtitle1_label = tk.Label(main_frame, text="Made by: A. Brzica, E. Donev, D.Keran, L. Marunjić", font=("Arial", 12, 'bold'), fg='blue', bg='white')
    subtitle1_label.grid(row=2, column=0, columnspan=2, pady=10)

    image_a = tk.PhotoImage(file="pok5.png")
    image_label = tk.Label(main_frame, image=image_a, bg='white')
    image_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="n")

    button_width = 25
    button_height = 5

    button_a = tk.Button(main_frame, text="Explore\nHabitable Exoplanets", command=lambda: open_pageA("#ffffff"), font=("Arial", 18, 'bold'), bg='white', fg='blue', width=button_width, height=button_height, relief=tk.RAISED)
    button_b = tk.Button(main_frame, text="Create Your\nOwn Exoplanet", command=lambda: open_pageB("#ffffff"), font=("Arial", 18, 'bold'), bg='white', fg='red', width=button_width, height=button_height, relief=tk.RAISED)
    exit_button = tk.Button(main_frame, text="Exit", command=print_window_size, font=("Arial", 16, 'bold'), bg='white', fg='green', padx=10, pady=5, relief=tk.RAISED)

    button_a.grid(row=4, column=0, padx=100, pady=5, sticky="n")
    button_b.grid(row=4, column=1, padx=100, pady=5, sticky="n")
    exit_button.grid(row=5, column=0, columnspan=2, pady=10, sticky="n")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.mainloop()

#KEPLER DATA BASE PLANETS PAGE
def open_pageA(color):
    global main_frame
    global new_page

    main_frame.grid_forget()
    new_page = tk.Frame(root, bg=color)
    new_page.grid(row=0, column=1, sticky="nsew")
    
    def povratak_na_pocetnu():
            main_frame.grid_forget()
            pocetna_stranica()

    return_button = tk.Button(new_page, text="Return to Main Page", command=povratak_na_pocetnu, bg=color, fg='green', font=("Arial", 12, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    return_button.grid(row=0, column=0,columnspan=4, pady=10, sticky="n")

    title_label = tk.Label(new_page, text="What habitable exoplanet do you want to explore? ", font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0))
    
    subtitle_label = tk.Label(new_page, text="These 24 planets are considered most habitable. Their data was collected from [1]", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label.grid(row=2, column=0, columnspan=4, padx=20, pady=(20, 0))

    subtitle2_label = tk.Label(new_page, text="------", font=("Arial", 18, 'bold'), fg='white', bg=color)
    subtitle2_label.grid(row=3, column=0, columnspan=4, pady=5)
    lista=["Teegarden's Star b", "TOI-700 d", "Kepler-1649 c", "TRAPPIST-1 d", "LP 890-9 c",
    "Proxima Cen b", "K2-72 e", "GJ 1002 b", "GJ 1061 d", "GJ 1061 c", "Ross 128 b",
    "GJ 273 b", "Kepler-296 e", "TRAPPIST-1 e", "Kepler-442 b", "GJ 667 C f",
    "Kepler-62 f", "TRAPPIST-1 f", "Teegarden's Star c", "Kepler-1229 b", "Kepler-186 f",
    "GJ 667 C e", "GJ 1002 c", "TRAPPIST-1 g"]

    for i in range(6):
        for j in range(4):
            button_text = lista[i*4+j]
            broj_u_listi = i*4+j
            subpage_color = color 
            button = tk.Button(new_page, text=button_text, bg=color, fg='black', font=("Arial", 14, 'bold'), padx=10, pady=10, width=23, height=2, relief=tk.RAISED, command=lambda bt=button_text, br=broj_u_listi: open_subpageA(bt, br, lista, subpage_color))
            button.grid(row=i + 4, column=j, padx=1, pady=1, sticky="nsew")

    root.mainloop()

#DATA VISUALIZATION - KEPLER DATABASE
#---------------------- 
def open_subpageA(button_text, broj_u_listi, lista, color):
    global main_frame
    global new_page
    global new_page2
    main_frame.grid_forget()
    new_page.grid_forget()
    subpage = tk.Frame(root, bg=color)
    subpage.grid(row=0, column=1, sticky="nsew")

    def return_to_previous():
        subpage.grid_forget()  
        open_pageA(color)

    return_button = tk.Button(subpage, text="Return to Previous Page", command=return_to_previous, bg=color, fg='green', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    return_button.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

    title_label = tk.Label(subpage, text="Information about exoplanet: " + lista[broj_u_listi], font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=3, padx=20, pady=(20, 0))

    subtitle_label1 = tk.Label(subpage, text="Basic data on chosen planet", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label1.grid(row=2, column=0, padx=50, pady=(40, 0), sticky="e")

    display_dataA(subpage, broj_u_listi)
    
    subtitle_label4 = tk.Label(subpage, text="This data was gathered in the \nNASA Exoplanet Archive." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label4.grid(row=10, column=0, padx=50, pady=(10, 0), sticky="e")
    subtitle_label5 = tk.Label(subpage, text="The Archive contains datasets \non over 130,041,578 celestial \nobjects." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label5.grid(row=11, column=0, padx=50, pady=(10, 0), sticky="e")

    subtitle_label2 = tk.Label(subpage, text="Revolution simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label2.grid(row=2, column=1, padx=50, pady=(40, 0), sticky="ew")

    create_kepler_animation(radius_planet[broj_u_listi]*0.1, 2, 1, semi_major_axis[broj_u_listi]*150, eccentricity[broj_u_listi], 'ivory', spclass_star[broj_u_listi], orbital_period[broj_u_listi], 'Exoplanet_'+name_planet[broj_u_listi]+'.gif')
    gif_path='Exoplanet_'+name_planet[broj_u_listi]+'.gif'
    display_gif(subpage, gif_path)

    subtitle_label7 = tk.Label(subpage, text="Planet and star are not\n in scale." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label7.grid(row=10, column=1, padx=50, pady=(10, 0), sticky="e")
    subtitle_label8 = tk.Label(subpage, text="This part of the code\n needs an additional \nimplementation." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label8.grid(row=11, column=1, padx=50, pady=(10, 0), sticky="e")
    
    subtitle_label3 = tk.Label(subpage, text="Biology simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label3.grid(row=2, column=2, padx=50, pady=(40, 0), sticky="w")

    generate_planet(surface_temperature[broj_u_listi], mass_planet[broj_u_listi], radius_planet[broj_u_listi], flux_planet[broj_u_listi], spclass_star_lower[broj_u_listi], 'Exoplanet_'+name_planet[broj_u_listi]+'.png')
    image_path="Exoplanet_"+name_planet[broj_u_listi]+".png"
    pil_image = Image.open(image_path)
    resized_image = resize_image(pil_image, width=300, height=300)
    image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(subpage, image=image, bg='white')
    image_label.grid(row=3, column=2, padx=20, pady=10, sticky="n")
    image_label.image = image

    subtitle_label9 = tk.Label(subpage, text="This is the generated\n map of exoplanet." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label9.grid(row=10, column=2, padx=50, pady=(10, 0), sticky="e")
    subtitle_label10 = tk.Label(subpage, text="It is based on data\n shown in column \none." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label10.grid(row=11, column=2, padx=50, pady=(10, 0), sticky="e")
    

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


def resize_image(image, width, height):
    """
    Resize the given image to the specified width and height.

    Args:
        image (PIL.Image): The image to resize.
        width (): The desired width of the resized image.
        height (): The desired height of the resized image.

    Returns:
        PIL.Image: The resized image.
    """
    return image.resize((width, height), Image.LANCZOS)

def display_dataA(subpage, broj_u_listi, label_color='green', data_color='black'):
    labels_data = [
        ("Mass (Me):", mass_planet[broj_u_listi]),
        ("Radius (Re):", radius_planet[broj_u_listi]),
        ("Semi-Major Axis (AU):", semi_major_axis[broj_u_listi]),
        ("Orbital Period (Days):", orbital_period[broj_u_listi]),
        ("Surface Temperature (C):", surface_temperature[broj_u_listi]),
        ("Spectral Class:", spclass_star[broj_u_listi]),
        ("Star Mass (Ms):", mass_star[broj_u_listi])
    ]
    
    combined_text = "\n".join([f"{label_text} {data_value}" for label_text, data_value in labels_data])
    
    label = tk.Label(subpage, text=combined_text, font=("Arial", 16, "bold"), fg="black", bg=color)
    label.grid(row=3, column=0, padx=50, pady=(10, 0), sticky="w")


#DATA INPUT - USER GENERATED PLANET
#---------------------- 
def open_pageB(color):
    global main_frame
    global new_page
    global new_page2
    global name_exoplanet
    
    main_frame.grid_forget()
    new_page2 = tk.Frame(root, bg=color)
    new_page2.grid(row=0, column=1, sticky="nsew")

    def return_to_previous():
        main_frame.grid_forget()
        pocetna_stranica()

    def display_data():
        global name_exoplanet1
        global mass_planet1
        global radius_planet1
        global semi_major_axis1
        global orbital_period1
        global surface_temperature1
        global spclass_star1
        global flux_planet1
        global eccentricity_orbit1

        
        mass_planet1 = float(input_box1.get())
        radius_planet1 = float(input_box2.get())
        semi_major_axis1 = float(input_box3.get())
        orbital_period1 = float(input_box4.get())
        surface_temperature1 = float(input_box5.get())
        spclass_star1 = input_box6.get()
        flux_planet1 = float(input_box7.get())
        eccentricity_orbit1 = float(input_box8.get())
        name_exoplanet1 =   input_box9.get()

    return_button = tk.Button(new_page2, text="Return to Previous Page", command=return_to_previous, bg=color, fg='green', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    return_button.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

    title_label = tk.Label(new_page2, text="Input the data of the planet you want to create: ", font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0))

    #prvi red inputa

    input_label1 = tk.Label(new_page2, text="Mass of planet (Me):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label1.grid(row=2, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box1 = tk.Entry(new_page2, font=("Arial", 14))
    input_box1.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label2 = tk.Label(new_page2, text="Radius of planet(Re):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label2.grid(row=2, column=1, padx=20, pady=(40, 0), sticky="ew")

    input_box2 = tk.Entry(new_page2, font=("Arial", 14))
    input_box2.grid(row=3, column=1, padx=20, pady=(0, 10), sticky="ew")

    input_label3 = tk.Label(new_page2, text="Semi-major axis of planet (AU):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label3.grid(row=2, column=2, padx=20, pady=(40, 0), sticky="ew")

    input_box3 = tk.Entry(new_page2, font=("Arial", 14))
    input_box3.grid(row=3, column=2, padx=20, pady=(0, 10), sticky="ew")

    #drugi red inputa

    input_label4 = tk.Label(new_page2, text="Orbital period of planet (Days):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label4.grid(row=4, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box4 = tk.Entry(new_page2, font=("Arial", 14))
    input_box4.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label5 = tk.Label(new_page2, text="Planet surface temperature (C):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label5.grid(row=4, column=1, padx=20, pady=(40, 0), sticky="ew")

    input_box5 = tk.Entry(new_page2, font=("Arial", 14))
    input_box5.grid(row=5, column=1, padx=20, pady=(0, 10), sticky="ew")

    input_label6 = tk.Label(new_page2, text="Type of host star:", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label6.grid(row=4, column=2, padx=20, pady=(40, 0), sticky="ew")

    input_box6 = tk.Entry(new_page2, font=("Arial", 14))
    input_box6.grid(row=5, column=2, padx=10, pady=(0, 10), sticky="ew")

    #treci red inputa

    input_label7 = tk.Label(new_page2, text="Planet Flux (Fe):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label7.grid(row=6, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box7 = tk.Entry(new_page2, font=("Arial", 14))
    input_box7.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label8 = tk.Label(new_page2, text="Eccentricity of planet orbit:", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label8.grid(row=6, column=1, padx=20, pady=(40, 0), sticky="ew")

    input_box8 = tk.Entry(new_page2, font=("Arial", 14))
    input_box8.grid(row=7, column=1, padx=20, pady=(0, 10), sticky="ew")

    input_label9 = tk.Label(new_page2, text="Name of your exoplanet:", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label9.grid(row=6, column=2, padx=20, pady=(40, 0), sticky="ew")

    input_box9 = tk.Entry(new_page2, font=("Arial", 14))
    input_box9.grid(row=7, column=2, padx=20, pady=(0, 10), sticky="ew")
    
    next_button = tk.Button(new_page2, text="Save data", command=display_data, bg="green", fg='white', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    next_button.grid(row=8, column=0, columnspan=3, pady=20, sticky="ew")

    visualisation_button = tk.Button(new_page2, text="Display Data", command=open_subpageB, bg="red", fg='white', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    visualisation_button.grid(row=9, column=0, columnspan=3, pady=20, sticky="nsew")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

#što se prikazuje nakon gumba na B stranici

#DATA VISUALIZATION - USER GENERATED PLANET
#---------------------- 
def open_subpageB():
    global main_frame
    global new_page
    global new_page2
    global name_exoplanet1
    color="white"
    main_frame.grid_forget()
    new_page2.grid_forget()
    subpage2 = tk.Frame(root, bg=color)
    subpage2.grid(row=0, column=1, sticky="nsew")

    def return_to_previous():
        subpage2.grid_forget()  
        open_pageB(color)

    return_button = tk.Button(subpage2, text="Return to Previous Page", command=return_to_previous, bg=color, fg='green', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    return_button.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

    title_label = tk.Label(subpage2, text="Data on Exoplanet "+name_exoplanet1, font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0))

    subtitle_label1 = tk.Label(subpage2, text="Basic data on chosen planet", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label1.grid(row=2, column=0, padx=50, pady=(40, 0), sticky="e")

    display_dataB(subpage2)

    subtitle_label4 = tk.Label(subpage2, text="This data was inputed by \nthe user." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label4.grid(row=10, column=0, padx=50, pady=(10, 0), sticky="e")
    subtitle_label5 = tk.Label(subpage2, text="Using this data we \n simulate your exoplanet." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label5.grid(row=11, column=0, padx=50, pady=(10, 0), sticky="e")


    subtitle_label2 = tk.Label(subpage2, text="Revolution simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label2.grid(row=2, column=1, padx=50,pady=(40, 0), sticky="ew")

    create_kepler_animation(radius_planet1, 2, 2, semi_major_axis1*100, eccentricity_orbit1, 'ivory', spclass_star1, orbital_period1, 'Exoplanet_'+name_exoplanet1+'.gif')
    gif_path='Exoplanet_'+name_exoplanet1+'.gif'
    display_gif(subpage2, gif_path)

    subtitle_label6 = tk.Label(subpage2, text="This simulation was created \nusing data inputed\n by the user." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label6.grid(row=10, column=1, padx=50, pady=(10, 0), sticky="e")
    subtitle_label7 = tk.Label(subpage2, text="Planet and star radius are not\n to scale. " , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label7.grid(row=11, column=1, padx=50, pady=(10, 0), sticky="e")

    subtitle_label3 = tk.Label(subpage2, text="Biology simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label3.grid(row=2, column=2, padx=50,pady=(40, 0), sticky="w")

    generate_planet(surface_temperature1, mass_planet1, radius_planet1, flux_planet1, spclass_star1.lower(), 'Exoplanet_'+name_exoplanet1+'.png')
    image_path="Exoplanet_"+name_exoplanet1+".png"
    pil_image = Image.open(image_path)
    resized_image = resize_image(pil_image, width=270, height=270)
    image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(subpage2, image=image, bg='white')
    image_label.grid(row=3, column=2, padx=20, pady=10, sticky="n")
    image_label.image = image
    
    subtitle_label8 = tk.Label(subpage2, text="This is the generated\n map of exoplanet." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label8.grid(row=10, column=2, padx=50, pady=(10, 0), sticky="e")
    subtitle_label9 = tk.Label(subpage2, text="It is based on data\n shown in column \none. " , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label9.grid(row=11, column=2, padx=50, pady=(10, 0), sticky="e")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

#USER INPUT DATA DISPLAY
#----------------------   
def display_dataB(subpage2, label_color='green', data_color='black'):
    labels_data = [
        ("Mass (Mz):", mass_planet1),
        ("Radius (Rz):", radius_planet1),
        ("Flux (Fe):", flux_planet1),
        ("Semi-Major Axis (AU):", semi_major_axis1),
        ("Orbital Period (Days):", orbital_period1),
        ("Surface Temperature (C):", surface_temperature1),
        ("Spectral Class:", spclass_star1),
    ]
    combined_text = "\n".join([f"{label_text} {data_value}" for label_text, data_value in labels_data])
    
    label = tk.Label(subpage2, text=combined_text, font=("Arial", 16, "bold"), fg="black", bg=color)
    label.grid(row=3, column=0, padx=50, pady=(10, 0), sticky="w")


#GIF DISPLAY
#----------------------
def display_gif(subpage, gif_path):
    try:
        gif_image = Image.open(gif_path)
        gif_frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(gif_image)]

        # Create a label to display the animated GIF
        gif_label = tk.Label(subpage, bg='white')
        gif_label.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="e")

        def update_frame(frame_num=0):
            gif_label.config(image=gif_frames[frame_num])
            frame_num = (frame_num + 1) % len(gif_frames)
            subpage.after(100, update_frame, frame_num)  # Change the delay to control animation speed

        update_frame()  # Start the animation

    except Exception as e:
        print("Error displaying GIF:", str(e))

#kad ovu funkciju maknem padne kod?
def print_window_size():
    global main_frame
    global new_page

    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.destroy()

pocetna_stranica()
root.mainloop()
