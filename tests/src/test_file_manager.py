import pytest
from unittest.mock import patch, mock_open
from src.file_manager import FileManager

@patch("builtins.open", new_callable=mock_open, read_data="file content")
def test_read_input_file(mock_file):
    result = FileManager.read_input_file("dummy_file.txt")
    assert result == "file content"
    mock_file.assert_called_once_with("dummy_file.txt", "r", encoding="utf-8")

@patch("builtins.open", new_callable=mock_open)
def test_write_output_file(mock_file):
    FileManager.write_output_file("dummy_file.txt", "file content")
    mock_file.assert_called_once_with("dummy_file.txt", "w", encoding="utf-8")
    mock_file().write.assert_called_once_with("file content")