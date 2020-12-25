import graphene
from .facility import FacilityQuery
from .inventory_item import InventoryItemQuery
from .product import ProductQuery
from .product_group import ProductGroupQuery
from .stash_location import StashLocationQuery
from .stash_setting import StashSettingQuery
from .transaction import TransactionQuery
from .user_custom import UserQuery


class Query(
        FacilityQuery,
        InventoryItemQuery,
        ProductQuery,
        ProductGroupQuery,
        StashLocationQuery,
        StashSettingQuery,
        TransactionQuery,
        UserQuery,
        graphene.ObjectType,
):
    version = graphene.String(default_value="v0.1.0")


schema = graphene.Schema(query=Query)
