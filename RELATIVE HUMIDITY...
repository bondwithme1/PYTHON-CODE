# Get inputs from user
temperature = float(input("Enter temperature in °C: "))
humidity = float(input("Enter humidity in %: "))
wind_speed = float(input("Enter wind speed in km/h: "))

# Determine condition
if temperature > 30 and humidity > 60:
    condition = "Hot and Humid"
elif temperature > 30 and humidity <= 60:
    condition = "Hot and Dry"
elif 15 <= temperature <= 30:
    condition = "Moderate"
elif temperature < 15 and wind_speed > 20:
    condition = "Cold and Windy"
else:
    condition = "Cold"

# Show result
print(f"Weather Condition: {condition}")
