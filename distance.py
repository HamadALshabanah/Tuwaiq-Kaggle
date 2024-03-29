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

cities_distances_from_riyadh['بيشة'] = 672.65
cities_distances_from_riyadh['محايل'] = 390.10
cities_distances_from_riyadh['المذنب'] = 284.82
cities_distances_from_riyadh['الخفجي'] = 450.32
cities_distances_from_riyadh['رأس تنورة'] = 403.60
cities_distances_from_riyadh['ضمد'] = 936.61
cities_distances_from_riyadh['القريات'] = 850.27
cities_distances_from_riyadh['حوطة بني تميم'] = 89.49
cities_distances_from_riyadh['ضبا'] = 1140.38
cities_distances_from_riyadh['مهد الذهب'] = 608.47
cities_distances_from_riyadh['بارق'] = 19.43
cities_distances_from_riyadh['بيش'] = 774.62
cities_distances_from_riyadh['دومة الجندل'] = 883.95
cities_distances_from_riyadh['صبيا'] = 938.15
cities_distances_from_riyadh['العرضيات'] = 17.90
cities_distances_from_riyadh['الحناكية'] = 626.83
cities_distances_from_riyadh['سراة عبيدة'] = 823.43
cities_distances_from_riyadh['أحد رفيدة'] = 824.88
cities_distances_from_riyadh['تربة'] = 649.55
cities_distances_from_riyadh['العلا'] = 904.66
cities_distances_from_riyadh['الحريملاء'] = 77.50
cities_distances_from_riyadh['بلجرشي'] = 756.95
cities_distances_from_riyadh['بقيق'] = 390.94
cities_distances_from_riyadh['القرى'] = 349.80
cities_distances_from_riyadh['رجال ألمع'] = 856.22
cities_distances_from_riyadh['المجاردة'] = 794.90
cities_distances_from_riyadh['وادي الدواسر'] = 845.47
cities_distances_from_riyadh['وادي الفرع'] = 509.48
cities_distances_from_riyadh['محايل عسير'] = 954.17
cities_distances_from_riyadh['الزلفي'] = 262.24
cities_distances_from_riyadh['بدر'] = 812.27
cities_distances_from_riyadh['تثليت'] = 661.43
cities_distances_from_riyadh['عنك'] = 387.84
cities_distances_from_riyadh['البكيرية'] = 357.35
cities_distances_from_riyadh['طريف'] = 897.82
cities_distances_from_riyadh['بني حسن'] = 762.45
cities_distances_from_riyadh['رياض الخبراء'] = 350.45
cities_distances_from_riyadh['طبرجل'] = 14.60
cities_distances_from_riyadh['ثادق'] = 108.64
cities_distances_from_riyadh['الجموم'] = 794.73
cities_distances_from_riyadh['الغاط'] = 231.97
cities_distances_from_riyadh['تيماء'] = 879.41
cities_distances_from_riyadh['ظهران الجنوب'] = 848.66
cities_distances_from_riyadh['أملج'] = 949.86
cities_distances_from_riyadh['ابها'] = 842.43
cities_distances_from_riyadh['الدرب'] = 899.74
cities_distances_from_riyadh['بحرة'] = 829.66







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