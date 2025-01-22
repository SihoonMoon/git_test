def save_file(file_name):
    song = "가나다라마바사 나는 깃의 고수다"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(song)
    print(f"텍스트가 파일로 나왔서요")

save_file("내파일.txt")
