import easyocr
from tkinter import filedialog


def fetch_file() -> str:
    print("Please choose an image file for text processing!")
    file_path = filedialog.askdirectory()

    while not file_path.lower().endswith((".png", ".jpg")):
        response = input("No existing file at given path, try again? y/n")

        if response.lower() == "n":
            file_path = "QUIT!"
            break
        else:
            file_path = filedialog.askdirectory()
    return file_path


def main():
    print(fetch_file())


if __name__ == "__main__":
    main()
