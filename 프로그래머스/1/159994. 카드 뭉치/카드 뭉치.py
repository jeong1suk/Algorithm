def solution(cards1, cards2, goal):
    for word in goal:
        if cards1:
            word_1 = cards1[0]
        if cards2:
            word_2 = cards2[0]
        if word == word_1:
            cards1.remove(word)
        elif word == word_2:
            cards2.remove(word)
        else:
            return 'No'
    return 'Yes'