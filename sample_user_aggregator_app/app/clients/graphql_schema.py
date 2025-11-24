# app/graphql_schema.py
import strawberry
from typing import Optional
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class UserProfile:
    id: str
    email: str
    name: str
    bio: Optional[str]
    avatar_url: Optional[str]
    # intentionally NOT including phone number to reflect original design

# A simple dependency-like holder that will be set by main.
_AGGREGATOR = None

@strawberry.type
class Query:
    @strawberry.field
    def user_profile(self, id: str, token: Optional[str] = None) -> Optional[UserProfile]:
        """
        GraphQL resolver that queries the UserAggregatorService.
        Original design: missing phone number field.
        """
        agg = _AGGREGATOR.get_user_aggregate(id, auth_token=token)
        if not agg:
            return None
        return UserProfile(
            id=str(agg.get("id")),
            email=agg.get("email"),
            name=agg.get("name"),
            bio=agg.get("bio"),
            avatar_url=agg.get("avatar_url"),
        )

def set_aggregator(aggregator):
    global _AGGREGATOR
    _AGGREGATOR = aggregator

schema = strawberry.Schema(query=Query)
graphql_router = GraphQLRouter(schema)
