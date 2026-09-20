# 🚰 Classificador de Consumo de Água

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com)
[![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-%C3%81gua%20&%20Meio%20Ambiente-0077B6?style=for-the-badge&logo=eco&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-brightgreen?style=for-the-badge)](#)

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido para a **campanha de conscientização ambiental** da companhia de saneamento local. O objetivo do script é analisar o perfil de consumo mensal de água ($m^3$) dos imóveis e emitir alertas educativos aos moradores para incentivar o uso consciente dos recursos hídricos e a identificação de vazamentos.

---

## ⚙️ Regras de Negócio e Classificação

O sistema classifica o consumo de acordo com o tipo de imóvel e o volume consumido:

* 🏢 **Comercial**: Recebe a orientação para consulta do plano corporativo.
* 🏢 **Apartamento ($< 10\text{ m}^3$)**: Classificado como **Consumo econômico**.
* 🏠 **Apartamento ($\ge 10\text{ m}^3$)** ou **Casa ($\le 25\text{ m}^3$)**: Classificado como **Consumo moderado**.
* ⚠️ **Demais casos** (Consumo residencial acima dos limites): Alerta de **Consumo excessivo** com recomendação de checagem de vazamentos.

---

## 🛠️ Tecnologias Utilizadas

* 🐍 **Python 3.x** - Linguagem principal do script.
* 💻 **Git & GitHub** - Controle de versão e hospedagem do código.

---

## 🚀 Como Executar o Programa

### Pré-requisitos

Certifique-se de ter o [Python 3](https://www.python.org/downloads/) instalado em sua máquina.

### Passo a Passo

1. **Clone o repositório** (ou baixe os arquivos):
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Navegue até a pasta do projeto**:
   ```bash
   cd seu-repositorio
   ```

3. **Execute o script**:
   ```bash
   python app.py
   ```

---

## 📝 Exemplo de Uso

```text
Informe o tipo de imóvel ("comercial", "casa" ou "apartamento"): apartamento
Informe o consumo mensal de água em m³: 8.5
Consumo econômico – excelente controle de água!
Obrigado por contribuir para a preservação dos recursos hídricos!
```

---

🌱 *Pequenas atitudes geram grandes economias. Preserve nossos recursos hídricos!*
