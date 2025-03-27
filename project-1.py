def main():
    while True:
        print("\nUnit Converter")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        choice = input("Choose a category (1-4): ")

        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

def convert_length():
    units = [
        {"name": "Meters", "abbr": "m", "factor": 1},
        {"name": "Kilometers", "abbr": "km", "factor": 1000},
        {"name": "Miles", "abbr": "mi", "factor": 1609.34},
        {"name": "Feet", "abbr": "ft", "factor": 0.3048},
        {"name": "Inches", "abbr": "in", "factor": 0.0254},
    ]
    
    print("\nLength Units:")
    for idx, unit in enumerate(units):
        print(f"{idx + 1}. {unit['name']} ({unit['abbr']})")
    
    try:
        source = int(input("\nEnter source unit (1-5): ")) - 1
        target = int(input("Enter target unit (1-5): ")) - 1
        value = float(input("Enter value to convert: "))
        
        result = (value * units[source]['factor']) / units[target]['factor']
        print(f"\n{value} {units[source]['abbr']} = {result:.2f} {units[target]['abbr']}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid numbers.")

def convert_weight():
    units = [
        {"name": "Kilograms", "abbr": "kg", "factor": 1},
        {"name": "Grams", "abbr": "g", "factor": 0.001},
        {"name": "Pounds", "abbr": "lb", "factor": 0.453592},
        {"name": "Ounces", "abbr": "oz", "factor": 0.0283495},
    ]
    
    print("\nWeight Units:")
    for idx, unit in enumerate(units):
        print(f"{idx + 1}. {unit['name']} ({unit['abbr']})")
    
    try:
        source = int(input("\nEnter source unit (1-4): ")) - 1
        target = int(input("Enter target unit (1-4): ")) - 1
        value = float(input("Enter value to convert: "))
        
        result = (value * units[source]['factor']) / units[target]['factor']
        print(f"\n{value} {units[source]['abbr']} = {result:.2f} {units[target]['abbr']}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid numbers.")

def convert_temperature():
    units = [
        {"name": "Celsius", "abbr": "°C"},
        {"name": "Fahrenheit", "abbr": "°F"},
        {"name": "Kelvin", "abbr": "K"},
    ]
    
    print("\nTemperature Units:")
    for idx, unit in enumerate(units):
        print(f"{idx + 1}. {unit['name']} ({unit['abbr']})")
    
    try:
        source = int(input("\nEnter source unit (1-3): ")) - 1
        target = int(input("Enter target unit (1-3): ")) - 1
        value = float(input("Enter temperature: "))
        
        source_unit = units[source]['abbr']
        target_unit = units[target]['abbr']

        if source_unit == target_unit:
            result = value
        else:
            if source_unit == '°C':
                if target_unit == '°F':
                    result = (value * 9/5) + 32
                elif target_unit == 'K':
                    result = value + 273.15
            elif source_unit == '°F':
                if target_unit == '°C':
                    result = (value - 32) * 5/9
                elif target_unit == 'K':
                    result = (value - 32) * 5/9 + 273.15
            elif source_unit == 'K':
                if target_unit == '°C':
                    result = value - 273.15
                elif target_unit == '°F':
                    result = (value - 273.15) * 9/5 + 32
            else:
                raise ValueError("Invalid units")
        
        print(f"\n{value} {source_unit} = {result:.2f} {target_unit}")
    except (ValueError, IndexError):
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()