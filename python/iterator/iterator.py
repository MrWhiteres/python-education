from re import match, findall, sub


class MultipleSentencesError(Exception):
    """This class extends error options"""
    pass


class Sentence:
    def __init__(self, sentence: str):
        if not isinstance(sentence, str):
            raise TypeError("Sentence must be a string data type.")
        if match(r'[^.!?]+$', sentence):
            raise ValueError("Sentence must be completed - (.?!).")
        if not match(r'([^\.!?]|[^\.!?]+[\_.])$', sentence):
            raise MultipleSentencesError("There should only be one offer.")

        self._sentence = sentence

    @property
    def __repr__(self):
        """Method shows the number of words and punctuation marks in a sentence"""
        words = len(findall(r'\w+', self._sentence))
        other_chars = len(findall(fr'[.,!?]', self._sentence))
        return f'<Sentence(words={words},other_chars={other_chars})> '

    @property
    def _words(self):
        """Method returns a lazy operator"""
        return (word for word in sub(r'[^\w+]', ' ', self._sentence).split())

    @property
    def words(self):
        """Method returns a list of only words in a sentence"""
        return sub(r'[^\w+]', ' ', self._sentence).split()

    @property
    def other_chars(self):
        """Method returns only punctuation marks in a sentence"""
        return sub(r'[\w+]', ' ', self._sentence).split()

    def __getitem__(self, item: int or slice):
        """Method can return a slice or an element"""
        if isinstance(item, slice):
            return self.words[item.start:item.stop:item.step]
        if item >= len(self.words) or item < -len(self.words):
            raise IndexError("Is no word with this index")
        return self.words[item]

    @property
    def __iter__(self):
        """Method overloads the work of the iterator on the sentence iterator"""
        return SentenceIterator(self)


class SentenceIterator:
    def __init__(self, sentence: Sentence):
        self._word = sentence.words()
        self.iter = -1

    def __next__(self):
        self.iter += 1
        if self.iter >= self._word:
            raise StopIteration
        return self._word[self.iter]

    def __iter__(self):
        return self


a = "Uber relaunches operations in Kyiv and continues to operate in Lviv."
# -----ERROR-----
# print(Sentence(99))
# print(Sentence(a + " Sentence:."))
# print(Sentence(a[:-1]))

# -----SLICE and INDEX-----
# print(Sentence(a)[:])
# print(Sentence(a)[1])

# -----LAZY ITERATOR-----
# print(Sentence(a)._words)

# -----CYCLE-----
# for word in Sentence(a):
#     print(word)


