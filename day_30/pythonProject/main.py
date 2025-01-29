
# try:
#     file = open("a_file.txt")
#
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exits.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()


height = float(input("Height: "))
weight = float(input("Weight: "))

if height >3:
    raise ValueError("Human Height should not ve over 3 meters.")

bmi = weight/ height**2
print(bmi)
