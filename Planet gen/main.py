import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from itertools import product
import noise_gen as ng
import body_gen as bg
from scipy.constants import G as G


class PlanetGeneratorApp:
    def __init__(self, input_root):
        # Initialize instance variables for GUI elements
        self.output_image = None  # Placeholder for the generated planet image
        self.tk_image = None  # Placeholder for a Tkinter-compatible image
        self.save_button = None  # Button to save the generated planet image
        self.generate_button = None  # Button to generate a new planet
        self.temperature_scale = None  # Scale to adjust the planet's average temperature
        self.resolution_scale = None  # Scale to adjust the planet's resolution
        self.right_frame = None  # Frame to contain GUI elements
        self.canvas_scale = None  # Canvas to display the generated planet image
        self.mass_scale = None #Scale mass of the planet
        self.radius_scale = None #Scale radius of the planet
        self.flux_scale = None #Scale solar flux

        self.persistence = 0.7
        self.octaves = 7

        # Initialize the root window for the application
        self.root = input_root
        self.root.title("Planet Generator")  # Set the title of the application window
        self.root.iconbitmap("resources/icon.ico")  # Set the application icon
        self.root.configure(bg="#333333")  # Set the background color of the window
        self.root.option_add("*Font", "Arial 10")  # Set the default font for all elements

        # Define custom button style for consistency
        custom_button_style = {
            "background": "#666666",  # Background color of buttons
            "foreground": "#FFFFFF",  # Text color of buttons
            "activebackground": "#888888",  # Background color when button is clicked
            "activeforeground": "#FFFFFF",  # Text color when button is clicked
            "bd": 0,  # Border width
        }
        self.root.option_add("*TButton", custom_button_style)  # Apply custom button style

        # Load and resize a space background image for the application
        self.background_image = Image.open("resources/space_background.png")
        self.background_image = self.background_image.resize((1024, 1024), Image.LANCZOS)
        self.background_tk_image = ImageTk.PhotoImage(self.background_image)

        # Initialize default values for planet generation parameters
        self.resolution = 1024  # Default resolution of the generated planet image
        self.avg_temperature = 15  # Default average temperature of the planet (Earth)
        self.mass = 1 #Mass of the planet
        self.radius = 1 #Radius of the planet
        self.flux = 1 #Solar flux in earth flux
        self.star_type = tk.StringVar()  # Variable to store the selected star type
        self.star_type.set("g")  # Set the default star type to "g"

        # Create the GUI elements for the application
        self.create_widgets()  # Call the create_widgets() method to build the GUI

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=self.resolution, height=self.resolution)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_tk_image)
        self.canvas.pack(side=tk.LEFT)

        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(side=tk.RIGHT, padx=10)

        tk.Label(self.right_frame, text="Resolution:").pack()
        self.resolution_scale = tk.Scale(self.right_frame, from_=128, to=1024, orient=tk.HORIZONTAL)
        self.resolution_scale.set(self.resolution)
        self.resolution_scale.pack()

        tk.Label(self.right_frame, text="Average Temperature (°C):").pack()
        self.temperature_scale = tk.Scale(self.right_frame, from_=-50, to=50, orient=tk.HORIZONTAL)
        self.temperature_scale.set(self.avg_temperature)
        self.temperature_scale.pack()

        tk.Label(self.right_frame, text="Planet Mass (Earth Masses):").pack()
        self.mass_scale = tk.Scale(self.right_frame, from_=-0.1, to=5.0, orient=tk.HORIZONTAL) #In terms of Earth masses
        self.mass_scale.set(self.mass)
        self.mass_scale.pack()

        tk.Label(self.right_frame, text="Planet Radius (Earth Radiuses):").pack()
        self.radius_scale = tk.Scale(self.right_frame, from_=-0.1, to=5.0, orient=tk.HORIZONTAL) #In terms of Earth radiuses
        self.radius_scale.set(self.radius)
        self.radius_scale.pack()

        tk.Label(self.right_frame, text="Solar flux (Earth flux):").pack()
        self.flux_scale = tk.Scale(self.right_frame, from_=-0.1, to=5.0, orient=tk.HORIZONTAL) #In Earth flux (1400 W/m**2)
        self.flux_scale.set(self.flux)
        self.flux_scale.pack()

        tk.Label(self.right_frame, text="Star Type:").pack()
        star_types = [("M", "m"), ("K", "k"), ("G", "g"), ("F", "f"), ("A", "a")] 
        for star_type, value in star_types:
            tk.Radiobutton(self.right_frame, text=star_type, variable=self.star_type, value=value).pack(anchor=tk.W)

        self.generate_button = tk.Button(self.right_frame, text="Generate Planet", command=self.generate_planet)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(self.right_frame, text="Save Planet", command=self.save_planet)
        self.save_button.pack()

    def generate_planet(self):
        self.resolution = self.resolution_scale.get()
        self.avg_temperature = self.temperature_scale.get()
        self.mass = self.mass_scale.get() #Mass of the planet
        self.radius = self.radius_scale.get() #Radius of the planet
        self.flux = self.flux_scale.get() #Solar flux

        water_normalized_noise, land_normalized_noise = ng.NoiseGen.generate_noise(self.resolution, self.avg_temperature, self.mass, self.radius, self.flux, self.octaves, self.persistence, self.star_type.get())
        clouds_noise_map = ng.NoiseGen.generate_clouds_noise(self.resolution, self.avg_temperature, self.mass, self.radius, self.flux, self.octaves, self.persistence)
        water_map, land_map = bg.BodyGen.generate_colors(self.avg_temperature, self.star_type.get(), self.mass, self.radius, self.flux)
        cloud_map = bg.BodyGen.generate_clouds(self.avg_temperature, self.star_type.get(), self.mass, self.radius, self.flux)

        land_image = Image.new("RGBA", (self.resolution, self.resolution))
        clouds_image = Image.new("RGBA", (self.resolution, self.resolution))
        water_image = Image.new("RGBA", (self.resolution, self.resolution))

        land_array = land_image.load()
        clouds_array = clouds_image.load()
        water_array = water_image.load()

        for y, x in product(range(self.resolution), repeat=2):
            planet_noise_value = land_normalized_noise[y, x]
            land_array[x, y] = self.find_color(planet_noise_value, land_map)

            cloud_noise_value = clouds_noise_map[y, x]
            clouds_array[x, y] = self.find_color(cloud_noise_value, cloud_map)

            water_noise_value = water_normalized_noise[y, x]
            water_array[x, y] = self.find_color(water_noise_value, water_map)

        shadow_image = Image.open("./resources/shadow.png").resize((self.resolution, self.resolution), Image.LANCZOS)
        self.output_image = Image.alpha_composite(water_image, land_image)
        self.output_image = Image.alpha_composite(self.output_image, clouds_image)
        self.output_image = Image.alpha_composite(self.output_image, shadow_image)

        self.display_image(self.output_image)

    @staticmethod
    def find_color(noise_value, color_map):
        for (lower, upper), color in color_map.items():
            if lower <= noise_value <= upper:
                return color
        return 0, 0, 0, 0

    def display_image(self, image):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        x_center = (canvas_width - self.resolution) / 2
        y_center = (canvas_height - self.resolution) / 2

        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(x_center, y_center, anchor=tk.NW, image=self.tk_image)

    def save_planet(self):
        if self.tk_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
            if file_path:
                self.output_image.save(file_path)


if __name__ == "__main__":
    root = tk.Tk()
    app = PlanetGeneratorApp(root)
    root.mainloop()
