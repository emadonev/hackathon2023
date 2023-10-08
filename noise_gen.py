import random
import noise
import numpy as np
from noise import pnoise2
import planet_type as pt
from scipy.constants import G as G


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

        sea_level = abs((1 / (1.6 * 10 ** 8)) * t * (t + 30) * (t - 60) * (t - 50) * (t + 60)) + pt.PlanetType.WaterLevelIncrease(star_type) # Calculate the sea level threshold based on average temperature (t)

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
