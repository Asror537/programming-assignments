password = "python"
checkPassword = input()
tries = 3

while checkPassword != password:
    tries -= 1
    checkPassword = input(f"Wrong! {tries} tres left\n")
    if tries <= 1:
        print("Wrong {tries} left! \nALARM vault locked!")
        break