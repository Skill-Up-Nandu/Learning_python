# FUNCTION RETURN UNPACKING
# def get_coordinates():
#     return (34.0522, -118.2437)
# Unpack the returned values into lat and lon

def get_coordinates(x, y):
    return (x, y)

lat , lon = get_coordinates(34.0522, -118.2437)
print(f"Latitude : {lat}")
print(f"Longitude : {lon}")