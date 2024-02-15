from typing import Any, List, TypeAlias

GeneralDict: TypeAlias = dict[str, Any]


class Plan:
    def __init__(self, data: GeneralDict):
        self.name: str = data.get("name", "")
        self.monthly_cost: str = data.get("monthly_cost", "")
        self.monthly_cost_cents: int = data.get("monthly_cost_cents", 0)


class App:
    def __init__(self, data: GeneralDict):
        self.average_rating: str = data.get("average_rating", "")
        self.app_store_url: str = data.get("app_store_url", "")
        self.state: str = data.get("state", "")
        self.description: str = data.get("description", "")
        self.icon_url: str = data.get("icon_url", "")
        self.name: str = data.get("name", "")
        self.token: str = data.get("token", "")
        self.platform: str = data.get("platform", "")
        self.vendor_name: str = data.get("vendor_name", "")
        self.vendor_url: str = data.get("vendor_url", "")
        self.vendor_email: str = data.get("vendor_email", "")
        self.vendor_website: str = data.get("vendor_website", "")
        self.id: str = data.get("id", "")
        self.created_at: str = data.get("created_at", "")
        self.plans: List[Plan] = [
            Plan(plan_data) for plan_data in data.get("plans", [])
        ]
        self.categories: List[str] = data.get("categories", [])
        self.review_count: int = data.get("review_count", 0)


class AppList:
    def __init__(self, data: GeneralDict):
        self.apps: List[App] = [App(app_data) for app_data in data.get("apps", [])]


# Example usage:
json_data = {
    "apps": [
        {
            "average_rating": "5.0",
            "app_store_url": "https://apps.shopify.com/flashyapp-marketing-automation",
            "state": "Active",
            "description": "All-In-One Marketing Automation Platform for eCommerce",
            "icon_url": "https://cdn.shopify.com/app-store/listing_images/372dbfce35571e26aba38e41b47c5a0c/icon/CJXqis70lu8CEAE=.png?height=84&width=84",
            "name": "Flashy ‑ Marketing Automation",
            "token": "flashyapp-marketing-automation",
            "platform": "shopify",
            "vendor_name": "Flashy",
            "vendor_url": "https://apps.shopify.com/partners/developer-8c7c2ff225c2d971",
            "vendor_email": "hello@flashyapp.com",
            "vendor_website": "https://flashyapp.com",
            "id": "1.flashyapp-marketing-automation",
            "created_at": "2019-02-27T00:00:00",
            "plans": [
                {
                    "name": "Starter",
                    "monthly_cost": "$7/month",
                    "monthly_cost_cents": 700,
                },
                {
                    "name": "Professional",
                    "monthly_cost": "$40/month",
                    "monthly_cost_cents": 4000,
                },
                {
                    "name": "Master",
                    "monthly_cost": "$99/month",
                    "monthly_cost_cents": 9900,
                },
                {
                    "name": "Enterprise",
                    "monthly_cost": "$199/month",
                    "monthly_cost_cents": 19900,
                },
            ],
            "categories": ["store design", "marketing", "conversion"],
            "review_count": 11,
        },
        {
            "average_rating": "5.0",
            "app_store_url": "https://apps.shopify.com/google-seo-monitor-1",
            "state": "Active",
            "free_trial_duration": "168h0m0s",
            "description": "Google SEO optimizer - see keyword/page trends & opportunities",
            "icon_url": "https://cdn.shopify.com/app-store/listing_images/d549c0dcb6ea916754cb9256fe92ad5e/icon/CNDXtdn0lu8CEAE=.png?height=84&width=84",
            "name": "SEO Rank & Traffic Optimizer",
            "token": "google-seo-monitor-1",
            "platform": "shopify",
            "vendor_name": "Invenire Analytics",
            "vendor_url": "https://apps.shopify.com/partners/invenire",
            "vendor_email": "support@invenire.com.au",
            "id": "1.google-seo-monitor-1",
            "created_at": "2020-05-01T00:00:00",
            "plans": [
                {
                    "name": "Basic Plan",
                    "monthly_cost": "$29/month",
                    "monthly_cost_cents": 2900,
                }
            ],
            "categories": ["marketing"],
            "review_count": 6,
        },
    ]
}
if __name__ == "__main__":

    for app in json_data["apps"]:
        a = App(app)
        print(a.app_store_url)
