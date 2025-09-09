

class HTMLNode:
    
    def __init__(self, tag = None, value = None , children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if not self.props:
            return ""
        parts = []
        for k, v in self.props.items():
            parts.append(f' {k}="{v}"')
        return "".join(parts)
    
    def __repr__(self):
         return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
        
