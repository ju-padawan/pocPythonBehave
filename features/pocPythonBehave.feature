#language: pt

Funcionalidade: Poc

    Eu como usuário,
    Quero acessar a página Automação com Batista 
    Para fazer um exemplo

    
    @cenario_teste_01
    Cenário: Validar a url de uma nova janela
        Dado que tenha acessado a página Automação com Batista
        Quando acessar mudança de foco para acessar uma nova janela
        Então deve exibir uma nova janela com link especificado

    
    @cenario_teste_02
    Cenário: Validar a consulta da lista de usuários cadastrados
        Dado que tenha acessado a página Automação com Batista
        Quando acessar a lista de usuários cadastrados
        Então deve exibir a lista de usuários
