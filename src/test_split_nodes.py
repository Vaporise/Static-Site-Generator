import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node

class Testsplit_nodes(unittest.TestCase):

    def test_node_split_code(self):
        node = [TextNode("This is a test `code` block", TextType.Text)]
        new_node = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual([
    TextNode("This is a test ", TextType.TEXT),
    TextNode("code", TextType.CODE),
    TextNode(" block", TextType.TEXT),
], new_node)


if __name__ == "__main__":
    unittest.main()