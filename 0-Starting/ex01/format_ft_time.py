from datetime import datetime

# Data inicial "Era Unix" (Unix Epoch)
data_inicial = datetime(1970, 1, 1)

# Data atual
data_atual = datetime.now()

# Diferença entre as duas datas
diferenca = data_atual - data_inicial

# Total de segundos desde a Era Unix
total_segundos = diferenca.total_seconds()

print(
    f"Seconds since January 1, 1970: {total_segundos:,.3f} "
    f"or {total_segundos:.2e} in scientific notation.")
