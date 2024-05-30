import easyocr
from tkinter import filedialog


def fetch_file() -> str:
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select An Image",
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
    )

    return file_path


def main():
    print(fetch_file())


if __name__ == "__main__":
    main()
