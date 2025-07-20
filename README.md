
# Structural-Aware Zero-Shot Code Refactoring with LLMs

## Objective
Use Large Language Models (LLMs) to refactor code using abstract syntax tree (AST) or call graph input, without training data (zero-shot).

## Project Structure
- `sample_projects/`: Source code to refactor
- `structure_extractor/`: Extracts AST/call graphs
- `llm_interface/`: Interfaces with GPT-4
- `evaluation/`: Evaluates quality before/after
- `results/`: Stores outputs and reports

## Run Instructions
1. Add your OpenAI API key to `main.py`
2. Install requirements: `pip install openai textstat radon networkx`
3. Run `python main.py`


## 🧠 AI Research Utility
This project demonstrates how to use structural code representations (like ASTs and call graphs) combined with LLMs to automatically refactor code in a zero-shot setting. Ideal for:
- AI-assisted software engineering
- Developer tools research
- NLP x Program Synthesis studies

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
