# 🚀 MDM Data Quality API

Plataforma de **Qualidade de Dados Cadastrais com IA**, focada em **Master Data Management (MDM)**, com funcionalidades de:

*  Detecção de Anomalias (Machine Learning)
*  Deduplicação de Dados (Entity Resolution)
*  Pipeline de dados (ETL)
*  API REST com FastAPI

---


## Solução

Esta API utiliza técnicas de **Machine Learning** e **Data Engineering** para:

* Identificar **anomalias em dados cadastrais**
* Detectar **duplicidades com fuzzy matching**
* Criar uma base confiável para decisões de negócio

---

##  Arquitetura

```
src/
│
├── api/
│   └── main.py              # API FastAPI
│
├── ml/
│   └── anomaly_detection.py # Modelo de ML (Isolation Forest)
│
├── quality/
│   └── deduplication.py     # Deduplicação com RapidFuzz
│
├── etl/
│   └── build_master_table.py # Pipeline de dados
│
data/
├── raw/
├── processed/
```

---

## ⚙️ Tecnologias

* Python
* FastAPI
* Pandas
* Scikit-learn
* RapidFuzz
* Uvicorn

---

##  Funcionalidades

###  1. Detecção de Anomalias

Utiliza **Isolation Forest** para identificar padrões incomuns nos dados.

**Endpoint:**

```
GET /anomalias
```

**Retorno:**

* Total de anomalias
* Exemplos de registros suspeitos

---

###  2. Deduplicação de Dados

Implementa:

* Normalização de texto
* Fuzzy matching (RapidFuzz)
* Blocking por cidade (otimização)

**Endpoint:**

```
GET /deduplicacao
```

---

### 🧪 3. Documentação interativa

Swagger disponível em:

```
http://127.0.0.1:8000/docs
```

---

## Como executar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/mdm-data-quality-ai.git
cd mdm-data-quality-ai
```

---

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Rodar API

```bash
uvicorn src.api.main:app --reload
```

---

## Diferenciais técnicos

* ✔️ Pipeline de dados (ETL)
* ✔️ ML aplicado em dados reais
* ✔️ Deduplicação com técnicas de MDM
* ✔️ API pronta para produção
* ✔️ Arquitetura modular

---


##  Autor

Juliane Bezerra Ferreira
Desenvolvedora Full Stack & Machine Learning

---

## Sobre o projeto

Este projeto foi desenvolvido com foco em aplicações reais de **Machine Learning em dados cadastrais**, simulando cenários de **Master Data Management (MDM)** utilizados em empresas.

##  Dataset

Este projeto utiliza dados públicos do Olist (e-commerce brasileiro).

Para reproduzir:

1. Baixe o dataset do Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

2. Coloque os arquivos em:

data/raw/

3. Execute o pipeline ETL:

python src/etl/build_master_table.py



