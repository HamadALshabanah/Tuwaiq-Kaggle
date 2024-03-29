# Let's first read the file content to see how the cities are listed and then proceed to create the dictionary and function.

file_path = './cities.txt'

# Open and read the file content
with open(file_path, 'r') as file:
    cities = file.read().split(', ')


# Since we're going to create a dictionary with city names as keys and placeholder distances as values,
# Let's proceed to create that dictionary. Note that the distances here will be placeholders and should be replaced
# with actual distances.

# Creating a dictionary with city names from the file
cities_distances_from_riyadh = {city: 0 for city in cities}

# Showing the first few items to confirm
list(cities_distances_from_riyadh.items())[:5]

cities_distances_from_riyadh['Khamis Mushait'] = 822.50
cities_distances_from_riyadh['Hafr Al-Batin'] = 422.67
cities_distances_from_riyadh['Jeddah'] = 849.76
cities_distances_from_riyadh['Bisha'] = 672.65
cities_distances_from_riyadh['Mahayil'] = 390.10
cities_distances_from_riyadh['Al Midhnab'] = 284.82
cities_distances_from_riyadh['Khafji'] = 450.32
cities_distances_from_riyadh['Ras Tanura'] = 403.60
cities_distances_from_riyadh['Damad'] = 936.61
cities_distances_from_riyadh['Qurayyat'] = 850.27
cities_distances_from_riyadh['Hotat Bani Tamim'] = 89.49
cities_distances_from_riyadh['Duba'] = 1140.38
cities_distances_from_riyadh['Mahd Al Dhahab'] = 608.47
cities_distances_from_riyadh['Bareq'] = 19.43
cities_distances_from_riyadh['Bish'] = 774.62
cities_distances_from_riyadh['Domat Al-Jandal'] = 883.95
cities_distances_from_riyadh['Sabya'] = 938.15
cities_distances_from_riyadh['Al-Aridhah'] = 17.90
cities_distances_from_riyadh['Al-Hanakiyah'] = 626.83
cities_distances_from_riyadh['Sarat Abidah'] = 823.43
cities_distances_from_riyadh['Ahad Rufaidah'] = 824.88
cities_distances_from_riyadh['Turbah'] = 649.55
cities_distances_from_riyadh['AlUla'] = 904.66
cities_distances_from_riyadh['Huraymila'] = 77.50
cities_distances_from_riyadh['Baljurashi'] = 756.95
cities_distances_from_riyadh['Buqayq'] = 390.94
cities_distances_from_riyadh['Al-Qurayyat'] = 850.27
cities_distances_from_riyadh['Rijal Alma'] = 856.22
cities_distances_from_riyadh['Al Majardah'] = 794.90
cities_distances_from_riyadh['Wadi Al-Dawasir'] = 845.47
cities_distances_from_riyadh['Al Khurma'] = 565.67
cities_distances_from_riyadh['Adham'] = 762.04
cities_distances_from_riyadh['Umm Lajj'] = 798.60
cities_distances_from_riyadh['Al-Wajh'] = 1043.85
cities_distances_from_riyadh['Al Bukayriyah'] = 357.35
cities_distances_from_riyadh['Al Qaysumah'] = 408.51
cities_distances_from_riyadh['Turaif'] = 897.82
cities_distances_from_riyadh['Al Mithnab'] = 321.68
cities_distances_from_riyadh['Al-Oyoon'] = 836.22
cities_distances_from_riyadh['Al-Quwayiyah'] = 648.15
cities_distances_from_riyadh['Tabarjal'] = 14.60
cities_distances_from_riyadh['Thadiq'] = 108.64
cities_distances_from_riyadh['Al Jumum'] = 794.73
cities_distances_from_riyadh['Al Ghat'] = 231.97
cities_distances_from_riyadh['Tayma'] = 879.41
cities_distances_from_riyadh['Al Khafji'] = 843.37
cities_distances_from_riyadh['Ras Tanura'] = 403.60
cities_distances_from_riyadh['Dhahran Al Janoub'] = 848.66
cities_distances_from_riyadh['Umluj'] = 949.86







# Function to get distance from Riyadh
def get_distance_from_riyadh(city_name):
    """
    Returns the distance of a given city from Riyadh.
    
    Parameters:
    - city_name (str): The name of the city
    
    Returns:
    - int or str: The distance in kilometers if the city is in the dictionary, 
                  otherwise a message indicating the city is not found.
    """
    return cities_distances_from_riyadh.get(city_name, "City not found in the dictionary.")

# Example usage of the function
example_city = 'Hafr Al-Batin'
distance = get_distance_from_riyadh(example_city)

print(f'distance:',  distance)


def get_distance_from_riyadh(city_name):
    """
    Returns the distance of a given city from Riyadh.
    
    Parameters:
    - city_name (str): The name of the city
    
    Returns:
    - int or str: The distance in kilometers if the city is in the dictionary, 
                  otherwise a message indicating the city is not found.
    """
    return cities_distances_from_riyadh.get(city_name, "City not found in the dictionary.")


# Display the first few cities to understand the format
print(cities)