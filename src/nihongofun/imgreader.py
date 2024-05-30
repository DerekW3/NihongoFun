import easyocr
from tkinter import filedialog


def fetch_file() -> str:
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Select An Image",
        filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png")),
    )

    return file_path


def fetch_text(file_path: str) -> list[str]:
    reader = easyocr.Reader(["ja"])
    return reader.readtext(file_path, detail=0)


def main():
    text = fetch_text(fetch_file())
    print(text)


if __name__ == "__main__":
    main()
