def top_k_freq_words(filename, k):
    with open(filename, "r") as file:
        s = file.read()
         
    words = s.split()
    cnt = {}
     
    for word in words:
        cnt[word.lower()] = cnt.get(word.lower(), 0) + 1
     
    data = list(cnt.items())
    data.sort(key=lambda x: x[1], reverse=True)
     
    return [x[0] for x in data[:k]]
 
 
if __name__ == "__main__":
    assert top_k_freq_words("test.txt", 3) == ['is', 'an', 'apple']
    
"""
test.txt:
This is an apple
I like the orange
An apple is red
"""
