#Victor Hugo Cardoso: Lógica Matemática
def calcular_imc(p, a):
    imc = p / (a ** 2)
    return imc
#Tiago Caetao Santos Silva Parte 2--
def classificador(valor_imc):
    if valor_imc < 25 
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
