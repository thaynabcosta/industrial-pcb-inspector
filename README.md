# 🔍 Inspeção Automatizada de PCBs com Visão Computacional

Este projeto simula um sistema de inspeção em linha de produção utilizando **Python** e **OpenCV**. O objetivo é identificar a presença e o correto posicionamento de componentes em placas de circuito impresso (PCBs).

## 🚀 Funcionalidades
* **Detecção de Componentes:** Utiliza técnica de *Template Matching* para localizar peças específicas.
* **Validação de Qualidade:** Compara o nível de confiança da detecção para aprovar ou reprovar o produto.
* **Simulação de Falhas:** Capaz de distinguir entre componentes corretos e peças com defeitos ou ausentes.

## 🛠️ Tecnologias
* [Python 3.x](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [NumPy](https://numpy.org/)

## 🔧 Como Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-projeto.git](https://github.com/seu-usuario/nome-do-projeto.git)

2. **Instale as dependências**
    ```bash
    pip install -r requirements.txt

3. **Cenário 1: Testando Produto Conforme (OK)**  
    * No arquivo configuracao.py, certifique-se de que a variável IMAGEM_PRINCIPAL aponta para a imagem correta:
    ```python
    IMAGEM_PRINCIPAL = 'imagens/produto_na_esteira.png'  
    ```
    * Execute: 
    ```bash
    python inspecao.py
    ```
    * Resultado esperado: Retângulo verde sobre o componente e mensagem de aprovação.

4. **Cenário 2: Testando Produto Não Conforme (NG)**
    * Altere no arquivo configuracao.py o caminho para a imagem com defeito que você gerou:
    ```python
    IMAGEM_PRINCIPAL = 'imagens/componente_ng.png'
    ```
    * Execute: 
    ```bash
    python inspecao.py
    ```
    * Resultado esperado: O sistema não desenhará o retângulo e exibirá a mensagem de reprovação no console.