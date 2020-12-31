import statistics


class ExtendList(list):
    def __init__(self, lst):
        super().__init__(lst)
        self.lst = lst

    def __add__(self, other):
        lst_new = []
        lst_new.extend(self.lst)
        lst_new.extend(other.lst)
        return lst_new

    @staticmethod
    def average(other):
        return statistics.mean(other)

    def __eq__(self, other):
        return ExtendList.average(self.lst) == ExtendList.average(other.lst)

    def __gt__(self, other):
        return ExtendList.average(self.lst) > ExtendList.average(other.lst)

    def __lt__(self, other):
        return ExtendList.average(self.lst) < ExtendList.average(other.lst)

    def __le__(self, other):
        return ExtendList.average(self.lst) <= ExtendList.average(other.lst)

    def __ge__(self, other):
        return ExtendList.average(self.lst) >= ExtendList.average(other.lst)

    def __ne__(self, other):
        return ExtendList.average(self.lst) != ExtendList.average(other.lst)


class TypeList(ExtendList):
    # def __init__(self,lst):
    #     super().__init__(lst)
    def __eq__(self, other):
        return self.lst[-1] == other.lst[-1]

    def __ne__(self, other):
        return self.lst[-1] != other.lst[-1]


