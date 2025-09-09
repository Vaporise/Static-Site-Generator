import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_to_html_error_raised(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_none(self):
        node = HTMLNode(props=None)
        self.assertEqual(node.props_to_html(), "")

    def test_all_props_none(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

    def test_single_prop(self):
        node = HTMLNode(props={"href": "https://test.com"})
        self.assertEqual(node.props_to_html(), ' href="https://test.com"')

    def test_multiple_props(self):
        node = HTMLNode(props={"href": "https://test.com", "target": "_blank"})
        out = node.props_to_html()
        self.assertIn(' href="https://test.com"', out)
        self.assertIn(' target="_blank"', out)
        self.assertTrue(out.startswith(" "))

    def test_non_string_prop_value(self):
        node = HTMLNode(props={"data-id": 42})
        self.assertEqual(node.props_to_html(), ' data-id="42"')