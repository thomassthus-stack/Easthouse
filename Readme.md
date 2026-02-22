# 🚀 Nova Analytics Engine

Dette er Python-backenden for en avansert AI-drevet SaaS. Den fungerer som en "Code Interpreter" som kjører i skyen via Google Cloud Run.

## 🛠 Tech Stack
- **Framework:** FastAPI (Python)
- **Deployment:** Google Cloud Run (Dockerized)
- **Data Science:** Pandas, NumPy, Scikit-learn, SciPy
- **Visualisering:** Plotly

## 🧩 Slik fungerer det
1. **Input:** Brukeren sender naturlig språk via en frontend (bygget i Lovable).
2. **LLM:** En AI-modell genererer Python-kode basert på dataens struktur.
3. **Execution:** Denne backenden mottar koden, kjører den i et isolert miljø, og returnerer interaktive Plotly-grafer og statistikk.

## 🚀 Installasjon (Lokal utvikling)
1. Klon repoet: `git clone <ditt-repo-url>`
2. Opprett venv: `python -m venv venv`
3. Aktiver: `source venv/bin/activate` (eller `venv\Scripts\activate` på Windows)
4. Installer: `pip install -r requirements.txt`
5. Kjør server: `uvicorn main:app --reload`

## 🌍 Deployment
Hver "push" til `main`-branchen trigger en automatisk build i Google Cloud Run.
