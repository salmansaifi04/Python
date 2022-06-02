# word counter

def word_counter(s):
    output = {}
    for i in s:
        output[i] = s.count(i)
    return output

print(word_counter("Salman Saifi"))