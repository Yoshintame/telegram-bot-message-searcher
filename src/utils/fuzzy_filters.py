from rapidfuzz import fuzz


def fuzzy_check_text_for_keywords(text, keywords):
    return fuzz.token_set_ratio(text, " ".join(keywords))


def bare_check_text_for_keywords(text, keywords):
    return any(keyword in text for keyword in keywords)
