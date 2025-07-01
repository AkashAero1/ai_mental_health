def get_prompt(mood):
    if mood == "positive":
        return "You're sounding great! Want to reflect on something meaningful today?"
    elif mood == "negative":
        return (
            "It seems you're feeling a bit low. Would you like a calming thought or a reflective journaling prompt?"
        )
    else:
        return "Feeling neutral? I'm here to listen. What's been on your mind today?"
