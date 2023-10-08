# Space Apps Hackathon 2023: Habitable Exoplanets - exploring worlds beyond our own

Our team created a Tkinter interface in Python. The interface has 2 main components: the exploration and creation parts. The exploration part consists of a list of 24 potentially  habitable exoplanets around low mass stars. The data for these planets was taken from https://exoplanetarchive.ipac.caltech.edu, and the list of exoplanets was accessed from this website: https://phl.upr.edu/projects/habitable-exoplanets-catalog. 

If we pick an exoplanet, another interface opens which shows the basic information for every exoplanet (mass, radius, semi-major axis, orbital period, surface temperature, spectral class, star mass). Next to the basic information we showcase a simulation (not to scale) of the revolution of this exoplanet around its host star. The host star takes on different colors based on its spectral type, and the planet orbits the star so that every day is one second. 

Next to the revolution simulation is a generated map of our planet based on various parameters (temperature, mass, radius, flux, star type). For example, different masses and radii of exoplanets change the gravitational acceleration on the planets which can either cause very high mountaneous planets or very flat planets. The planets also contain simulations of vegetation (potential life) based on the parameters but especially on the spectral type of the star due to different peak wavelength emissions. We used the code from: https://github.com/KornelSzyszka/PlanetGenerator. We changed the code by changing the colors, adding more spectral types of stars (F and A), adding more parameters like the gravitational constant, mass, radius, etc. and we enabled more complex planet generation. 

If we choose to create our own exoplanet, an interface pops up which enables users to input the necessary parameters (mass, radius, semi-major axis, orbital period, planet surface temperature, spectral type of star, mass of host star, radius of host star, name of your exoplanet). The same interface as with exploring already found exoplanets pops up, with all the data adjusted for the user's input. 

In order to run this app, you need to run `main.py`, and have the following dependencies and libraries installed:
- noise
- numpy
- matplotlib.pyplot
- pillow (PIL)
- tkinter
- scipy
- itertools