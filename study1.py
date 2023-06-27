def reverse_string(string):
    # Using slicing to reverse the string
    x = string[::-1]
    return x

# Example usage
string = "Hello, World!"
reversed_text = reverse_string(string)
print(f"The reversed string is: {reversed_text}")