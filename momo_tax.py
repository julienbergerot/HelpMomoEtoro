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
    reader = PdfReader(path)

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

    stored = []

    for idx, splits in enumerate(lines[START_LINE:]):
        print(f"Line number {idx + START_LINE}")

        if len(splits) == 9:
            # first lane is weird
            splits.insert(7, "")

        dic = {
            "211": splits[0].replace(".", "/"),
            "212": splits[1],
            "213": splits[2],
            "220": splits[6],
            "221": splits[7],
        }

        stored.append(dic)

        if len(stored) == 5:
            for key in dic.keys():
                for i in range(5):
                    value = stored[i][key]
                    pyperclip.copy(value)
                    wait_for_key()
                    time.sleep(0.2)
            stored = []
