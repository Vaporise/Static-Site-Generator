import unittest

from split_nodes import split_nodes_delimiter, text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
from extract_markdown import extract_markdown_images, extract_markdown_links
from split_nodes import split_nodes_image,split_nodes_link, text_to_textnodes

class Testsplit_nodes(unittest.TestCase):

    def test_node_split_code(self):
        node = [TextNode("This is a test `code` block", TextType.TEXT)]
        new_node = split_nodes_delimiter(node, "`", TextType.CODE)
        self.assertEqual([
        TextNode("This is a test ", TextType.TEXT),
        TextNode("code", TextType.CODE),
        TextNode(" block", TextType.TEXT),
        ], new_node)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )


class Test_extract(unittest.TestCase):

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

class TestTextToTextNodes(unittest.TestCase):
    def test_plain_text(self):
        out = text_to_textnodes("hello world")
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text, "hello world")
        self.assertEqual(out[0].text_type, TextType.TEXT)

    def test_code_only(self):
        out = text_to_textnodes("`x = 1`")
        self.assertEqual([n.text_type for n in out], [TextType.CODE])
        self.assertEqual(out[0].text, "x = 1")

    def test_bold_and_text(self):
        out = text_to_textnodes("a **b** c")
        types = [n.text_type for n in out]
        texts = [n.text for n in out]
        self.assertEqual(types, [TextType.TEXT, TextType.BOLD, TextType.TEXT])
        self.assertEqual(texts, ["a ", "b", " c"])

    def test_italic_and_text(self):
        out = text_to_textnodes("a _b_ c")
        types = [n.text_type for n in out]
        texts = [n.text for n in out]
        self.assertEqual(types, [TextType.TEXT, TextType.ITALIC, TextType.TEXT])
        self.assertEqual(texts, ["a ", "b", " c"])

    def test_link(self):
        out = text_to_textnodes("see [site](https://ex.com)")
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].text_type, TextType.TEXT)
        self.assertEqual(out[0].text, "see ")
        self.assertEqual(out[1].text_type, TextType.LINK)
        self.assertEqual(out[1].text, "site")
        self.assertEqual(out[1].url, "https://ex.com")

    def test_image(self):
        out = text_to_textnodes("img ![alt](https://ex.com/a.png)")
        self.assertEqual(len(out), 2)
        self.assertEqual(out[0].text, "img ")
        self.assertEqual(out[1].text_type, TextType.IMAGE)
        self.assertEqual(out[1].text, "alt")
        self.assertEqual(out[1].url, "https://ex.com/a.png")

    def test_code_protects_emphasis(self):
        out = text_to_textnodes("`a **b** _c_`")
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0].text_type, TextType.CODE)
        self.assertEqual(out[0].text, "a **b** _c_")

    def test_assignment_example(self):
        s = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        out = text_to_textnodes(s)
        types = [n.text_type for n in out]
        texts = [n.text for n in out]
        urls = [getattr(n, "url", None) for n in out]

        self.assertEqual(types, [
            TextType.TEXT, TextType.BOLD, TextType.TEXT, TextType.ITALIC,
            TextType.TEXT, TextType.CODE, TextType.TEXT, TextType.IMAGE,
            TextType.TEXT, TextType.LINK
        ])
        self.assertEqual(texts[0], "This is ")
        self.assertEqual(texts[1], "text")
        self.assertEqual(texts[3], "italic")
        self.assertEqual(texts[5], "code block")
        self.assertEqual(texts[7], "obi wan image")
        self.assertEqual(urls[7], "https://i.imgur.com/fJRm4Vk.jpeg")
        self.assertEqual(texts[9], "link")
        self.assertEqual(urls[9], "https://boot.dev")




if __name__ == "__main__":
    unittest.main()