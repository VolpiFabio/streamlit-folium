# 🌎 Mapa Interativo

Projeto construído com Streamlit + Folium para visualização interativa de marcadores, camadas WMS e mapas base. O app está estruturado em módulos para facilitar organização e manutenção.

## 🚀 Funcionalidades

- 📍 Visualização interativa em 2D usando Folium
- 🗺️ Seleção de mapas base via barra lateral
- 🧩 Camadas WMS dinâmicas a partir do Geoserver
- 🏢 Marcadores categorizados (Centro, Comércio, Residencial)
- 📂 Organização modular com pastas para cada funcionalidade (`camadas`, `marcadores`, `plugins`, etc)
- 🔐 URL do Geoserver protegida usando variável de ambiente no `.env`

---

## 🧱 Estrutura de pastas

```bash
project/
│
├── main.py                # Arquivo principal do Streamlit
├── .env                   # Variáveis sensíveis (não versionado)
│
├── marcadores/
│   ├── marcadores.py
│   └── __init__.py
│
├── camadas/
│   ├── camadas.py
│   └── __init__.py
│
├── mapa_base/
│   ├── mapa_base.py
│   └── __init__.py
│
├── sidebar/
│   ├── sidebar.py
│   └── __init__.py
│
├── plugins/
│   ├── plugins.py
│   └── __init__.py
│
├── config/
│   ├── url.py             # Leitura da URL via .env
│   └── __init__.py
