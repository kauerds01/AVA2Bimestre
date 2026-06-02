#Victor Hugo Cardoso: Lógica Matemática
def calcular_imc(p, a):
    imc = p / (a ** 2)
    return imc
#Davi da Silva Marculino: Parte 3--
def gerar_aviso(status):
    if status == "NORMAL":
        return("Parabéns! Continue mantendo hábitos saudáveis.")
    elif status == "ACIMA DO PESO":
        return("Procure praticar atividades físicas e manter uma alimentação equilibrada.")
    else:
        return("Status Inválido.")