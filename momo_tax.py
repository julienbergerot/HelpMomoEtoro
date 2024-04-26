import pyperclip
import keyboard
import time

from pypdf import PdfReader

DOCUMENT_NAME = "example.pdf"
START_LINE = 0


def wait_for_key():
    while True:  # making a loop
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed("v"):  # if key 'q' is pressed
                # print("You Pressed V Key!")
                break  # finishing the loop
        except:
            break


def process_document(path="example.pdf"):
    # creating a pdf reader object
    reader = PdfReader("example.pdf")

    # creating a page object
    pages = reader.pages

    texts = [page.extract_text() for page in pages]
    text = "\n".join(texts)
    text = text.replace("\uffff", "")
    lines = text.split("\n")
    lines = [
        l.split(" ") for l in lines if len(l.split(" ")) == 9 or len(l.split(" ")) == 10
    ]

    print(f"There are {len(lines)} lines in your document")

    return lines


if __name__ == "__main__":
    lines = process_document(path=DOCUMENT_NAME)

    for idx, splits in enumerate(lines[START_LINE:]):
        print(f"Line number {idx + START_LINE}")

        if len(splits) == 9:
            # first lane is weird
            splits.insert(7, "")

        dic = {
            "211": splits[0],
            "212": splits[1],
            "213": splits[2],
            "214": "",
            "215": splits[3],
            "216": "",
            "217": splits[4],
            "218": splits[5],
            "220": splits[6],
            "221": splits[7],
            "222": "",
            "223": splits[8],
            "final": splits[9],
        }
        for key, value in dic.items():
            pyperclip.copy(value)
            wait_for_key()
            time.sleep(0.2)
