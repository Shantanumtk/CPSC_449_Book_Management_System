# Main entry point for running the FastAPI application
if __name__ == "__main__":
    uvicorn.run(
        "main:app",          # Specify the FastAPI app location
        host="0.0.0.0",      # Bind to all available network interfaces
        port=5000,           # Set the port to 5000
        reload=True          # Enable live-reload for development
    )

