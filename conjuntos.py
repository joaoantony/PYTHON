'''
EX1 - Calcular a densidade de um material com base em sua massa e 
volume. Fórmula: densidade = massa / volume

1) Obter as medidas (massa e volume)
2) Calcular a densidade com base na fórmula acima
restrições:
    - massa < 0 or volume < 0 I volume != 0 
3) Executar análise da densidade 
    - função responsável por executar as funções dos itens 1) e 2)
    - tratamento de execuções 

'''

def obter_massa():
    massa = float(input('Massa do material (em kg): '))
    return massa

def obter_volume():
    volume = float(input('Volume do material: (em m³): '))
    return volume

def calcular_densidade(massa:float, volume:float) -> float: 
    #validação 
    if massa < 0 or volume < 0:
        raise ValueError("[ValueError]: Massa e Volume não podem ser NEGATIVOS!")

    if volume == 0:
        raise ZeroDivisionError("[ZeroDivisionError]: O volume não pode ser ZERO!")

    densidade = massa / volume
    return densidade

def executar_analise_densidade() -> None:

    try:
        massa = obter_massa()
        volume = obter_volume()

        densidade = calcular_densidade(massa, volume)
    except ValueError as erro:
        print(f'[ERRO de ENTRADA]: {erro}')
        print('Divisão por zero impede o cálculo da densidade')
    except ZeroDivisionError as erro:
        print(f'[ERRO FÍSICO]: {erro}')
        print('Divisão por zero impede o cálculo da densidade')

    else:
        print(f'\n[SUCESSO]: Densidade do material: {densidade:.2f} em kg/m³')
    finally:
        print('----Encerrando o ensaio----')

    #principal 
    while True:
        executar_analise_densidade()
        print('\n')