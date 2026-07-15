# utils/math_utils.py
import math

def calculate_compound_interest(principal, rate, time, n=1):
    """Calculates compound interest: A = P * (1 + r/n)**(n*t)"""
    # Converting rate percentage to decimal
    r = rate / 100
    amount = principal * math.pow((1 + r / n), (n * time))
    interest = amount - principal
    return amount, interest

def calculate_area_circle(radius):
    """Calculates the area of a circle using math.pi."""
    return math.pi * math.pow(radius, 2)

def convert_celsius_to_fahrenheit(celsius):
    """Basic unit conversion utility."""
    return (celsius * 9/5) + 32