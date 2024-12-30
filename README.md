# WSI - Corretor Ortográfico

Este programa carrega um modelo de processamento de linguagem natural (NLP) e um dicionário Hunspell para realizar correção ortográfica em um texto em português. Ele corrige cada token (palavra) do texto, sugerindo a correção mais provável se a palavra estiver incorreta.

# Setup

1. Crie um ambiente virtual:

    ```sh
    python -m virtualenv venv
    source ./venv/bin/activate
    ```

2. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

3. Instale o modelo do spaCy em pt-br:

    ```sh
    python -m spacy download pt_core_news_md
    ```

4. Instale o hunspell-pt-br:

    - Ubuntu: `sudo apt-get install hunspell-pt-br`
    - macOS: `brew install hunspell-pt-br`
    - Arch Linux: `yay -S hunspell-pt-br`

5. Execute o programa:

    ```sh
    python main.py
    ```

## Tests

Para executar os testes, use:

```sh
python -m pytest -v