"""
Módulo de Previsão de Vendas com TensorFlow
Autor: Engenheiro de Machine Learning / Desenvolvedor Python
Descrição: Script modular para carga de dados em dicionário, conversão para DataFrame,
           análise exploratória básica e treinamento de um modelo preditivo com TensorFlow.
"""

import logging
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers, models

# Configuração de logging para rastreabilidade profissional
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def carregar_dados_dicionario() -> dict:
  """Carrega o dataset bruto em formato de dicionário Python."""
  logger.info("Carregando dados a partir do dicionário em memória...")
  dados_brutos = {
      "data": [
          "2025-01-01",
          "2025-01-08",
          "2025-01-15",
          "2025-01-22",
          "2025-01-29",
          "2025-02-05",
          "2025-02-12",
          "2025-02-19",
          "2025-02-26",
          "2025-03-05",
          "2025-03-12",
          "2025-03-19",
          "2025-03-26",
          "2025-04-02",
          "2025-04-09",
          "2025-04-16",
          "2025-04-23",
          "2025-04-30",
          "2025-05-07",
          "2025-05-14",
      ],
      "vendas": [
          1200.5,
          1350.0,
          1280.0,
          1420.5,
          1500.0,
          1480.0,
          1600.2,
          1550.0,
          1700.0,
          1650.0,
          1750.5,
          1800.0,
          1720.0,
          1900.0,
          1850.5,
          1950.0,
          2000.0,
          2100.2,
          2050.0,
          2150.0,
      ],
      "promocao_ativa": [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
  }
  return dados_brutos


def preparar_dataframe(dados_brutos: dict) -> pd.DataFrame:
  """Converte o dicionário em DataFrame, trata tipos e engenharia básica de features."""
  try:
    logger.info("Convertendo dicionário para Pandas DataFrame...")
    df = pd.DataFrame(dados_brutos)

    # Conversão de datas e extração de componentes temporais
    df["data"] = pd.to_datetime(df["data"])
    df["mes"] = df["data"].dt.month
    df["dia_semana"] = df["data"].dt.dayofweek
    df["tendencia_tempo"] = np.arange(len(df))  # Índice temporal sequencial

    # Tratamento básico de nulos/erros
    df.fillna(0, inplace=True)
    return df
  except Exception as e:
    logger.error(f"Erro ao preparar o DataFrame: {e}")
    raise


def analise_exploratoria(df: pd.DataFrame) -> None:
  """Executa e exibe estatísticas descritivas básicas do dataset."""
  print("\n" + "=" * 50)
  print(" ANÁLISE EXPLORATÓRIA DE VENDAS ")
  print("=" * 50)
  print(f"Total de registros: {len(df)}")
  print(f"Média de vendas: {df['vendas'].mean():.2f}")
  print(f"Desvio padrão das vendas: {df['vendas'].std():.2f}")
  print(f"Menor venda registrada: {df['vendas'].min():.2f}")
  print(f"Maior venda registrada: {df['vendas'].max():.2f}")
  print("-" * 50 + "\n")


def construir_modelo(input_shape: int) -> tf.keras.Model:
  """Constrói a arquitetura da rede neural densa usando TensorFlow/Keras."""
  model = models.Sequential([
      layers.Input(shape=(input_shape,)),
      layers.Dense(64, activation="relu"),
      layers.Dense(32, activation="relu"),
      layers.Dense(1),  # Camada de saída para regressão (previsão contínua)
  ])

  model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])
  return model


def main():
  """Função principal que orquestra o pipeline de dados e machine learning."""
  # 1. Carga de Dados
  dados = carregar_dados_dicionario()

  # 2. Transformação em DataFrame e Pré-processamento
  df = preparar_dataframe(dados)

  # 3. Análise Básica
  analise_exploratoria(df)

  # 4. Preparação de Features (X) e Target (y)
  features = ["promocao_ativa", "mes", "dia_semana", "tendencia_tempo"]
  X = df[features].values
  y = df["vendas"].values

  # Normalização simples (MinMax) para estabilizar o treinamento do TensorFlow
  X_min, X_max = X.min(axis=0), X.max(axis=0)
  # Evita divisão por zero se houver colunas constantes
  X_range = np.where(X_max - X_min == 0, 1, X_max - X_min)
  X_scaled = (X - X_min) / X_range

  # 5. Construção e Treinamento do Modelo
  logger.info("Iniciando treinamento do modelo TensorFlow...")
  model = construir_modelo(input_shape=X.shape[1])

  # Treinamento por 100 épocas para demonstração
  model.fit(X_scaled, y, epochs=100, batch_size=4, verbose=0)
  logger.info("Treinamento concluído com sucesso.")

  # 6. Simulação de Previsão para o Próximo Período
  # Exemplo: Próximo período (índice 20), mês 5, dia de semana 2, com promoção ativa (1)
  novo_dado = np.array([[1, 5, 2, len(df)]])
  novo_dado_scaled = (novo_dado - X_min) / X_range

  previsao = model.predict(novo_dado_scaled)

  print("\n" + "=" * 50)
  print(" RESULTADO DA PREVISÃO DE VENDAS ")
  print("=" * 50)
  print(f"Previsão de vendas para o próximo período: R$ {previsao[0][0]:.2f}")
  print("=" * 50 + "\n")


if __name__ == "__main__":
  main()