
import ast

def extract_ast_structure(file_path):
    with open(file_path, "r") as file:
        source = file.read()
    tree = ast.parse(source)
    return ast.dump(tree, indent=4)

if __name__ == "__main__":
    import sys
    print(extract_ast_structure(sys.argv[1]))
