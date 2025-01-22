def save_file(file_name):
    song = "apple banana cherry do juseyo"

    with open(file_name, "w") as file:
        file.write(song)
    print(f"save files")

save_file("gitAction.txt")
