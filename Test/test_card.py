from page_card.card import *
import unittest


class TestCalc(unittest.TestCase):

    def setUp(self):
        # This method is use to set up all the necessary things.

        """
        self.card1 -> object created by Card
        self.card2 -> dict to compare
        """
        self.card1 = Card(ID="lorem", ELEMENT="p", CONTENT="Lorem Ipsum", CLASS="paragraph")
        self.card2 = {
            "ID": "lorem",
            "ELEMENT": "p",
            "CONTENT": "Lorem Ipsum",
            "CLASS": "paragraph"
        }

        """
        self.deck1 -> object created by Deck
        self.deck2 -> dict to compare
        """
        self.deck1 = Deck(ID="test", CARDS=[self.card1])
        self.deck2 = {
            "ID": "test",
            "CARDS": [self.card2],
            "ELEMENT": "div"
        }

    def test_card(self):
        # Compares card1 with card2
        self.assertEqual(self.card2, self.card1.make_dict())

    def test_deck(self):
        # Compares deck1 with deck2
        self.assertEqual(self.deck2, self.deck1.make_dict())

    def test_get_properties_card(self):
        # Test accessor of card
        self.assertEqual('p', self.card1.element)
        self.assertEqual('Lorem Ipsum', self.card1.content)
        self.assertEqual('lorem', self.card1.id)
        self.assertEqual('paragraph', self.card1.attr['CLASS'])
        print(self.card1.attr['CLASS'])
        self.assertEqual({'CLASS': 'paragraph'}, self.card1.attr)

    def test_set_properties_card(self):
        # Test mutator of card

        # Setting up the values
        self.card1.id = 'test'
        self.card1.element = 'a'
        self.card1.content = 'lipsum'
        self.card1.attr['HREF'] = 'http://google.com/'
        print(self.card1.attr['HREF'])

        # Compares the result
        self.assertEqual('a', self.card1.element)
        self.assertEqual('lipsum', self.card1.content)
        self.assertEqual('test', self.card1.id)
        self.assertEqual('http://google.com/', self.card1.attr['HREF'])

        # Setting the values with an alternative
        self.card1.attr = {"HREF": "http://pluralsight.com/"}
        self.assertEqual('http://pluralsight.com/', self.card1.attr['HREF'])
        print(self.card1.attr)

        # Test .set_attr method
        self.card1.set_attr(key="CLASS", value="paragraph link")
        self.assertEqual('paragraph link', self.card1.attr['CLASS'])
        print(self.card1.attr)

    def test_get_properties_deck(self):
        # Test accessor of deck
        self.assertEqual('div', self.deck1.element)
        self.assertEqual('test', self.deck1.id)

    def test_set_properties_deck(self):
        # Test mutator of deck

        # Setting up the values
        self.deck1.id = 'test1'
        self.deck1.attr['CLASS'] = 'section1'
        print(self.card1.attr['CLASS'])

        # Compares the result
        self.assertEqual('test1', self.deck1.id)
        self.assertEqual('section1', self.deck1.attr['CLASS'])

        # Setting the values with an alternative
        self.card1.attr = {"CLASS": "section2"}
        self.assertEqual('section2', self.card1.attr['CLASS'])
        print(self.card1.attr)

        # Test .set_attr method
        self.card1.set_attr(key="STYLE", value="color=red;")
        self.assertEqual('color=red;', self.card1.attr['STYLE'])
        print(self.card1.attr)

    def test_add_card(self):
        # Test .add_card method (Deck exclusive)
        self.deck1.add(self.card1)
        self.deck2['CARDS'].append(self.card2.copy())
        self.assertEqual(self.deck2, self.deck1.make_dict())

    def test_exception_deck(self):
        # Test exceptions of deck
        with self.assertRaises(NotImplementedError):
            self.deck1.content()

    def test_exception_card(self):
        # Test exceptions of card
        with self.assertRaises(TypeError):
            self.card1.attr = []
            self.card1.element = 1
            self.card1.content = 2
            self.card1.id = 3

            self.card1.set_attr(key=None, value='test')
            self.card1.set_attr(key='test', value=None)

    def test_deck_to_tag(self):
        self.card1.attr = {
            "CLASS": "paragraph link",
            "STYLE": "color=\"red;\""
        }
        test = """<div id="test" >

<p id="lorem" CLASS="paragraph link" STYLE="color="red;"">
Lorem Ipsum
</p>

</div>"""

        self.assertEqual(test, self.deck1.make_html())


if __name__ == '__main__':
    unittest.main()
