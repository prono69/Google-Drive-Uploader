# This  Thing will only identify sent token :D


def is_token(token):
    token = token.split()[-1]
    TLEN = len(token)
    return TLEN == 57 and token[1] == "/"
