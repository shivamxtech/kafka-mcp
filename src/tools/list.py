from common.config import BOOTSTRAP_SERVERS
from common.server import mcp
from kafka.errors import KafkaError
from kafka import KafkaConsumer, KafkaAdminClient
from typing import List


@mcp.tool()
def list_topics() -> List[str]:
    """List all topics in the Kafka cluster."""
    try:
        consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS)
        return list(consumer.topics())
    except KafkaError as e:
        return [f"Error listing topics: {str(e)}"]


@mcp.tool()
def get_consumer_groups() -> List[str]:
    """List all Kafka consumer groups."""
    try:
        admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
        return [group[0] for group in admin.list_consumer_groups()]
    except KafkaError as e:
        return [f"Error: {str(e)}"]