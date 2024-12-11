# Flask API Example

Este repositório contém um exemplo básico de uma aplicação web construída com o framework Flask, utilizando a biblioteca `requests` para consumir dados de uma API externa e retorná-los em formato JSON para o cliente.

## 📜 Sobre o Flask

- **Ano de lançamento:** 2010
- **Desenvolvedor:** Pocoo Team
- **Linguagem de programação:** Python

### 🏗️ Quando é recomendado utilizar o Flask?

- Ideal para desenvolvimento de aplicativos web Python, desde projetos simples até aplicações mais complexas.
- Excelente escolha para criar APIs RESTful, sites estáticos e prototipagem rápida de projetos.

### 🔑 Principais características

- **Microframework:** Flask é leve e flexível, permitindo que os desenvolvedores escolham as bibliotecas e ferramentas necessárias.
- **Extensibilidade:** Possui um ecossistema rico de extensões, como autenticação de usuários e integração com bancos de dados.
- **Fácil de aprender:** Tem uma curva de aprendizado suave e é ideal para iniciantes no desenvolvimento web.

## 🛠️ Estrutura do Código

A aplicação realiza os seguintes passos:
1. Inicializa o servidor Flask.
2. Define uma rota na URL raiz (`/`).
3. Faz uma requisição HTTP GET a uma API externa.
4. Retorna os dados da API externa em formato JSON ou uma mensagem de erro caso a requisição falhe.

### 📄 Código Principal

```python
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Failed to fetch data from API'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

## 🚀 Como executar

1. **Clone o repositório**:
   ```bash
   git clone <URL-do-repositório>
   cd <nome-da-pasta>
   ```
2. **Instale as dependências**:
   Certifique-se de que o Python 3 está instalado em sua máquina.
   ```bash
   pip install flask requests
   ```
3. **Execute a aplicação**:
   ```bash
   python <nome-do-arquivo>.py
   ```
4. **Acesse no navegador**:
   Abra `http://127.0.0.1:5000/` no navegador para ver os dados retornados.

## 📚 Recursos adicionais

- **Vídeo:** [Introdução ao Flask](https://www.youtube.com/watch?v=e9EPb5AoMf8)
- **Site oficial:** [Flask Documentation](https://flask.palletsprojects.com/)

---

Sinta-se à vontade para usar este exemplo como base para seus projetos Flask! 😊
