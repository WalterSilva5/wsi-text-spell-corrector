import pytest
from unittest.mock import patch, mock_open
from main import display_menu, main

@patch('builtins.input', return_value='1')
@patch('builtins.print')
def test_display_menu(mock_print, mock_input):
    result = display_menu()
    assert result == '1'
    mock_print.assert_any_call("Configure o spaCy e o Hunspell corretamente antes de executar.")
    mock_print.assert_any_call("Execute com: python main.py")
    mock_print.assert_any_call("\nMenu:")
    mock_print.assert_any_call("1 - Corrigir texto do arquivo input.txt")
    mock_print.assert_any_call("2 - Sair")

@patch('main.NLPProcessor.correct_text', return_value='corrected text')
@patch('main.FileManager.read_input_file', return_value='input text')
@patch('main.FileManager.write_output_file')
@patch('builtins.input', return_value='1')
def test_main_option_1(mock_input, mock_write, mock_read, mock_correct):
    main()
    mock_read.assert_called_once_with('input.txt')
    mock_correct.assert_called_once_with('input text')
    mock_write.assert_called_once_with('output.txt', 'corrected text')