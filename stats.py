def get_num_words(text):
    words = text.split()
    return len(words)
    
def get_char_counts(text):
    char_counts = {}

    for char in text:
        char = char.lower()
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_counts(char_counts):
    # Convert dictionary to a list of dictionaries
    char_list = [{"char": char, "num": count} for char, count in char_counts.items() if char.isalpha()]

    # Helper function to sort by the "num" key
    def sort_on(item):
        return item["num"]

    # Sort the list descending by count
    char_list.sort(reverse=True, key=sort_on)

    return char_list

