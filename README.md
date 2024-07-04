# Eventos Históricos

 - Este projeto é uma aplicação web que permite aos usuários consultar eventos históricos que ocorreram em uma data específica. A aplicação utiliza a API do [History API](http://history.muffinlabs.com/) para obter os eventos e a biblioteca `translate` para traduzir as descrições dos eventos para o português.
 - O Projeto está em produção e pode ser acessado através do endereço: https://eventoshistoricos.streamlit.app/
## Funcionalidades

- Consulta de eventos históricos por dia e mês.
- Tradução das descrições dos eventos para o português.
- Exibição dos eventos com ano, descrição traduzida e link para mais informações.

## Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/) - Framework para criação de aplicações web interativas.
- [Requests](https://docs.python-requests.org/en/latest/) - Biblioteca para fazer requisições HTTP.
- [Translate](https://pypi.org/project/translate/) - Biblioteca para tradução de texto.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/thiagoregueira/eventos_historicos_com_Python.git
    cd eventos_historicos_com_Python
    ```

2. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute a aplicação:
    ```bash
    streamlit run evt_historicos.py
    ```

2. Acesse a aplicação no navegador através do endereço:
    ```
    http://localhost:8501
    ```

3. Insira o dia e o mês desejados e clique em "Buscar Eventos" para ver os eventos históricos.

## Estrutura do Projeto

```plaintext
eventos_historicos/
│
├── evt_historicos.py       # Arquivo principal da aplicação
├── requirements.txt        # Lista de dependências do projeto
├── README.md               # Documentação do projeto
└── .gitignore              # Arquivo para ignorar arquivos desnecessários no Git
