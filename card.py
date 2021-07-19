
def htmlTag(f):
    pass


class Card:

    __attr = {}

    def __init__(self, id_name: str, element: str, content: str, **attrs):
        self.__attr['id'] = id_name
        self.__attr['element'] = element
        self.__attr['content'] = content
        self.__attr.update(attrs)

    def __call__(self):
        # convert class to html tag
        return self.__attr


class Deck(Card):
    def __init__(self, id_name: str):
        Card.__init__(self,
                      id_name=id_name,
                      element='div',
                      content='')
        self.__attr['child'] = {}

    def add(self, card: Card):
        self.__attr['child'].update(card())
