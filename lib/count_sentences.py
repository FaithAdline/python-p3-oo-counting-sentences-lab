import re

class MyString:
    def __init__(self, value):
        # Verify that the value is a string before assigning it
        if isinstance(value, str):
            self.value = value
        else:
            raise ValueError("Input must be a string")

    def is_sentence(self):
        # Check if the value ends with a period
        return self.value.endswith('.')

    def is_question(self):
        # Check if the value ends with a question mark
        return self.value.endswith('?')

    def is_exclamation(self):
        # Check if the value ends with an exclamation mark
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string on periods, question marks, and exclamation marks
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())      # Output: False
print(string.is_question())      # Output: False
print(string.is_exclamation())   # Output: True
print(string.count_sentences())  # Output: 3

