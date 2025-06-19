from kafka import KafkaProducer
from kafka.errors import KafkaError
import json
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp


@mcp.tool()
def publish_message(topic: str, message: str) -> str:
    """Publish a message to a Kafka topic."""
    try:
        producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        producer.send(topic, {"message": message})
        producer.flush()
        return f"Message published to {topic}"
    except KafkaError as e:
        return f"Error publishing message: {str(e)}"
