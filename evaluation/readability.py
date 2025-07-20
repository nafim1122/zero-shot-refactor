
import textstat

def readability_score(code_str):
    return textstat.flesch_reading_ease(code_str)
