import sys
from graphql_client import GraphQLClient

subscription_create_query = '''
    subscription {
        organizationCreated { count }
    }
    '''


def create_callback(_id, data):
    print(__name__)
    return default_callback(data)


def default_callback(data):
    print(data)


if __name__ == "__main__":
    with GraphQLClient("ws://localhost:9000/graphql") as client:
        sub_id = client.subscribe(subscription_create_query, callback=create_callback)
