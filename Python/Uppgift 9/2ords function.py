

def longestWord(ord1, ord2):
    if len(ord1) >= len(ord2):
        return ord1
    else:
        return ord2
    
print(longestWord("book", "linjal"))
