from fastapi import FastAPI, Request, HTTPException
from confluent_kafka import Producer
import json

app = FastAPI()

# Basic Kafka configuration (no auth)
KAFKA_BROKER = "10.88.233.206:9092" 
TOPIC_NAME = "test-message-topics"            

# Create Kafka producer
producer = Producer({'bootstrap.servers': KAFKA_BROKER})

@app.post("/api/sendData/")
async def send_data(request: Request):
    try:
        data = await request.json()
        message = json.dumps(data)

        # Send message to Kafka
        producer.produce(TOPIC_NAME, value=message)
        producer.flush()

        return {"status": "success", "message": "Data sent to Kafka successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Start the server (Python 3.6 compatible)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

