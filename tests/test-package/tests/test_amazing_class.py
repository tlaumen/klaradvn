
from package_one.amazing_class import CoolNewList

import pytest
from dataclasses import dataclass

@dataclass
class CoolNewList:
    elements: list[int]

    def add_element(self, n: int):
        self.elements.append(n)
    
    def remove_element(self, idx: int):
        if idx > len(self.elements) - 1:
            raise IndexError(f"List is only {len(self.elements)} long, the index you provided: {idx} does not exist")
        self.elements.pop(idx)
    
    def reverse(self):
        self.elements.reverse()

# Test setup for testing CoolNewList
@pytest.fixture()
def test_list():
    return CoolNewList([])

# Test: Add element to an empty list
def test_add_element_empty_list(test_list):
    # Arrange
    value_to_add = 5
    
    # Act
    test_list.add_element(value_to_add)
    
    # Assert
    assert test_list.elements == [value_to_add], "The list should contain the added element"

# Test: Add multiple elements to a list
def test_add_multiple_elements(test_list):
    # Arrange
    values_to_add = [1, 2, 3]
    
    # Act
    for value in values_to_add:
        test_list.add_element(value)
    
    # Assert
    assert test_list.elements == values_to_add, "The list should contain all added elements"

# Test: Remove element from a non-empty list
def test_remove_element_non_empty_list(test_list):
    # Arrange
    initial_values = [1, 2, 3]
    index_to_remove = 1
    
    # Act
    test_list.elements = initial_values
    test_list.remove_element(index_to_remove)
    
    # Assert
    assert test_list.elements == [initial_values[0], initial_values[2]], "The element should be removed correctly"

# Test: Attempt to remove an element at an invalid index (should raise IndexError)
def test_remove_invalid_index(test_list):
    # Arrange
    index_to_remove = 5
    
    # Act and Assert
    with pytest.raises(IndexError, match=f"List is only 0 long"):
        test_list.remove_element(index_to_remove)

# Test: Reverse an empty list
def test_reverse_empty_list(test_list):
    # Act
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [], "The reversed empty list should be empty"

# Test: Reverse a non-empty list
def test_reverse_non_empty_list(test_list):
    # Arrange
    initial_values = [1, 2, 3]
    
    # Act
    test_list.elements = initial_values
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [3, 2, 1], "The list should be reversed correctly"

# Test: Reverse a list with duplicate elements
def test_reverse_with_duplicates(test_list):
    # Arrange
    initial_values = [4, 5, 6, 4]
    
    # Act
    test_list.elements = initial_values
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [4, 6, 5, 4], "The list should be reversed correctly with duplicates"

# Test: Reverse a single-element list
def test_reverse_single_element_list(test_list):
    # Arrange
    value = 1
    
    # Act
    test_list.elements = [value]
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [value], "The reversed single-element list should remain the same"

# Test: Reverse an empty list after adding elements and then reversing it again
def test_reverse_after_adding_elements(test_list):
    # Arrange
    initial_values = [1, 2, 3]
    
    # Act
    for value in initial_values:
        test_list.add_element(value)
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [3, 2, 1], "The list should be reversed correctly after adding elements"

# Test: Reverse a list with multiple duplicates and then reversing it again
def test_reverse_with_duplicates_after_adding_elements(test_list):
    # Arrange
    initial_values = [4, 5, 6, 4]
    
    # Act
    for value in initial_values:
        test_list.add_element(value)
    test_list.reverse()
    
    # Assert
    assert test_list.elements == [4, 6, 5, 4], "The list should be reversed correctly after adding elements and with duplicates"