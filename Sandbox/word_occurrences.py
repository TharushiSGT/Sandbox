"""
Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""


def main():
    text = input("Text: ").strip()
    words = text.split()
    word_to_count = {}

    for word in words:
        word = word.lower()
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Sort by word
    words = sorted(word_to_count.keys())
    max_length = max(len(word) for word in words)
    for word in words:
        print(f"{word:{max_length}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
