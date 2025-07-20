
from structure_extractor.extract_ast import extract_ast_structure
from llm_interface.gpt4_api_call import call_gpt4
from evaluation.metrics_report import generate_report

API_KEY = "your-openai-api-key"

def main():
    file_path = "sample_projects/flask_sample.py"
    structure = extract_ast_structure(file_path)

    with open("llm_interface/prompt_template.txt", "r") as f:
        template = f.read()

    prompt = template.replace("{structure}", structure)
    refactored_code = call_gpt4(prompt, API_KEY)

    with open(file_path, "r") as f:
        original_code = f.read()

    report = generate_report(original_code, refactored_code)
    print("=== Refactoring Evaluation Report ===")
    for key, value in report.items():
        print(f"{key}: {value}")

    with open("results/before_after_diff/refactored_flask_sample.py", "w") as f:
        f.write(refactored_code)

if __name__ == "__main__":
    main()
