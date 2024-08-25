import pytest
from organizer import Organizer

organizer = Organizer()


def test_basic_classification():
    assert organizer.organize_data([1, "hello", [1, 2, 3]]) == {"lists": [[1, 2, 3]], "dicts": [], "singles": [1, "hello"]}


def test_intermediate_classification():
    input_data = [{"name": "Alice"}, [1, 2, 3], "hello"]
    expected = {"lists": [[1, 2, 3]], "dicts": [{"name": "Alice"}], "singles": ["hello"]}
    assert organizer.organize_data(input_data) == expected


def test_advanced_classification():
    input_data = [{"name": "Alice"}, [1, 2, [3, {"key": "value"}]], "hello", 42]
    expected = {"lists": [[1, 2, [3, {"key": "value"}]]], "dicts": [{"name": "Alice"}], "singles": ["hello", 42]}
    assert organizer.organize_data(input_data) == expected


def test_expert_classification():
    input_data = [{"name": "Alice", "details": {"age": 30, "hobbies": ["reading", {"sport": "cycling"}]}}, "hello", 42,
                  ["list", ["nested", {"deep": "value"}]]]
    expected = {
        "lists": [["list", ["nested", {"deep": "value"}]]],
        "dicts": [{"name": "Alice", "details": {"age": 30, "hobbies": ["reading", {"sport": "cycling"}]}}],
        "singles": ["hello", 42]
    }
    assert organizer.organize_data(input_data) == expected
