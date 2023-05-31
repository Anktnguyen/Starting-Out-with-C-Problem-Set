"""
1. Galilean Moons of Jupiter
Write a program that creates a dictionary containing the names of the Galilean moons of
Jupiter as keys and their mean radiuses (in kilometers) as values. The dictionary should
contain the following key-value pairs:

Moon Name (key) Mean Radius (value)
Io 1821.6
Europa 1560.8
Ganymede 2634.1
Callisto 2410.3

The program should also create a dictionary containing the moon names and their surface
gravities (in meters per second squared). The dictionary should contain the following
key-value pairs:

Moon Name (key) Surface Gravity (value)
Io 1.796
Europa 1.314
Ganymede 1.428
Callisto 1.235

The program should also create a dictionary containing the moon names and their orbital
periods (in days). The dictionary should contain the following key-value pairs:
Moon Name (key) Orbital Period (value)
Io 1.769
Europa 3.551
Ganymede 7.154
Callisto 16.689

The program should let the user enter the name of a Galilean moon of Jupiter; then it
should display the moon's mean radius, surface gravity, and orbital period. It should display
an error message if the user enters an invalid moon name.
"""
def main():
    #user input of moon name
    moon_name = input("Enter moon a Galilean moon of Jupiter's name: ")
    #printing out information and calling function
    print(f"The radius of {moon_name}:")
    #dictionary_name[key], retrieving value in the dictionary using the key
    radius[moon_name]
    print(f"The surface gravity of {moon_name}:")
    sur_gravity[moon_name]
    print(f"The orbital period of {moon_name}:")
    orbit_per[moon_name]


#Separating the characteristics of moon into each function for efficient future update
def radius(moon_name):
        mean_radius = {'Io': 1821.6, 'Europa': 1560.8,
                   'Ganymede': 2634.1, 'Callisto': 2410.3}
        print(mean_radius[moon_name])
        
def sur_gravity(moon_name):
    surface_gravity = {'Io': 1.796, 'Europa': 1.314,
                   'Ganymede': 1.428, 'Callisto': 1.235}
    print(surface_gravity[moon_name])

def orbit_per(moon_name):
    orbital_period = {'Io': 1.769, 'Europa': 3.551,
                   'Ganymede': 7.154, 'Callisto': 16.689}
    print(orbital_period[moon_name]) 


if __name__ == "__main__":
    main()
