

def calculates_reading_time_of_text(text):
    if isinstance(text, str):
        words = text.split()
        word_count = len(words)
        
        if word_count >= 200:
            minutes = word_count // 200
            remainder_words = word_count % 200
            if remainder_words == 0:
                if minutes == 1:
                    return f"{minutes} minute"
                else:
                    return f"{minutes} minutes"
            else:
                seconds = remainder_words * (60 / 200) 
                if minutes == 1:
                    return f"{minutes} minute and {int(seconds)} seconds"
                else:
                    return f"{minutes} minutes and {int(seconds)} seconds"
        else:       
            seconds = word_count * (60 / 200)  
            return f"{int(seconds)} seconds"
    else:
        raise Exception("Invalid input format. Please provide a text string.") 