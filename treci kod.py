import tkinter as tk
from tkinter import PhotoImage

color="white"
lista=[]
mass_planet= ['6.2708e+24', '9.3764e+24', '7.1666e+24', '2.3292e+24', '1.511e+26', '7.5847e+24', '1.3199e+25', '6.45e+24', '9.7944e+24', '1.0392e+25', '8.3611e+24', '1.726e+25', '1.7678e+25', '4.1208e+24', '1.4094e+25', '1.5169e+25', '2.0903e+26', '6.2111e+24', '6.6291e+24', '1.5169e+25', '1.0212e+25', '1.5169e+25', '8.1222e+24', '7.8833e+24']
radius_planet= ['6.4984e+06', '7.2629e+06', '6.7533e+06', '4.9694e+06', '8.7283e+06', '6.8807e+06', '8.2186e+06', '6.5621e+06', '7.3266e+06', '7.5178e+06', '7.0718e+06', '9.6202e+06', '9.6839e+06', '5.8613e+06', '8.6008e+06', '9.238e+06', '8.9831e+06', '6.6258e+06', '6.6258e+06', '8.9194e+06', '7.4541e+06', '9.238e+06', '7.0081e+06', '7.1992e+06']
semi_major_axis= ['37400', '4.3384e+09', '1.2716e+10', '3.2912e+09', '3.8896e+09', '7.48e+09', '4.488e+09', '3.4408e+09', '3.4408e+09', '2.992e+09', '3.8896e+09', '5.6848e+09', '3.5904e+09', '4.1888e+09', '7.7792e+09', '1.1968e+10', '6.1336e+09', '5.5352e+09', '4.7872e+09', '1.0023e+10', '1.7952e+10', '8.976e+09', '1.0023e+10', '6.732e+09']
orbital_period= ['4.2336e+05', '3.2314e+06', '1.6848e+06', '3.456e+05', '7.344e+05', '9.6768e+05', '2.0909e+06', '8.8992e+05', '1.1232e+06', '5.7888e+05', '8.5536e+05', '1.607e+06', '2.9462e+06', '5.2704e+05', '9.7027e+06', '3.2832e+06', '2.3095e+07', '7.9488e+05', '9.8496e+05', '7.4995e+06', '1.1223e+07', '5.3741e+06', '1.8317e+06', '1.0714e+06']
surface_temperature= ['25', '5', '30', '23', '8', '-16', '34', '-12', '-26', '38', '44', '19', '9', '-15', '-10', '-24', '-43', '-48', '-48', '-56', '-61', '-60', '-68', '-69']
spclass_star= ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'K', 'M', 'K', 'M', 'M', 'M', 'M', 'M', 'M']
mass_star= ['1.5912e+29', '8.1549e+29', '1.7901e+29', '1.5912e+29', '2.1879e+29', '2.3868e+29', '6.9615e+29', '2.1879e+29', '2.1879e+29', '2.1879e+29', '2.9835e+29', '5.1714e+29', '2.3868e+29', '1.5912e+29', '7.7571e+29', '6.5637e+29', '1.3724e+30', '1.5912e+29', '1.5912e+29', '1.989e+29', '3.7791e+29', '6.5637e+29', '2.1879e+29', '1.5912e+29']

root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Hackathon program")

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

#stranice s gumbova na stranici A
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

    display_data(subpage, broj_u_listi)
    
    subtitle_label4 = tk.Label(subpage, text="This data was gathered in the \nNASA Exoplanet Archive." , font=("Arial", 18, 'bold'), fg='green', bg=color)
    subtitle_label4.grid(row=10, column=0, padx=50, pady=(10, 0), sticky="e")
    subtitle_label5 = tk.Label(subpage, text="The Archive contains datasets \non over 130,041,578 celestial \nobjects." , font=("Arial", 18, 'bold'), fg='red', bg=color)
    subtitle_label5.grid(row=11, column=0, padx=50, pady=(10, 0), sticky="e")

    subtitle_label2 = tk.Label(subpage, text="Revolution simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label2.grid(row=2, column=1, padx=50, pady=(40, 0), sticky="ew")

    subtitle_label3 = tk.Label(subpage, text="Biology simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label3.grid(row=2, column=2, padx=50, pady=(40, 0), sticky="w")

    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

def display_data(subpage, broj_u_listi, label_color='green', data_color='black'):
    labels_data = [
        ("Mass (kg):", mass_planet[broj_u_listi]),
        ("Radius (m):", radius_planet[broj_u_listi]),
        ("Semi-Major Axis (m):", semi_major_axis[broj_u_listi]),
        ("Orbital Period (s):", orbital_period[broj_u_listi]),
        ("Surface Temperature (K):", surface_temperature[broj_u_listi]),
        ("Spectral Class:", spclass_star[broj_u_listi]),
        ("Star Mass (kg):", mass_star[broj_u_listi])
    ]
    row = 3  
    for label_text, data_value in labels_data:
        combined_text = f"{label_text} {data_value}"
        label = tk.Label(subpage, text=combined_text, font=("Arial", 16, "bold"), fg="black", bg=color)
        label.grid(row=row, column=0, padx=50, pady=(10,0), sticky="w")
        row += 1
    

#stranica gumba B
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
        global name_exoplanet
        mass_planet = input_box1.get()
        radius_planet = input_box2.get()
        semi_major_axis = input_box3.get()
        orbital_period = input_box4.get()
        surface_temperature = input_box5.get()
        spclass_star = input_box6.get()
        mass_star = input_box7.get()
        radius_star = input_box8.get()
        name_exoplanet = input_box9.get()

    return_button = tk.Button(new_page2, text="Return to Previous Page", command=return_to_previous, bg=color, fg='green', font=("Arial", 14, 'bold'), padx=10, pady=5, relief=tk.RAISED)
    return_button.grid(row=0, column=0, columnspan=4, pady=10, sticky="n")

    title_label = tk.Label(new_page2, text="Input the data of the planet you want to create: ", font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0))

    #prvi red inputa

    input_label1 = tk.Label(new_page2, text="Mass of planet (kg):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label1.grid(row=2, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box1 = tk.Entry(new_page2, font=("Arial", 14))
    input_box1.grid(row=3, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label2 = tk.Label(new_page2, text="Radius of planet(m):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label2.grid(row=2, column=1, padx=20, pady=(40, 0), sticky="ew")

    input_box2 = tk.Entry(new_page2, font=("Arial", 14))
    input_box2.grid(row=3, column=1, padx=20, pady=(0, 10), sticky="ew")

    input_label3 = tk.Label(new_page2, text="Semi-major axis of planet (m):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label3.grid(row=2, column=2, padx=20, pady=(40, 0), sticky="ew")

    input_box3 = tk.Entry(new_page2, font=("Arial", 14))
    input_box3.grid(row=3, column=2, padx=20, pady=(0, 10), sticky="ew")

    #drugi red inputa

    input_label4 = tk.Label(new_page2, text="Orbital period of planet (days):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label4.grid(row=4, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box4 = tk.Entry(new_page2, font=("Arial", 14))
    input_box4.grid(row=5, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label5 = tk.Label(new_page2, text="Planet surface temperature (K):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label5.grid(row=4, column=1, padx=20, pady=(40, 0), sticky="ew")

    input_box5 = tk.Entry(new_page2, font=("Arial", 14))
    input_box5.grid(row=5, column=1, padx=20, pady=(0, 10), sticky="ew")

    input_label6 = tk.Label(new_page2, text="Type of host star:", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label6.grid(row=4, column=2, padx=20, pady=(40, 0), sticky="ew")

    input_box6 = tk.Entry(new_page2, font=("Arial", 14))
    input_box6.grid(row=5, column=2, padx=10, pady=(0, 10), sticky="ew")

    #treci red inputa

    input_label7 = tk.Label(new_page2, text="Mass of host star (m):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    input_label7.grid(row=6, column=0, padx=20, pady=(40, 0), sticky="ew")

    input_box7 = tk.Entry(new_page2, font=("Arial", 14))
    input_box7.grid(row=7, column=0, padx=20, pady=(0, 10), sticky="ew")

    input_label8 = tk.Label(new_page2, text="Radius of host star (m):", font=("Arial", 18, 'bold'), fg='blue', bg=color)
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

def open_subpageB():
    global main_frame
    global new_page
    global new_page2
    global name_exoplanet
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

    title_label = tk.Label(subpage2, text="Data on Exoplanet "+name_exoplanet, font=("Arial", 24, 'bold'), fg='red', bg=color)
    title_label.grid(row=1, column=0, columnspan=4, padx=20, pady=(20, 0))

    subtitle_label1 = tk.Label(subpage2, text="Basic data on chosen planet", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label1.grid(row=2, column=0, padx=50, pady=(40, 0), sticky="e")

    subtitle_label2 = tk.Label(subpage2, text="Revolution simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label2.grid(row=2, column=1, padx=50,pady=(40, 0), sticky="ew")

    subtitle_label3 = tk.Label(subpage2, text="Biology simulation", font=("Arial", 18, 'bold'), fg='blue', bg=color)
    subtitle_label3.grid(row=2, column=2, padx=50,pady=(40, 0), sticky="w")
    
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
#kad ovu funkciju maknem padne kod?
def print_window_size():
    global main_frame
    global new_page

    window_width = root.winfo_screenwidth()
    window_height = root.winfo_screenheight()
    root.destroy()

pocetna_stranica()
root.mainloop()
