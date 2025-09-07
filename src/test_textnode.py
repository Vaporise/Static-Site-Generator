import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase): # Unit test to check if 2 nodes that are equal match
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self): #Unit test to check if not equal specifically text type
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_codeeq(self):
        node = 


if __name__ == "__main__":
    unittest.main()