class reverse:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def reverse_sentence(self):
        words = self.sentence.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)

sentence = input("Enter a sentence to reverse:")

s = reverse(sentence)
print(s.reverse_sentence())