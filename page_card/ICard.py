from abc import ABC, abstractmethod


class ICard(ABC):
    @abstractmethod
    def __init__(self, **attrs):
        raise NotImplementedError("This is an Interface Method.")

    @property
    @abstractmethod
    def element(self):
        raise NotImplementedError("This is an Interface Method.")

    @element.setter
    @abstractmethod
    def element(self, item: str):
        raise NotImplementedError("This is an Interface Method.")

    @property
    @abstractmethod
    def content(self):
        raise NotImplementedError("This is an Interface Method.")

    @content.setter
    @abstractmethod
    def content(self, item: str):
        raise NotImplementedError("This is an Interface Method.")

    @property
    @abstractmethod
    def id(self):
        raise NotImplementedError("This is an Interface Method.")

    @id.setter
    @abstractmethod
    def id(self, item: str):
        raise NotImplementedError("This is an Interface Method.")

    @property
    @abstractmethod
    def attr(self):
        raise NotImplementedError("This is an Interface Method.")

    @attr.setter
    @abstractmethod
    def attr(self, item: dict):
        raise NotImplementedError("This is an Interface Method.")

    @abstractmethod
    def set_attr(self, *, key: str, value: str):
        raise NotImplementedError("This is an Interface Method.")

    @abstractmethod
    def make_dict(self):
        """Make a new card in DICT form"""
        raise NotImplementedError("This is an Interface Method.")

    @abstractmethod
    def make_html(self):
        raise NotImplementedError("This is an Interface Method.")

    @abstractmethod
    def make_json(self):
        raise NotImplementedError("This is an Interface Method.")