from rapidfuzz import fuzz


def fuzzy_check_text_for_keywords(text, keywords):
    return fuzz.token_set_ratio(text, " ".join(keywords))


def bare_check_text_for_keywords(text, keywords):
    if text is None: return False
    text = text.lower()

    for keyword in keywords:
        if keyword in text:
            return keyword

    return None
