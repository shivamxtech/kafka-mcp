# Kafka MCP

## Overview

The Kafka MCP Server offers efficient way to convert prompts into actions into Kafka ecosystem. It is a natural 
language interface designed for agentic applications to efficiently manage Kafka operations and integrate seamlessly 
with MCP Clients enabling AI driven workflows to interact with processes in Kafka. Using this MCP Server, you can ask
questions like:

1. Publish message 'i am using kafka server' on the topic 'test-kafka'
2. Consume the message from topic 'test-kafka'
3. List all topics from the kafka environment

## Features

- Natural Language Queries: Enables AI agents to query and update Redis using natural language.
- Seamless MCP Integration: Works with any MCP client for smooth communication.
- Full Kafka Support: Handles producer, consumer, topics, broker, partitions and offsets.
- Scalable & Lightweight: Designed for high-performance data operations.


## Tools

This MCP Server offers various tools for Kafka:

`consumer` and `producer` tools allow to consumer and publish message on topics

`topic` tools allow to `list`, `create`, `delete` and `describe` topics in Kafka.

`broker` allows to get broker info.

`partition` tools allow to get partitions and partition offsets.

`group_offset` tools allow to get and reset offsets in Kafka.

## Configurations

set the following in `.env` file or export manually

```text
BOOTSTRAP_SERVERS=your_kafka_server
MCP_TRANSPORT=stdio
```

## Local Development

Create a virtual environment
```shell
# Using venv (built-in)
python3 -m venv .venv

# Activate the virtual environment
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```


Install Dependencies
```shell
# Using pip
pip install -r requirements.txt

# Or using uv (faster)
uv pip install -r requirements.txt
```

Set Configurations in terminal/env

```text
BOOTSTRAP_SERVERS=<your_kafka_url>
MCP_TRANSPORT=stdio
```

Run the application
```shell
python3 src/main.py

# OR

uv run python3 src/main.py
```

To interact with server,

Add the following configuration to your MCPO server's config.json file (e.g., in Claude Desktop):

```json
{
  "mcpServers": {
    "kafka-mcp": {
      "command": "python3",
      "args": ["/Users/I528600/Desktop/mcp/kafka-mcp/src/main.py"],
      "env": {
        "BOOTSTRAP_SERVERS": "localhost:9092",
        "MCP_TRANSPORT": "stdio"
      }
    }
  }
}
```

## Example prompts

- List all topics in the kafka cluster
- Create topic 'my-kafka' in kafka cluster
- Publish a message 'hello from mcp' to the topic 'my-kafka' in cluster
- Consume 2 messages from the topic 'my-kafka' in kafka cluster
- Describe the topic 'my-kafka'