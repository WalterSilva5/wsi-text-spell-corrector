import spacy
import pytest
from unittest.mock import patch, MagicMock
from spacy.tokens import Doc, Token
from src.nlp_processor import NLPProcessor

@pytest.fixture
def nlp_processor():
    with patch('spacy.load') as mock_spacy, patch('hunspell.HunSpell') as mock_hunspell:
        mock_hunspell_instance = mock_hunspell.return_value
        mock_spacy_instance = mock_spacy.return_value
        processor = NLPProcessor("pt_core_news_md", 'dummy_dic_path', 'dummy_aff_path')
        yield processor, mock_spacy, mock_hunspell_instance

def test_load_nlp_model(nlp_processor):
    processor, mock_spacy, _ = nlp_processor
    mock_spacy.reset_mock()
    processor.load_nlp_model("pt_core_news_md")
    mock_spacy.assert_called_once_with("pt_core_news_md")

def test_spell_check_token_correct(nlp_processor):
    processor, _, mock_hunspell = nlp_processor
    mock_hunspell.spell.return_value = True
    token = "correct"
    result = processor.spell_check_token(token)
    assert result == token

def test_spell_check_token_incorrect(nlp_processor):
    processor, _, mock_hunspell = nlp_processor
    mock_hunspell.spell.return_value = False
    mock_hunspell.suggest.return_value = ["suggestion"]
    token = "incorret"
    result = processor.spell_check_token(token)
    assert result == "suggestion"

def test_correct_text(nlp_processor):
    processor, mock_spacy, mock_hunspell = nlp_processor
    nlp = spacy.blank("pt")
    doc = Doc(nlp.vocab, words=["eu gosto de cumer"])
    mock_spacy.return_value = doc
    mock_hunspell.spell.return_value = False
    mock_hunspell.suggest.return_value = ["correto"]
    text = "incorret"
    result = processor.correct_text(text)
    print(f"Corrected text: {result}") 
    assert result == ""