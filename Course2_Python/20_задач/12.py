def counts_word(text:str, words: list) -> int:
    text = text.lower()
    return sum([text.count(word.lower()) for word in words])
 
print(counts_word('ae aE bf Bf', ['ae','bf']))