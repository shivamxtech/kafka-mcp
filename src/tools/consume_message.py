from kafka import KafkaConsumer
from kafka.errors import KafkaError
from typing import List
import json
from common.config import BOOTSTRAP_SERVERS
from common.server import mcp


@mcp.tool()
def consume_messages(topic: str, limit: int = 1) -> List[str]:
    """Consume a limited number of messages from a Kafka topic."""
    try:
        consumer = KafkaConsumer(topic,
                                 bootstrap_servers=BOOTSTRAP_SERVERS,
                                 consumer_timeout_ms=5000,
                                 auto_offset_reset='earliest')

        messages = []
        for i, msg in enumerate(consumer):
            messages.append(msg.value.decode("utf-8"))
            if i + 1 >= limit:
                break
        return messages
    except KafkaError as e:
        return [f"Error consuming messages: {str(e)}"]
