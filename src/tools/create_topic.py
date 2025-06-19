from common.config import BOOTSTRAP_SERVERS
from common.server import mcp
from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import KafkaError, TopicAlreadyExistsError


@mcp.tool()
def create_topic(name: str, partitions: int = 1) -> str:
    """Create a new Kafka topic with the given name and number of partitions."""
    try:
        admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)
        topic = NewTopic(name=name, num_partitions=partitions, replication_factor=1)
        admin.create_topics([topic])
        return f"Topic '{name}' created with {partitions} partition(s)"
    except TopicAlreadyExistsError:
        return f"Topic '{name}' already exists"
    except KafkaError as e:
        return f"Error creating topic: {str(e)}"
