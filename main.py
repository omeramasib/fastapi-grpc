# main.py
from fastapi import FastAPI
from threading import Thread
from server.greeter_server import serve

app = FastAPI()

# Launch the gRPC server in a separate thread
def start_grpc_server():
    serve()

# Start the gRPC server on app startup
@app.on_event("startup")
def startup_event():
    Thread(target=start_grpc_server, daemon=True).start()

# FastAPI endpoint for health check (optional)
@app.get("/health")
async def health_check():
    return {"status": "FastAPI and gRPC are running"}