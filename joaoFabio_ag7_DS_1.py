# Campanha de conscientização ambiental — classificação de consumo de água

# Campanha de conscientização ambiental — classificação de consumo de água

# .strip().lower() garante que diferenças de maiúsculas/minúsculas e espaços não quebrem o programa

tipo = input('Informe o tipo de imóvel ("comercial", "casa" ou "apartamento"): ').strip().lower()
consumo = float(input("Informe o consumo mensal de água em m³: "))

if tipo == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")

elif tipo == "apartamento" and consumo < 10:
    print("Consumo econômico – excelente controle de água!")

elif tipo == "apartamento" or (tipo == "casa" and consumo <= 25):
    print("Consumo moderado – dentro do padrão residencial.")

else:
    print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

print("Obrigado por contribuir para a preservação dos recursos hídricos!")


