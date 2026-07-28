import re


def clean_input(text):

    if text is None:
        return ""

    text = str(text)

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    return text.strip()



def format_list(text):

    if not text:
        return ""

    items = text.split(",")

    result = ""

    for item in items:
        result += "- " + item.strip() + "\n"

    return result