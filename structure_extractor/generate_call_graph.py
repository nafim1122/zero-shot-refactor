
import ast
import networkx as nx

class CallGraphVisitor(ast.NodeVisitor):
    def __init__(self):
        self.graph = nx.DiGraph()
        self.current_function = None

    def visit_FunctionDef(self, node):
        self.current_function = node.name
        self.graph.add_node(self.current_function)
        self.generic_visit(node)

    def visit_Call(self, node):
        if hasattr(node.func, 'id'):
            called_func = node.func.id
            self.graph.add_edge(self.current_function, called_func)
        self.generic_visit(node)

def build_call_graph(code):
    tree = ast.parse(code)
    visitor = CallGraphVisitor()
    visitor.visit(tree)
    return visitor.graph

if __name__ == "__main__":
    import sys
    with open(sys.argv[1], "r") as file:
        code = file.read()
    graph = build_call_graph(code)
    nx.nx_pydot.write_dot(graph, "call_graph.dot")
    print("Call graph saved to call_graph.dot")
