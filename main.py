import hashlib
import requests

from fastapi import FastAPI, HTTPException

app = FastAPI()

SIGN_API_URL = "http://localhost:9333/sign"


@app.get("/echo")
def echo(message: str):
    # Compute SHA-256 hash of the message
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()

    # Call the /sign API
    try:
        response = requests.post(SIGN_API_URL, json={"hash": sha256_hash})
        response_data = response.json()
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error calling /sign API: {str(e)}")

    # Return the response from /sign API with the original message
    return {"message": message, **response_data}
