# GRAYBOX
_for the Code Evaluator Project_

## Overview
Graybox is a tool for gray box testing of Python code, specially value functions.

The idea is providing the python code, the function that has to be called, the given parameters and the 
expected return value to test the python code.

## Installation
`pip install graybox`

## Usage
To use the library you have to import the `evaluate_gray_box` method located in `graybox.graybox` module

```python
from graybox.graybox import evaluate_gray_box

solution = '''def hello(name):
return f'Hello {name}!'
'''

function_name = 'hello'

arguments = ['Python']

expected = 'Hello Python!'

print(evaluate_gray_box(solution,function_name,arguments,expected))
```