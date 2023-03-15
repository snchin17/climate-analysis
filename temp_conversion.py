"""
A module for converting temperature from Imperial to Metric units.
Will throw ValueErrors for temperatures < absolute zero.

Functions:
    convert_fahr_to_celsius: Converts Fahrenheit to Celsius
    convert_fahr_to_kelvin: Converts Fahrenheit to Kelvin
"""


def convert_fahr_to_celsius(fahr):
     """
    Given a temperature in Fahrenheit, converts it to Celsius

    :param fahr: The temperature in Fahrenheit
    :raises ValueError: If the temperature is below absolute zero
    :return: The temperature in Celsius
    """  
    
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:  # If temperature is below absolute zero, throw an error
    
        raise ValueError(f"Trying to convert impossible temperatue: {fahr}F")
    return celsius

def convert_fahr_to_kelvin(fahr):
    celsius = convert_fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin
