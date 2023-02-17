import graphene 

import links.schema

class Query(links.schema.Query, graphen.ObjectType):
    pass 

schema = graphene.Schema(query=query)
