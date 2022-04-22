from os import system
from time import sleep
from MaxHeap import MaxHeap
from Paciente import Paciente

class Menu:
    def entradaDeDados():
        titulo = "Fila de espera".center(50)
        enfeites = "="*50
        linhaVazia = "\n"

        while(True):
            print(linhaVazia)
            print(enfeites)
            print(titulo)
            print(enfeites, linhaVazia)
            print("[1] Adicionar novo paciente")
            print("[2] Chamar próximo paciente")
            print("[3] Mostrar próximo paciente")
            print("[4] Listar últimos 5 pacientes chamados")
            print("[5] Encerrar Programa")

            opcao = int(input("\nDigite a opção selecionada: "))
            if opcao == 1:
                Menu.criarNovoPaciente()
            elif opcao == 2:
                Menu.chamarProximoPaciente()
            elif opcao == 3:
                Menu.mostrarProximoPaciente()
            elif opcao == 4:
                Menu.mostrarUltimos5Pacientes()
            elif opcao == 5:
                Menu.fecharHospital()
            else:
                print("Opção escolhida inválida")

    def criarNovoPaciente():
        global ordem_atendimento

        nome_completo = str(input("\nNome do paciente: "))
        tipo_sanguineo = str(input("Tipo sanguíneo: "))
        data_nascimento = str(input("Data de Nascimento (dd/mm/aaaa): "))
        paciente = Paciente(nome_completo, tipo_sanguineo, data_nascimento)

        prioridade_atendimento = 0
        prioridade_atendimento = int(input("\nPrioridade do paciente [1 a 10]: "))

        item = (prioridade_atendimento, ordem_atendimento, Paciente.__repr__(paciente))
        fila_espera.put(item)
        ordem_atendimento += 1
        
    def chamarProximoPaciente():
        if(fila_espera.peek()):
            pacientes_chamados.append(fila_espera.peek())
            print(fila_espera.get())
            sleep(2)
        else:
            print("Não há mais pacientes para serem atendidos")
            sleep(2)

    def mostrarProximoPaciente():
        if(fila_espera.peek()):
            print(fila_espera.peek())
            sleep(2)
        else:
            print("Não há mais pacientes para serem atendidos")
            sleep(2)

    def mostrarUltimos5Pacientes():
        if(len(pacientes_chamados) <= 4):
            for i in range(len(pacientes_chamados)):
                print(pacientes_chamados[i])
        elif(len(pacientes_chamados > 5)):
            for i in range(1, 6):
                print(pacientes_chamados[len(pacientes_chamados) - i])

    def fecharHospital():
        print("O hospital está fechado!")
        exit()

fila_espera = MaxHeap()
ordem_atendimento = 0
pacientes_chamados = list()

system("cls")

Menu.entradaDeDados()