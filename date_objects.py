from datetime import date

# Pegando a data atual
data_atual = str(date.today())
dia_atual = str(data_atual[8:])
mes_atual = str(data_atual[5:7])
ano_atual = str(data_atual[:4])

# Ano não bissexto
ano_completo = [31,
       28,
       31,
       30,
       31,
       30,
       31,
       31,
       30,
       31,
       30,
       31]