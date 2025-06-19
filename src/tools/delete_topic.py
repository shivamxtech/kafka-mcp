from common.config import BOOTSTRAP_SERVERS
from common.server import mcp
from kafka.admin import KafkaAdminClient
from kafka.errors import KafkaError


@mcp.tool()
def delete_topic(name: str) -> str:
    """Delete the Kafka topic with the given name."""
    try:
        admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
        admin.delete_topics([name])
        return f"Topic '{name}' deleted"
    except KafkaError as e:
        return f"Error deleting topic: {str(e)}"