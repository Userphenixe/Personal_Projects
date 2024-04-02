my_string = 'Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet.'

class TextAnalyser(object):
    def __init__(self, text):
        self.text = text.lower()

    def remove_punctuation(self):
        punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        for char in punctuation:
            self.text = self.text.replace(char, '')
        return self.text

    def count_words(self, word):
        return self.text.split().count(word.lower())

c = TextAnalyser(my_string)
print(c.remove_punctuation())
print(c.count_words('diam'))