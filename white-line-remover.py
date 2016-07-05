# Open the file
with open("your_file_name", mode="r") as f:
    data = f.readlines()

# Get rid of the newline character
for i in range(0, len(data)):
    data[i] = data[i].replace("\n","")

# Filter out the blank strings ("") from the list
data = filter(None, data)

# Create a new file with the correct formatting
with open("your_new_file_name", mode="w") as f:
    for element in data:
        f.write(email + "\n")
