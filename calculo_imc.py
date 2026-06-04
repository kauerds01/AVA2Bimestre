#Victor Hugo Cardoso: Lógica Matemática
def calcular_imc(p, a):
    imc = p / (a * 2)
    return imc
#Tiago Caetao Santos Silva Parte 2--
def classificador(valor_imc):
    if valor_imc <= 25: 
        return "NORMAL"
    else:
        return "ACIMA DO PESO"
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
peso = float(input("Qual é seu peso atual?: "))
altura = float(input("Qual é sua altura atual em metros?: "))
imc_final = calcular_imc(peso, altura)
status_final = classificador(imc_final)
aviso_final = gerar_aviso(status_final)
print(f"Seu imc é: {imc_final:.2f}")
print(f"Sua situação atual é: {status_final}")
print(f"feedback para você: {aviso_final}")