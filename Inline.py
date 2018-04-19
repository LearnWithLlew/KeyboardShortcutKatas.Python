def n():
    return False


class Inline:
    e = 2

    def __init__(self):
        self.a = 5

    def practice(self):
        i = 2
        s = 2 - i
        j = (self.b() - self.a + i)
        m = self.f(3)
        l = m + j
        if (n()):
            m += 56
        k = lambda: l - Inline.c(self.e)

        q = 1 - O.create().p
        return 42 + k() + q + Extensions.h(7) + s

    def f(self, G):
        return -3 + G
    @staticmethod
    def c(d):
        return d

    def b(self):
        return 5


class Extensions:
    def h(that):
        return that - 7


class O:
    p = 1

    @staticmethod
    def create():
        return O()


if __name__ == "__main__":
    print(Inline().practice())