def bullscows(answer: str, jigsaw: str):
    b, c = 0, 0
    an = list(answer)
    jig = list(jigsaw)
    for i in range(len(answer)):
        if answer[i] == jigsaw[i]:
            jig = jig[:i - b] + jig[i+1 - b:]
            an = an[:i - b] + an[i+1 - b:]
            b += 1
    for i in an: #set?
        if i in jig:
            jig.remove(i)
            c += 1
    return b, c
