#Victor Hugo Cardoso: Lógica Matemática
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
#Tiago Caetao Santos Silva Parte 2--
def classificador(valor_imc):
    if valor_imc < 25: 
        return "Peso na media"
    else:
        return "Acima da media"
#Davi da Silva Marculino: Parte 3--
def gerar_aviso(status):
    if status == "NORMAL":
        return("Parabéns! Continue mantendo hábitos saudáveis.")
    elif status == "ACIMA DO PESO":
        return("Procure praticar atividades físicas e manter uma alimentação equilibrada.")
    else:
        return("Status Inválido.")
#Kauê Rodrigues da Silva: Parte 4-- Integração
print("Bem vindo ao seu avaliador de saúde pessoal 😁")
print("Aqui iremos avaliar seu estado físico 💪🏻")
peso = float(input("Qual é seu peso atual?"))
altura = float(input("Qual é sua altura atual em cm?"))
imc_final = calcular_imc(peso, altura)
status_final = classificador(valor_imc)
aviso_final = gerar_aviso(status)