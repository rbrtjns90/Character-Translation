import re
 
class translator():
 
    def __init__(self, text):
        self.text = text
 
    def multiple_replace(text):
        dict = {
            "😂": "emoji-1",
            "🤣": "emoji-2",
            "🙃": "emoji-3",
        }
 
        # Create a regular expression  from the dictionary keys
        regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
 
        # For each match, look-up corresponding value in dictionary
        return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)
 
 
test = "🙃😂🙃"
 
fixed = translator.multiple_replace(test)
 
print(fixed)
