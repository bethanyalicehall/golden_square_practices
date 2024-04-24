
def capitalizes_and_adds_full_stop(text, question):
    if question == False:
        capitalized = text.capitalize()
        return f"{capitalized}."
    else:
        capitalized = text.capitalize()
        return f"{capitalized}?"