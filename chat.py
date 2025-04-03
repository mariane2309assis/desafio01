def time_to_minutes(hora):
    h, m = map(int, hora.split(':'))
    return h * 60 + m

# Função para converter minutos em formato de hora
def minutes_to_time(minutos):
    horas = minutos // 60
    minutos = minutos % 60
    return f"{horas:02}:{minutos:02}"

# Horários de entrada
entrada01 = "03:45"
entrada02 = "14:20"

# Convertendo os horários para minutos
minutos_entrada01 = time_to_minutes(entrada01)
minutos_entrada02 = time_to_minutes(entrada02)

# Somando as duas entradas (tempo total em minutos)
total_minutos = minutos_entrada01 + minutos_entrada02

# Convertendo de volta para o formato de hora
saida = minutes_to_time(total_minutos)

print(f"A saída calculada é: {saida}")
