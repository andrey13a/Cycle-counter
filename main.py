from PyQt5 import uic, QtWidgets
from date_objects import *

application = QtWidgets.QApplication([])


def calcular_ciclo():

    nome = str(initial_window.text_name.toPlainText())


    # Pegando data de nascimento
    dia_nasc = str(initial_window.spin_day.value())
    mes_nasc = str(initial_window.spin_month.value())
    ano_nasc = str(initial_window.spin_year.value())

    # Variaveis de calculo
    dias_ano_nasc = 0
    dias_ano_atual = 0
    anos_vida = 0
    dias_totais = 0

    # Quantidade de dias vividos até o final do primeiro ano de vida
    # Soma do mês de nascimento até o fim do ano, Subtraindo o dia de nascimento
    for valor in ano_completo[int(mes_nasc) - 1:]:
        dias_ano_nasc += valor
    dias_ano_nasc -= int(dia_nasc)

    # Soma do ano seguinte ao nascimento, até o ano anterior ao atual.
    for valor in range(int(ano_nasc) + 1, int(ano_atual)):
        dias_totais += 365
        anos_vida += 1
        if valor % 4 == 0 and valor % 100 != 0:
            dias_totais += 1

    # Quantidade de dias vividos no ano atual
    for valor in ano_completo[0:int(mes_atual) - 1]:
        dias_ano_atual += valor
    dias_ano_atual += int(dia_atual)
    dias_totais += dias_ano_nasc
    dias_totais += dias_ano_atual

    texto = f'''Olá {nome},
Você tem {anos_vida} anos e {dias_ano_atual + dias_ano_nasc} dias.

Você já viveu:
{dias_totais} Dias.
{dias_totais * 24} Horas.
{(dias_totais * 24) * 60} Minutos.
{((dias_totais * 24) * 60) * 60} Segundos.
{(((dias_totais * 24) * 60) * 60) * 1000} Mílisegundos.
'''

    initial_window.text_result.setText(texto)

initial_window = uic.loadUi('initial_window.ui')
initial_window.ok_button.clicked.connect(calcular_ciclo)
initial_window.show()

application.exec()
