import re

# Write a function that accepts a lengthy string parameter.
# Without utilizing any of the built-in library methods available to your language, return the first word to occur more than once in that provided string.
def repeated_word(string):
    string = re.sub(r'[^\w\s]', '', string)
    words = {}
    processed_words = []
    most_frequent_words = []

# Modify your function to return a count of each of the words in the provided string
    for word in string.split():
        if words[word]:
            words[word] += 1
        else: words[word] = 1

# Modify your function to return a list of the words most frequently used in the provided string
    for key in words:
        most_frequent_words.append((words[key], key))
    most_frequent_words.sort(reverse=True)

    for word in string.split():
        if word in processed_words:
            return [word, words, most_frequent_words]
        processed_words.append(word)
    return ["No repeating words", words, most_frequent_words]
