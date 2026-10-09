# Detector Visual de Pessoas e Objetos com OpenCV 👁️

Aplicação web desenvolvida em Python e Streamlit para simulação de Visão Computacional baseada em regras e classificadores Haar Cascade.

## 🚀 Funcionalidades
- **Detecção de Pessoas/Rostos:** Utiliza o algoritmo Haar Cascade para localizar rostos e olhos em tempo real.
- **Segmentação por Contornos:** Identifica objetos e formas proeminentes na imagem sem necessidade de redes neurais pesadas.
- **Baixo Consumo de Recursos:** Projetado para rodar em servidores com limite rígido de memória (< 100 MB RAM).

## 🛠️ Tecnologias
- Python 3.10+
- Streamlit
- OpenCV (Headless)
- NumPy
- Pillow

## ⚙️ Configuração para Deploy no Render
- **Environment:** Python 3
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
