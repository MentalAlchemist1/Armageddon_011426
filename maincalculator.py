"""
Simple Calculator App
A clean, functional calculator supporting basic arithmetic operations.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("\n" + "="*40)
    print("       SIMPLE CALCULATOR")
    print("="*40)
    
    while True:
        print("\nOperations:")
        print("  1. Add (+)")
        print("  2. Subtract (-)")
        print("  3. Multiply (*)")
        print("  4. Divide (/)")
        print("  5. Exit")
        
        choice = input("\nSelect operation (1-5): ").strip()
        
        if choice == '5':
            print("\nGoodbye!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1-5.")
            continue
        
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        
        operations = {
            '1': (add, '+'),
            '2': (subtract, '-'),
            '3': (multiply, '*'),
            '4': (divide, '/')
        }
        
        func, symbol = operations[choice]
        result = func(num1, num2)
        
        print(f"\n>> {num1} {symbol} {num2} = {result}")

if __name__ == "__main__":
    calculator()
