def first_non_repeating_letter(w):
    for i in w:
        if w.lower().count(i.lower()) == 1:
            return i
    return
