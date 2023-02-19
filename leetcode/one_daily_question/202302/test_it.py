class Entry(object):

    def __init__(self, name: str, years: int) -> None:
        """
        init
        :param p:
        :param t:
        """
        self.name = name
        self.years = years

    def __lt__(self, other: 'Entry') -> bool:
        """
        it
        :param other:
        :return:
        """
        return self.years < other.years

    def __eq__(self, other)-> bool:
        """
        eq
        :param other:
        :return:
        """
        return self.years == other.years

    def __gt__(self, other):
        """
        gt
        :param other:
        :return:
        """
        return self.years > other.years


if __name__ == '__main__':
    entry1 = Entry('a', 2)
    entry2 = Entry('b', 1)
    print(entry1 > entry2)
    print(entry1 < entry2)

