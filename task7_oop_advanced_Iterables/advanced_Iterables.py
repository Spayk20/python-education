"""Task - Iterables"""

from collections import Counter


class MultipleSentencesError(Exception):
    """Custom exception"""


class Sentence:
    """Container"""

    def __init__(self, sentence):
        """Arguments
        :parameter sentence: str
        :self.string :str - source string
        """
        self.string = sentence

        if not isinstance(self.string, str):
            raise TypeError('Your string must be str type')

        self._errors()
        self.string_non_char = self._cleaner()


    def _errors(self):
        if not self._ending_checker():
            raise ValueError("Please, finish sentence!!!")
        if not self._one_sentence_checker():
            raise MultipleSentencesError("Must be only one sentence")

    def _ending_checker(self):
        """Sentence ending checker"""
        message = False
        self.last_char = (".", "!", "?", "...")
        self.words_splitters = [',', '\'', '\"', ";", ":", "-", " "]

        if self.string.endswith(self.last_char):
            message = True
        return message

    def _one_sentence_checker(self) -> bool:
        """Checking for 1 sentence in sentence """

        message = False
        if (len(self.string.split('.')) > 0) or (len(self.string.split('!')) > 0) \
                or (len(self.string.split('?')) > 0) or (len(self.string.split('...')) > 0):
            message = True
        return message

    def _cleaner(self):
        """Clears all non-alphabetic characters"""
        data_non_char = ''
        for i in self.string:
            if i.isalpha() or i == ' ':
                data_non_char += i
        return data_non_char

    def _words(self):
        """Generator"""
        for i in SentenceIterator(self.string_non_char):
            yield i

    @property
    def words(self):
        """List of words"""
        res = []
        for i in SentenceIterator(self.string_non_char):
            res.append(i + ' ')
        return res

    @property
    def other_chars(self):
        """List of all non-alphabetic characters"""
        res = []
        for i in self.string:
            if not i.isalpha():
                res.append(i)
        return set(res)

    def __repr__(self):
        """Implements __repr__"""
        words, other_chars = SentenceIterator(self.string_non_char)._counter()
        return f'Sentence(words={words}, other_chars={other_chars})'

    def __iter__(self):
        """Implements iterator"""
        return SentenceIterator(self.string_non_char)

    def __getitem__(self, index):
        """Implements next()"""
        return SentenceIterator(self.string_non_char).fu_for_get_item(index)


class SentenceIterator:
    """Iterator class"""

    def __init__(self, sent):
        self.sent = sent
        self._start = 0
        self._stop = 0
        self._remains = 0
        self._words = 0

    def get_item(self):
        """Main iterator"""
        data = self.sent[self._start:].find(' ')
        res = ''
        if data == -1:
            res = self.sent[self._start:]
        elif data != -1:
            res = self.sent[self._start:data + self._start]
        self._start += data + 1

        if self._stop <= self.sent.count(' '):
            self._remains -= 1
            self._stop += 1
            return res
        raise StopIteration

    def _counter(self):
        """Count the symbols"""
        words = 0
        chars = 0

        count = Counter(self.sent)
        for i in count:
            if i.isalpha():
                words += count[i]
            else:
                chars += count[i]

        return words, chars

    def fu_for_get_item(self, index):
        """Responsible for choosing which function to call, slice or index"""
        if isinstance(index, int):
            res = self._non_slice_for_get_item(index)
        elif isinstance(index, slice):
            res = self._slice_fo_getitem(index)
        else:
            raise TypeError
        return res

    def _non_slice_for_get_item(self, index):
        """To find only indices"""
        res = ''
        for i in range(str(self.sent).count(' ') + 1):
            res = self.get_item()
            if i == index:
                break
        return res

    def _slice_fo_getitem(self, index):
        """Responsible for slicing"""
        res = ''
        count = index.start
        if not index.step:
            step = index.step
        else:
            step = 1

        for i in range(str(self.sent).count(' ') + 1):
            data = self.get_item()

            if i == count and i < index.stop:

                res += data + ' '
                count += step
            elif i == index.stop:
                break
        return res

    def __next__(self):
        return self.get_item()

    def __iter__(self):
        return self

    def __len__(self):
        return len(self.sent)


if __name__ == "__main__":

    SENT = "Hello my friend; I have good news for you!"

    iterate_word = Sentence(SENT)
    print(f'Task sentence: {SENT}')
    print(f"Task 1, __repr__ : {iterate_word}")
    print(f'Task 2, generator object : {iterate_word._words()}')
    next_iter = iterate_word._words()
    print(f"Task 3, next() :{next(next_iter)}")
    print(f"Task 3, next() :{next(next_iter)}")
    print(f"Task 4, slice[1:3:2]: {Sentence(SENT)[1:3:2]}")
    print(f"Task 5, index[5]: {Sentence(SENT)[5]}")
    print('Task 6, cycle :')
    for r in iterate_word:
        print(r)
    print(f'Task 7, words: {iterate_word.words}')
    print(f'Task 8, non_ite: {iterate_word.other_chars}')
