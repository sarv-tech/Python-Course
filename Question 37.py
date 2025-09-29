# Q. Create a dictionary student = {"name": "John", "age": 20, "grade": "A"} and:
# Print the value of "name".
# Change "grade" to "A+".
# Add a new key "city" with value "Delhi".


student = {"name": "John", "age": 20, "grade": "A"}

print(student.get("name"))  # Print the value of "name". 
student["grade"] = "A+"     # Change "grade" to "A+".
print(student)

student.update({"city": "Delhi"})   # Add a new key "city" with value "Delhi".
print(student)