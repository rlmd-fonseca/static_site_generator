from __future__ import annotations


class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list[HTMLNode] = None,
                 props: dict[str, str] = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag: str | None, value: str | None, props: dict[str, str] | None = None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value
        props = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""
        return f"<{self.tag}{props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str, str] = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode does not have a tag")

        if self.children is None:
            raise ValueError("ParentNode does not have children")

        props = " " + " ".join(f'{key}="{value}"' for key, value in self.props.items()) if self.props else ""

        return f"<{self.tag}{props}>{''.join(child.to_html() for child in self.children)}</{self.tag}>"
