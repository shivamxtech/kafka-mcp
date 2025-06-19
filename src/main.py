import sys

from common.config import MCP_TRANSPORT, BOOTSTRAP_SERVERS
from common.server import mcp
from tools.list import list_topics
from tools.describe_topic import describe_topic


class KafkaMCPServer:
    def __init__(self):
        print("Starting the KafkaMCPServer", file=sys.stderr)
        print('...', file=sys.stderr)

    def run(self):
        mcp.run(transport=MCP_TRANSPORT)
        print('...', file=sys.stderr)


def main():
    server = KafkaMCPServer()
    server.run()
    print('...', file=sys.stderr)


if __name__ == "__main__":
    main()
