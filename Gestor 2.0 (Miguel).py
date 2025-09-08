#Importa o deque (Funciona como um dicionario muito mais eficiente do que o "List" e diminui linhas de codigo.)
from collections import deque

Pessoas_Normais = deque ()
Pessoas_com_prioridade = deque ()

#Variaveis do relatorio (Cria as variaveis com quantidade zerada pra ser adicionada no dicionario.)
Total_de_pessoas = 0
Total_normal = 0
Total_prioridade = 0

#Regra da prioridade (se gestante ou pcd for maior que 60 anos então é "bool" (verdadeiro).) 
def Prioridade (idade: int, gestante: bool, pcd: bool ) -> bool:
    return idade >= 60 or gestante or pcd

 #Adição do cliente (Global serve para criar uma função que vai usar e alterar as filas que estão fora dela.)
def cliente():
    global Pessoas_com_prioridade, Pessoas_Normais 

#try serve para testar um bloco de código que pode dar erro. (front-end)
    try:
        print("|(GESTOR DE PRIORIDADE)")
        nome = input("\n|Digite seu nome: ")
        idade = int(input("|Digite sua idade: "))
        gestante = input("|Gestante? (Sim/Não): ").strip().lower() == "s"
        pcd = input("|Você tem algum tipo de deficiência? (Sim/Não): ").strip().lower() == "s"

        #cliente (funciona como um dicionário, um local com coisas nomeadas.) (back-end)
        cliente = {"nome": nome, "idade": idade, "gestante": gestante, "pcd": pcd}

        if  Prioridade(idade, gestante, pcd ):
            Pessoas_com_prioridade.append(cliente)
            print (f"< Cliente {nome} Você foi adicionado a prioridade, aguarde ser chamado.")        
        
        else:
            Pessoas_Normais.append(cliente)
            print (f"< Cliente {nome} Você foi adicionado a fila normal, aguarde ser chamado.")
    
    except ValueError: #ValueError toda vez que houver um digito errado na idade ele vai mostrar que voce errou. (front-end)
        print("|Erro, Voce não digitou um número.")
        

        #Lista de filas (back-end)
def atender_cliente():
    global Total_de_pessoas, Total_prioridade, Total_normal #adiciona total de pessoas, prioridade e pessoas "Normais" (função "global")
            
    if Pessoas_com_prioridade:
        cliente = Pessoas_com_prioridade.popleft()
        Total_de_pessoas +=1
        Total_prioridade +=1
    elif Pessoas_Normais:
        cliente = Pessoas_Normais.popleft()
        Total_de_pessoas +=1
        Total_normal +=1
    else: 
        print("|Nenhuma pessoa na fila.")
        return
        
        #Mostra o total de atendidos no dicionário (front-end)
    print(f"> Atendidos: {cliente['nome']} (Idade: {cliente['idade']})")

        #Lista de filas) Pessoas com prioridade vao para uma lista temporaria ("c") e quando-
        #elas forem terminadas de ser atendidas ou elas vão ser adicionadas a prioridade ou-
        #se não, elas vão para fila normal (front-end)
def listar_filas():
        print("\n |Fila de prioridade:")
        if Pessoas_com_prioridade:
            for c in Pessoas_com_prioridade:
                print(f"- {c['nome']} ({c['idade']} anos)") #Nunca esquecer de que quando colocar-
        else: print(" [Vazia]")                             #colocar f" quando for citar uma paalvra dentro de um (, { ou [ não usar " e sim '

        print ("\n |Fila Normal")
        if Pessoas_Normais:
            for c in Pessoas_Normais:
                print(f"- {c['nome']} ({c['idade']} anos)")
        else: print(" [Vazia]")

        #Conclusão final) Tabela de todas as pessoas que foram atendidas (front-end)
def Conclusão_final():
    print("\n|CONCLUSÃO FINAL:")
    print(f"|Total de atendidos: {Total_de_pessoas}")
    print(f"|Total de prioridades: {Total_prioridade}")
    print(f"|Fila de prioridade atual: {len(Pessoas_com_prioridade)}") #"len" conta quantos itens existem em uma coleção de um comando. 
    print(f"|Fila de pessoas normais: {len(Pessoas_Normais)}")
    if Total_de_pessoas > 0:
        percentual = (Total_prioridade / Total_de_pessoas) *100
        print (f"% de prioritários atendidos: {percentual:.2f}% ")
        percentual = (Total_normal / Total_de_pessoas) *100
        print (f"% de Normais atendidos: {percentual:.2f}% ")

        #Interface de Úsuario (front_end)
def menu():
    while True:
        print("|[FILA DE ATENDIMENTO]:")
        print("|1. Cadastrar cliente)")
        print("|2. Atender próximo cliente)")
        print("|3. Lista de pendentes)")
        print("|4. Conclusão final)")
        print("|5. Fechar Programa)")

    #Funções da interface (back-end)
        opcao = input("|[ESCOLHA UMA DAS OPÇÕES]:").strip()
        if opcao == "1":
            cliente()
        elif opcao == "2":
            atender_cliente()
        elif opcao == "3":
            listar_filas()
        elif opcao == "4":
            Conclusão_final()
        elif opcao == "5":
            print("|Fechando Programa...")
            break
        else: 
            print("|Esta opção não está disponível.")

if __name__ == "__main__":
    menu()