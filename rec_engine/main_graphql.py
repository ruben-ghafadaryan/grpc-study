import strawberry
import uvicorn

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

from graphql_api.core import Query, Mutation

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")


if __name__ == "__main__":
    uvicorn.run("main_graphql:app", host="0.0.0.0", port=9000, reload=True, log_level="info")
