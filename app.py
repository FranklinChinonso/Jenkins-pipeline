def greet_user(name):
    if not isinstance(name, str) or len(name.strip()) == 0:
        return "Hello, Guest!"
    return f"Hello, {name.strip()}!"

def add_numbers(a, b):
    return a + b

def reverse_string(text):
    return text[::-1]

if __name__ == "__main__":
    print(greet_user("Jenkins"))
    print(f"5 + 3 = {add_numbers(5, 3)}")
    print(f"'Pipeline' reversed is '{reverse_string('Pipeline')}'")
