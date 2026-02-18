def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"this is not a valid number: {temp_str} \n")
        return

    if temp >= 0 and temp <= 40:
        print(f" Temperatur {temp} C is perfect for plants \n")
    elif temp < 0:
        print(f"Error: {temp}C is too cold for a plant (min 0C)\n")
    elif temp > 40:
        print(f"Error: {temp}C is too hot for a plant (max 40C) \n")

def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===") 
    

    print("Testing temperature: 25") 
    check_temperature("25")
    
    print("Testing temperature: abc")
    check_temperature("abc")
    
    print("Testing temperature: 100")
    check_temperature("100")
    
    print("Testing temperature: -50")
    check_temperature("-50")
    
    print("All tests completed") 
    print("program didn't crash!")

if __name__ == "__main__":
    test_temperature_input()