## Free Copilot Limitations
Links: 4 up to 2 directorys deep.

    OK: `http://cyber.canton.edu/advisees/test.json` 
    NOT OK: `http://cyber.canton.edu/advisees/test/another.json`

Instructions: 8k characters

Hypothesis: converting pdf to structured data such as json may be more effective

# How to use
`cd helpers`

make sure data in ./knowledge is up to date

`uv run combine.py`

`uv run instruction_check.py`
