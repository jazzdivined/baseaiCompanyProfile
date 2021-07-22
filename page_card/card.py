from abc import ABC

from page_card.ICard import ICard


def HTML(f):
    # Converts from card
    def convert_card(*arg):
        attr = arg[0]
        id_name = attr.pop('ID')
        element = attr.pop('ELEMENT')
        content = attr.pop('CONTENT')

        attributes = [f'{key}="{value}"' for key, value in attr.items()]
        attributes = " ".join(attributes)
        output = f"<{element} id=\"{id_name}\" {attributes}>\n{content}\n</{element}>"

        return output

    def convert_deck(*arg):
        attr = arg[0]
        id_name = attr.pop('ID')
        element = attr.pop('ELEMENT')
        content = attr.pop('CARDS')

        cards = [convert_card(i) for i in content]
        content = "\n\n".join(cards)

        attributes = [f'{key}="{value}"' for key, value in attr.items()]
        attributes = " ".join(attributes)
        output = f"<{element} id=\"{id_name}\" {attributes}>\n\n{content}\n\n</{element}>"

        return output

    def convert(self=None):
        if 'CARDS' not in f(self):
            return convert_card(f(self))
        else:
            return convert_deck(f(self))

    return convert


def JSON(f):
    pass


class Card(ICard, ABC):

    def __init__(self, ID: str = "", ELEMENT: str = "", CONTENT: str = "", **attrs):
        self.__id = ID
        self.__element = ELEMENT
        self.__content = CONTENT
        self.__attr = attrs.copy()
        self.__export = {}

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, item: str):
        self.__element = item

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, item: str):
        self.__content = item

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, item: str):
        self.__id = item

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, item: dict):
        self.__attr.update(item)

    def set_attr(self, *, key: str, value: str):
        if isinstance(key, str) and isinstance(value, str):
            self.__attr[key] = value

        else:
            raise TypeError("Key and value must be a string!")

    def make_dict(self):
        """Make a new card in DICT form"""
        self.__export = self.__attr.copy()
        self.__export['ID'] = self.__id
        self.__export['ELEMENT'] = self.__element
        self.__export['CONTENT'] = self.__content
        return self.__export

    @HTML
    def make_html(self):
        return self.make_dict()

    def make_json(self):
        pass

    @staticmethod
    def __isEmpty(item):
        return item is None


class Deck(ICard, ABC):

    def __init__(self, ID: str = "", CARDS: list = None, **attrs):
        self.__id = ID
        self.__element = "div"
        self.__attr = attrs.copy()
        if CARDS is None:
            self.__cards = []
        else:
            for card in CARDS:
                if not isinstance(card, Card):
                    raise TypeError("List elements must be Card class")
            self.__cards = CARDS.copy()
        self.__export = {}

    def add(self, card: Card):
        self.__cards.append(card)

    @property
    def element(self):
        return self.__element

    @element.setter
    def element(self, item):
        raise NotImplementedError("Read-only property.")

    @property
    def content(self):
        raise NotImplementedError("Unsupported property.")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, item: str):
        self.__id = item

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, item: dict):
        self.__attr.update(item)

    def set_attr(self, *, key: str, value: str):
        if isinstance(key, str) and isinstance(value, str):
            self.__attr[key] = value

        else:
            raise TypeError("Key and value must be a string!")

    def make_dict(self):
        self.__export = self.attr.copy()
        self.__export['ID'] = self.id
        temp = [card.make_dict() for card in self.__cards]
        self.__export['CARDS'] = temp
        self.__export['ELEMENT'] = self.__element
        return self.__export

    @HTML
    def make_html(self):
        return self.make_dict()

    def make_json(self):
        pass
