from common.config import BOOTSTRAP_SERVERS
from common.server import mcp
from kafka.errors import KafkaError
from kafka import KafkaConsumer
from typing import Dict


@mcp.tool()
def describe_topic(name: str) -> Dict:
    """Describe details of a Kafka topic."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        metadata = consumer.partitions_for_topic(name)
        if metadata is None:
            return {"error": f"Topic '{name}' does not exist"}
        return {
            "topic": name,
            "partitions": list(metadata),
        }
    except KafkaError as e:
        return {"error": str(e)}
