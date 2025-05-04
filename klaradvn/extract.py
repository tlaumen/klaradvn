import os
import ast
import inspect
from pathlib import Path
from typing import Optional, Union


def extract_function_code(folder_path: str, function_name: str) -> Optional[tuple[str, Path]]:
    """
    Find and return the code of a specified Python function within a folder.
    
    Args:
        function_name: The name of the function to search for
        folder_path: Path to the folder containing Python files to search
        
    Returns:
        The complete function code as a string if found, None otherwise
    """
    # Check if folder exists
    if not os.path.isdir(folder_path):
        raise ValueError(f"Folder '{folder_path}' does not exist")
    
    # Function to extract the function code from an AST node
    def get_function_code(node, source_code):
        if isinstance(node, ast.FunctionDef) and node.name == function_name:
            # Get line numbers (subtract 1 as line numbers are 1-indexed)
            start_line = node.lineno - 1
            end_line = node.end_lineno if hasattr(node, 'end_lineno') else start_line
            
            # For older Python versions that don't have end_lineno
            if not hasattr(node, 'end_lineno'):
                lines = source_code.splitlines()
                indent = len(lines[start_line]) - len(lines[start_line].lstrip())
                
                # Find the end of the function by tracking indentation
                end_line = start_line
                for i in range(start_line + 1, len(lines)):
                    if i >= len(lines) or (lines[i].strip() and len(lines[i]) - len(lines[i].lstrip()) <= indent):
                        end_line = i - 1
                        break
                    end_line = i
            
            # Extract the function code
            lines = source_code.splitlines()[start_line:end_line+1]
            return '\n'.join(lines)
        return None
    
    # Recursively walk the AST to find the function
    def find_function_in_ast(node, source_code):
        # Try to extract the function from the current node
        result = get_function_code(node, source_code)
        if result:
            return result
        
        # Recursively search in child nodes
        for child in ast.iter_child_nodes(node):
            result = find_function_in_ast(child, source_code)
            if result:
                return result
        return None
    
    # Search through all Python files in the folder
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        source_code = f.read()
                    
                    # Parse the file into an AST
                    try:
                        tree = ast.parse(source_code)
                        result = find_function_in_ast(tree, source_code)
                        if result:
                            return result, Path(file_path)
                    except SyntaxError:
                        # Skip files with syntax errors
                        continue
                except Exception as e:
                    print(f"Error processing {file_path}: {str(e)}")
    
    return None, None