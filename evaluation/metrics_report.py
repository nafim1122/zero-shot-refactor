
from evaluation.cyclomatic import cyclomatic_complexity
from evaluation.readability import readability_score

def generate_report(before_code, after_code):
    return {
        "Before Cyclomatic": cyclomatic_complexity(before_code),
        "After Cyclomatic": cyclomatic_complexity(after_code),
        "Before Readability": readability_score(before_code),
        "After Readability": readability_score(after_code)
    }
