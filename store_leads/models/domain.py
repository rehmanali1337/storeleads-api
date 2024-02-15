from typing import List, Union
from ..types import GeneralDict


class ContactInfo:
    def __init__(self, data: GeneralDict):
        self.source: str = data.get("source", "")
        self.type: str = data.get("type", "")
        self.value: Union[str, int] = data.get("value", "")
        self.description: str = data.get("description", "")
        self.followers: int = data.get("followers", 0)
        self.followers_90d: int = data.get("followers_90d", 0)
        self.posts: int = data.get("posts", 0)


class Technology:
    def __init__(self, data: GeneralDict):
        self.installed_at: str = data.get("installed_at", "")
        self.name: str = data.get("name", "")
        self.description: str = data.get("description", "")
        self.vendor_url: str = data.get("vendor_url", "")
        self.icon_url: str = data.get("icon_url", "")
        self.installs: int = data.get("installs", 0)


class DomainInfo:
    def __init__(self, data: GeneralDict):
        self.cluster_best_ranked: str = data.get("cluster_best_ranked", "")
        self.city: str = data.get("city", "")
        self.last_updated_at: str = data.get("last_updated_at", "")
        self.subregion: str = data.get("subregion", "")
        self.contact_page: str = data.get("contact_page", "")
        self.country_code: str = data.get("country_code", "")
        self.title: str = data.get("title", "")
        self.administrative_area_level_1: str = data.get(
            "administrative_area_level_1", ""
        )
        self.state: str = data.get("state", "")
        self.icon: str = data.get("icon", "")
        self.brands_page: str = data.get("brands_page", "")
        self.region: str = data.get("region", "")
        self.language_code: str = data.get("language_code", "")
        self.about_us: str = data.get("about_us", "")
        self.tracking_page: str = data.get("tracking_page", "")
        self.last_platform_change_at: str = data.get("last_platform_change_at", "")
        self.platform: str = data.get("platform", "")
        self.location: str = data.get("location", "")
        self.og_image: str = data.get("og_image", "")
        self.merchant_name: str = data.get("merchant_name", "")
        self.last_platform: str = data.get("last_platform", "")
        self.keywords: str = data.get("keywords", "")
        self.created_at: str = data.get("created_at", "")
        self.name: str = data.get("name", "")
        self.description: str = data.get("description", "")
        self.contact_info: List[ContactInfo] = [
            ContactInfo(info) for info in data.get("contact_info", [])
        ]
        self.aliases: List[str] = data.get("aliases", [])
        self.categories: List[str] = data.get("categories", [])
        self.technologies: List[Technology] = [
            Technology(tech) for tech in data.get("technologies", [])
        ]
        self.cluster_domains: List[str] = data.get("cluster_domains", [])
        self.features: List[str] = data.get("features", [])
        self.shipping_carriers: List[str] = data.get("shipping_carriers", [])
        self.rank_percentile: float = data.get("rank_percentile", 0.0)
        self.rank: int = data.get("rank", 0)
        self.latitude: float = data.get("latitude", 0.0)
        self.platform_rank_percentile: float = data.get("platform_rank_percentile", 0.0)
        self.longitude: float = data.get("longitude", 0.0)
        self.employee_count: int = data.get("employee_count", 0)
        self.cc_rank: int = data.get("cc_rank", 0)
        self.cc_centrality: int = data.get("cc_centrality", 0)
        self.product_count: int = data.get("product_count", 0)
        self.platform_rank: int = data.get("platform_rank", 0)
        self.estimated_page_views = data.get("estimated_page_views", 0)
        self.estimated_sales = data.get("estimated_sales", 0)
