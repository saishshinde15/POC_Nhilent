#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from nihilentpoc.crew import Nihilentpoc

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'file_path': '/Users/saish/Downloads/AutoFilePOC/nihilentpoc/src/nihilentpoc/word-file.pdf',
        'modifications': "Make changes to the first table in the file by adding random names to it with gender"
    }
    
    try:
        Nihilentpoc().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
