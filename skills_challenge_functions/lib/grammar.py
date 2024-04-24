
def capitalizes_and_adds_full_stop(text, question):
    if isinstance(text, str):
            if question == False:
                if text[0].isupper() and text[-1] in [".", "!", "?"]:
                    return True
                elif not text[0].isupper() and not text[-1] in [".", "!", "?"]:
                    capitalized = text.capitalize()
                    return f"{capitalized}."
                elif not text[0].isupper() and text[-1] in [".", "!", "?"]:
                    capitalized = text.capitalize()
                    return f"{capitalized}"
                else:
                    return f'{text}.'
            elif question == True:
                if text[0].isupper() and text[-1] in [".", "!", "?"]:
                    return True
                elif not text[0].isupper() and not text[-1] in [".", "!", "?"]:
                    capitalized = text.capitalize()
                    return f"{capitalized}?"
                elif not text[0].isupper() and text[-1] in [".", "!", "?"]:
                    capitalized = text.capitalize()
                    return f"{capitalized}"
                else:
                    return f'{text}?'
            else:
                raise TypeError("Question parameter must be a boolean value.")
    else:
        raise Exception("Invalid input format. Please provide a text string.") 