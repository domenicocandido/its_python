def charDuplicator (s:str) ->  str:

    if not s:
        return " "
    else:
        return 2 * s[0] + charDuplicator(s[1:])

print(charDuplicator("libro"))