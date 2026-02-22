from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import plotly.express as px
import io

app = FastAPI()

class AnalysisRequest(BaseModel):
    code: str
    data_dict: dict = None

@app.get("/")
def read_root():
    return {"status": "Nova Engine Online"}

@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    try:
        # Lag et miljø for koden der df er tilgjengelig
        df = pd.DataFrame(request.data_dict) if request.data_dict else None
        
        # Lokale variabler som AI-koden kan bruke
        local_scope = {"pd": pd, "np": np, "px": px, "df": df}
        
        # KJØR KODEN (exec er kraftig, men må sikres senere)
        exec(request.code, {}, local_scope)
        
        # Finn resultater (f.eks. fig for grafer)
        result_fig = local_scope.get('fig')
        
        return {
            "chart_json": result_fig.to_json() if result_fig else None,
            "message": "Success"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
