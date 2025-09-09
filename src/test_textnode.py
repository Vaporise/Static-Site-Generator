import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase): # Unit test to check if 2 nodes that are equal match
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self): #Unit test to check if not equal specifically text type
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertNotEqual(node, node2)

    def test_codeeq(self): # Test for TextType Code being equal
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_unequaltext(self): # Test for text being different
        node = TextNode("This is a dog node", TextType.TEXT)
        node2 = TextNode("This is a nose node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_emptyurl(self): # Test if the url is empty that none is produced
        node = TextNode("This is a node", TextType.LINK, None)
        self.assertIsNone(node.url)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_incorrect_type(self):
        node = TextNode("Test", "PASTA")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)

    
    def test_image(self):
        node = TextNode("alt text here", TextType.IMAGE, url="https://example.com/cat.png")
        html = text_node_to_html_node(node)

        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props.get("src"), "https://example.com/cat.png")
        self.assertEqual(html.props.get("alt"), "alt text here")

if __name__ == "__main__":
    unittest.main()