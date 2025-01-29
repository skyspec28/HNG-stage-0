from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime, timezone

app = FastAPI(title="HNG Stage One API")

#  CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
async def get_info():
    current_time = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    return {
        "email": "maulomepelumi@gmail.com",
        "current_datetime": current_time,
        "github_url": "https://github.com/yourusername/your-repo"
    }

