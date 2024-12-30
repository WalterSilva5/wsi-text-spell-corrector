from src.nlp_processor import NLPProcessor
from src.file_manager import FileManager

def display_menu():
    print("Configure o spaCy e o Hunspell corretamente antes de executar.")
    print("Execute com: python main.py")
    print("\nMenu:")
    print("1 - Corrigir texto do arquivo input.txt")
    print("2 - Sair")
    return input("Escolha uma opção: ")

def main():
    opcao = display_menu()

    if opcao == "1":
        nlp_processor = NLPProcessor("pt_core_news_md", '/usr/share/hunspell/pt_BR.dic', '/usr/share/hunspell/pt_BR.aff')
        text = FileManager.read_input_file("input.txt")
        if text:
            corrected = nlp_processor.correct_text(text)
            FileManager.write_output_file("output.txt", corrected)

if __name__ == "__main__":
    main()