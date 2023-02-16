def resumo():
    mensagem = "John Von Neumann foi um matemático húngaro que utilizou pela primeira vez a linguagem binária para que as instruções, lidas na época por cartões perfurados, fossem gravadas na memória do computador;."
    return mensagem


def doutorado():
    mensagem = "Em 1926, Von Neumann conseguiu o doutorado em matemática pela universidade de Budapeste."
    return mensagem


def contribuicoes():
    mensagem = "Contribuiu com o hardware fazendo que as instruções fossem gravadas no ocmputador, que segue sendo o formato do processador atual até hoje. "
    return mensagem


def artigos():
    mensagem = "Alguns artigos publicados foram: Theory of self-reproducing automata, On the introduction of transfinite numbers,  A spectral theory for general operators of a unitary space\nmpact of Atomic Energy on the Physical and Chemical Sciences"
    return mensagem


def citacoes():
    mensagem = "Em matemática não percebemos coisas. Apenas nos habituamos a elas.\nExiste um conjunto infinito A que não é demasiado grande.\nPodia parecer que chegamos ao limite do que era possível alcançar com a tecnologia dos computadores, contudo, uma pessoa deveria ser cuidadosa com tais afirmações, pois tendem a soar muito tontas em 5 anos. (dito em 1949)"
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nBoa noite! Você está aprendendo sobre Allan Turing.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Doutorado
3 - Contribuições
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Doutorado")
        mensagem = doutorado()

    elif opcao == 3:
        print("3 - Contribuições")
        mensagem = contribuicoes()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
