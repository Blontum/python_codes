# Print out the last name of the second employee. Please search through the dictionary below: **Alexandra ®
# d = {"employees": [{"firstName": "John", "lastName": "Doe"},
# {"firstName": "Anna", "lastName": "Smith"}, {"firstName": "Peter", "lastName": "Jones"}],
# "owners": [{"firstName": "Jack", "lastName": "Petter"},
#{"firstName": "Jessy", "lastName": "Petter"}1}


# Assuming 'd' is already defined as your dictionary
d = {
    "employees": [
        {"firstName": "John", "lastName": "Doe"},
        {"firstName": "Anna", "lastName": "Smith"},
        {"firstName": "Peter", "lastName": "Jones"}
    ],
    "owners": [
        {"firstName": "Jack", "lastName": "Petter"},
        {"firstName": "Jessy", "lastName": "Petter"}
    ]
}
# Extract the last name of the second employee
employee2_last_name = d["employees"][1]["lastName"]
print(f"The last name of the second employee is: {employee2_last_name}\n")

# Assuming 'd' is already defined as your dictionary

definition = d.get("Alexandra")

# Check if 'definition' is not None (i.e., the key exists)
if definition:
    print(definition)
else:
    print(f"The name doesn't exit")