def is_fake_review(text):

    text = text.lower()

    spam_words = ["buy now", "click here", "subscribe", "free", "offer"]

    # Rule 1: spam keywords
    for word in spam_words:
        if word in text:
            return True

    # Rule 2: very short review
    if len(text) < 10:
        return True

    # Rule 3: repeated words
    words = text.split()
    if len(words) != len(set(words)):
        return True

    return False