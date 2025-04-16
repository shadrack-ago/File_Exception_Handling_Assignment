try:
    input_file = input("Enter the file name: ")

    with open(input_file, "r") as file:
        content = file.read()

    modified_content = content.upper()

    with open("modified_" + input_file, "w") as file:
        file.write(modified_content)

    print("File modified and saved as:", "modified_" + input_file)

except FileNotFoundError:
    print("File not found. Please check the name.")

finally:
    print("Done.")
