import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "DOG")
        self.assertEqual(node.to_html(), "<b>DOG</b>")

    def test_leaf_no_value_raise(self):
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_multiple_children(self):
        parent = ParentNode("p", [
            LeafNode("b", "Bold"),
            LeafNode(None, " and "),
            LeafNode("i", "italic"),
        ])
        self.assertEqual(parent.to_html(), "<p><b>Bold</b> and <i>italic</i></p>")

    def test_parent_nested_three_levels(self):
        n = ParentNode("div", [
                ParentNode("section", [
                    ParentNode("span", [LeafNode(None, "hi")])
                    ])
            ])
        self.assertEqual(n.to_html(), "<div><section><span>hi</span></section></div>")

    def test_parent_child_type_error(self):
        bad = ParentNode("div", ["not a node"])
        with self.assertRaises(AttributeError):
            bad.to_html()
    
    def test_parent_mixed_with_props_and_grandchildren(self):
        n = ParentNode("ul", [
            ParentNode("li", [LeafNode(None, "one")], {"class": "a"}),
            ParentNode("li", [LeafNode("b", "two")]),
        ], {"data-x": "1"})
        self.assertEqual(n.to_html(), '<ul data-x="1"><li class="a">one</li><li><b>two</b></li></ul>')