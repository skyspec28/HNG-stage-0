# HNG Stage 0 API

A FastAPI-based API that returns your email, current UTC datetime, and GitHub repository URL. This is part of the HNG Internship Stage One task.

## API Documentation

### Endpoint
- **GET /** - Retrieves personal information.

### Response (200 OK)
```json
{
    "email": "your.email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```

### Example Usage
**cURL**:
```bash
curl hng-stage-0-production-a7c1.up.railway.app
```

**Python**:
```python
import requests
response = requests.get('https://your-deployed-url/')
print(response.json())
```

## Local Development

1. Clone the repo:
   ```bash
   git clone https://github.com/skyspec28/HNG-stage-0.git
   cd main
   ```

2. Install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate #mac
   
   .venv \Scripts\activate  #windows 
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

The API will be available at `http://localhost:8000`

## Deployment

The API is deployed at:
```
hng-stage-0-production-a7c1.up.railway.app
```
