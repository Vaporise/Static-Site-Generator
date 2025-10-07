import unittest

from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType, text_node_to_html_node
from extract_markdown import extract_markdown_images, extract_markdown_links

class Testsplit_nodes(unittest.TestCase):

    def test_node_split_code(self):
        node = [TextNode("This is a test `code` block", TextType.TEXT)]
        new_node = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual([
    TextNode("This is a test ", TextType.TEXT),
    TextNode("code", TextType.CODE),
    TextNode(" block", TextType.TEXT),
], new_node)


class Test_extract(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

if __name__ == "__main__":
    unittest.main()