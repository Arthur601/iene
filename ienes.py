def converter_moeda(valor, moeda_origem, moeda_destino, taxas):
    """
    Converte o valor de uma moeda para outra usando taxas de câmbio.

    :param valor: float, valor a ser convertido
    :param moeda_origem: str, código da moeda de origem (ex: 'BRL')
    :param moeda_destino: str, código da moeda de destino (ex: 'USD')
    :param taxas: dict, dicionário com taxas de câmbio em relação ao Real (BRL)
    :return: float, valor convertido
    """
    if moeda_origem == moeda_destino:
        return valor

    # Converte o valor para BRL se necessário
    if moeda_origem != 'BRL':
        valor_em_brl = valor / taxas[moeda_origem]
    else:
        valor_em_brl = valor

    # Converte o valor em BRL para a moeda destino
    valor_convertido = valor_em_brl * taxas[moeda_destino]

    return valor_convertido


# Taxas de câmbio baseadas em BRL (exemplo)
taxas_cambio = {
    'BRL': 1.0,     # Real brasileiro
    'USD': 0.20,    # Dólar americano
    'EUR': 0.18,    # Euro
    'JPY': 27.5     # Iene japonês
}

# Exemplo de uso:
valor = float(input("Digite o valor a converter: "))
moeda_origem = input("Digite a moeda de origem (BRL, USD, EUR, JPY): ").upper()
moeda_destino = input("Digite a moeda de destino (BRL, USD, EUR, JPY): ").upper()

if moeda_origem not in taxas_cambio or moeda_destino not in taxas_cambio:
    print("Moeda inválida!")
else:
    resultado = converter_moeda(valor, moeda_origem, moeda_destino, taxas_cambio)
    print(f"{valor:.2f} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}.")
