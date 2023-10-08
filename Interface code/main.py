import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageSequence
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.animation import PillowWriter
import numpy as np

color="white"
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
                
mass_planet = [float(x) for x in mass_planet]
radius_planet = [float(x) for x in radius_planet]
semi_major_axis = [float(x) for x in semi_major_axis]
orbital_period = [float(x) for x in orbital_period]
surface_temperature = [float(x) for x in surface_temperature]
mass_star = [float(x) for x in mass_star]
eccentricity = [float(x) for x in eccentricity]
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

    image_path = "mjau.png"
    img = Image.open(image_path)
    image_b = ImageTk.PhotoImage(img)
    
    image_label = tk.Label(subpage, image=image_b, bg=color)
    image_label.grid(row=3, column=2, padx=10, pady=10, sticky="e")

    subtitle_label9 = tk.Label(subpage, text="This is the generated\n map of exoplanet." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label9.grid(row=10, column=2, padx=50, pady=(10, 0), sticky="e")
    subtitle_label10 = tk.Label(subpage, text="It is based on data\n shown in column \none." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label10.grid(row=11, column=2, padx=50, pady=(10, 0), sticky="e")
    

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)


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
        global mass_star1
        global eccentricity_orbit1
        
        mass_planet1 = float(input_box1.get())
        radius_planet1 = float(input_box2.get())
        semi_major_axis1 = float(input_box3.get())
        orbital_period1 = float(input_box4.get())
        surface_temperature1 = float(input_box5.get())
        spclass_star1 = input_box6.get()
        mass_star1 = float(input_box7.get())
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

    input_label7 = tk.Label(new_page2, text="Mass of host star (Ms):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
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
    
    next_button = tk.Button(new_page2, text="Pohrani podatke", command=display_data, bg="green", fg='white', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
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
        ("Semi-Major Axis (AU):", semi_major_axis1),
        ("Orbital Period (Days):", orbital_period1),
        ("Surface Temperature (C):", surface_temperature1),
        ("Spectral Class:", spclass_star1),
        ("Star Mass (Ms):", mass_star1)
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
