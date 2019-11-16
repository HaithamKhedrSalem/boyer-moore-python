from typing import Dict


def make_km_table(pattern: str) -> Dict[str, int]:

    """Generate a bad matches table with the number of skips for each
    character in the pattern."""

    table = dict()
    for index in range(len(pattern)):
       table[pattern[index]] = max(1, len(pattern) - index - 1)
    return table


class Bm(object):
    def __init__(self, text: str, pattern: str):
        self.text = text
        self.pattern = pattern
        self.table = make_km_table(pattern)

    def decide_slide_width(self, char: str) -> int:

        """ Return the number of skips for a char
        from the bad matches table and the
        default value is the length of the pattern. """

        return self.table.get(char, len(self.pattern))

    def search2(self) -> int:
        """
        Return the first index of the matched string.
        """
        counter = len(self.pattern) - 1
        while counter <= len(self.text) - 1:
            skips = 0
            text_counter = counter
            for char in reversed(self.pattern):
                if char == self.text[text_counter]:
                    text_counter -= 1
                    continue
                skips = self.decide_slide_width(char)
                counter += skips
                break
            if skips == 0:
                return counter - (len(self.pattern) - 1)
        return -1

    def search(self) -> int:
        """
        Return the first index of the matched string.
        """
        counter = 0
        while counter <= len(self.text) - len(self.pattern):
            skips = 0
            for index in range(len(self.pattern) - 1, -1, -1):
                if self.pattern[index] != self.text[counter + index]:
                    skips = self.decide_slide_width(self.pattern[index])
                    break
            if skips == 0:
                return counter
            counter += skips
        return -1
