
import radon.complexity as cc_mod
from radon.visitors import ComplexityVisitor

def cyclomatic_complexity(source_code):
    blocks = cc_mod.cc_visit(source_code)
    return sum(block.complexity for block in blocks)
