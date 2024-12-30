class FileManager:
    @staticmethod
    def read_input_file(filename: str) -> str:
        try:
            with open(filename, "r", encoding="utf-8") as infile:
                return infile.read()
        except FileNotFoundError:
            print(f"Arquivo {filename} não encontrado.")
            return ""

    @staticmethod
    def write_output_file(filename: str, text: str):
        with open(filename, "w", encoding="utf-8") as outfile:
            outfile.write(text)