# How to use
ensure data in directory `./knowledge` is up to date

`uv run main.py`

Script will check to see if the instructions has below 8k characters.

All outputs will be saved to ./output directory.

provide the agent with data in ./output directory

## Free Copilot Limitations
### Links:
4 up to 2 directorys deep.

NOTE: the ai-agent cannot provide links in responses from urls

    OK: `http://cyber.canton.edu/advisees/test.json` 
    NOT OK: `http://cyber.canton.edu/advisees/test/another.json`

//TODO What is the limitation of provided web link context?
### Instructions: 
8k characters max.