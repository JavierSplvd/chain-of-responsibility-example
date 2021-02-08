from handler import PrefixHandler, CacheHandler
from request import Request

if __name__ == "__main__":
    h1 = PrefixHandler()
    h2 = CacheHandler()
    h1.set_next(h2)

    r = Request("lunes")

    print(h1.process(r.data))
    print(h1.process(r.data))
    