#language: pt

Funcionalidade: Poc

    Eu como usuário,
    Quero acessar a página Automação com Batista 
    Para fazer um exemplo


    Cenário: Validar a url de uma nova janela
        Dado que tenha acessado a página Automação com Batista
        Quando acessar mudança de foco para acessar uma nova janela
        Então deve exibir uma nova janela com link especificado
