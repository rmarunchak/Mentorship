Python Task: Nested Data Organizer

Task Overview:
Create a Python function organize_data that accepts a list 
of mixed data types including dictionaries, lists, and individual elements. 
The function should classify and return a dictionary categorizing these items 
into lists under keys 'lists', 'dicts', and 'singles' for individual non-iterable elements.

Input/Output Examples:
Input: [{"name": "Alice"}, [1, 2, 3], "hello", {"age": 30}, 42]
Output:

{
  "lists": [[1, 2, 3]],
  "dicts": [{"name": "Alice"}, {"age": 30}],
  "singles": ["hello", 42]
}
Difficulty Levels for the Task:
Level D (Basic): Classify lists and individual elements.
Level C (Intermediate): Classify dictionaries, lists, and individual elements.
Level B (Advanced): Same as intermediate, but ensure functionality with nested lists and dictionaries.
Level A (Expert): Include error handling for non-iterable types not specified and ensure it works with any nested complexity.