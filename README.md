
# Estrutura Projeto de Dados

Este repositório contém um projeto que demonstra como estruturar um pipeline de dados. Inclui etapas de **extração**, **transformação** e **carregamento** (ETL), além de documentação gerada automaticamente usando o MkDocs com o tema Material.

## Documentação
Acesse a documentação do projeto gerada pelo MkDocs: [Documentação do Projeto](https://loliveirads.github.io/estrutura_projeto_dados/)


## Tecnologias Utilizadas

- **Python** 3.11.3
- **Pandas** para manipulação de dados
- **MkDocs** para documentação
- **Poetry** para gerenciamento de dependências
- **pytest** para testes unitários



### Instalação e Configuração

1. Clone o repositório:

```bash
git clone https://github.com/loliveirads/estrutura_projeto_dados.git
cd estrutura_projeto_dados
```

2. Configure a versão correta do Python com `pyenv`:

```bash
pyenv install 3.11.5
pyenv local 3.11.3
```

3. Configurar poetry para Python version 3.11.3 e ative o ambiente virtual:

```bash
poetry env use 3.11.3
poetry shell
```

4. Instale as dependencias do projeto:

```bash
poetry install
```

5. Execute os testes para garantir que tudo está funcionando como esperado:

```bash
task test
```

6. Execute o comando para ver a documentação do projeto:

```bash
task doc
```

7. Execute o comando de execucão da pipeline para realizar a ETL:

```bash
task run
```

8. Verifique na pasta data/output se o arquivo foi gerado corretamente.

## Contato

Para dúvidas, sugestões ou feedbacks:

* **Luiz Fernando** - [luizfsoliveira.lm@gmail.com](mailto:luizfsoliveira.lm@gmail.com)

