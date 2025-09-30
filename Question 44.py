# Q. Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:

# Both length and width
# Only length (use default width)


def calculate_area(length, width=10):
    return length * width

print(f"The area of a rectangle is {calculate_area(13, 20)}")
print(calculate_area(15))