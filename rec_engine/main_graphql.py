import strawberry
import uvicorn

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from graphql_api.core import Query, Mutation, Subscription

schema = strawberry.Schema(query=Query, mutation=Mutation, subscription=Subscription)
graphql_router = GraphQLRouter(schema,
                               subscription_protocols=[GRAPHQL_WS_PROTOCOL, GRAPHQL_TRANSPORT_WS_PROTOCOL])
app = FastAPI()
app.include_router(graphql_router, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run("main_graphql:app", host="0.0.0.0", port=9000, reload=True, log_level="info")
