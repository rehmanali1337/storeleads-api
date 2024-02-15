class StoreLeadsAPIError(Exception):
    """Base exception from Store Leads API"""


class NotFound(StoreLeadsAPIError):
    """Something not found from the API"""
