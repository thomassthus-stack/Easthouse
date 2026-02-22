from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import plotly.express as px

app = FastAPI(title="Nova Engine")

class AnalysisRequest(BaseModel):
    code: str
    data_dict: dict | None = None

@app.get("/health")
def health():
    return {"status": "ok", "message": "Nova Engine Online"}

@app.post("/analyze")
async def analyze(request: AnalysisRequest):
    try:
        df = pd.DataFrame(request.data_dict) if request.data_dict else None
        local_scope = {"pd": pd, "np": np, "px": px, "df": df}

        exec(request.code, {}, local_scope)

        fig = local_scope.get("fig")
        text = local_scope.get("text")
        tables = local_scope.get("tables")

        return {
            "chart_json": fig.to_json() if fig is not None else None,
            "text": text,
            "tables": tables,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

