# pocPythonBehave
Teste automatizado usando python com behave

# Configurações para rodar o projeto

- Faça a instalação do Python;
- Instale o pip;
- Instale o virtualenv;
- Pelo terminal acesse a pasta raiz do teu projeto;
- Crie um virtualenv com os comandos a seguir:
    - virtualenv nomeQueDesejar
- Entre no teu virtualenv com o comando:
    - Windows: nomeDoVirtualEnv/Scripts/activate
    - Linux: source nomeDoVirtualEnv/bin/activate
- Instale as dependências do projeto:
    - pip install -r requeriments.txt

# Para executar o teste execute no terminal:
- Para executar todos os testes:
    - behave
- Para executar um teste específico(identificado pela tag na feature)
    - behave --tags="@cenario_teste_02" features/pocPythonBehave.feature 
