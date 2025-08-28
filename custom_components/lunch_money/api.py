"""
Lunch Money API client for Home Assistant integration.
"""
import aiohttp

class LunchMoneyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://dev.lunchmoney.app/v1"

    async def async_get_balances(self):
        url = f"{self.base_url}/assets"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                resp.raise_for_status()
                data = await resp.json()
                # Group assets by type_name and sum their balances
                grouped = {}
                for asset in data.get("assets", []):
                    type_name = asset.get("type_name", "Other")
                    balance = asset.get("balance", 0)
                    try:
                        balance = float(balance)
                    except Exception:
                        balance = 0
                    grouped[type_name] = grouped.get(type_name, 0) + balance
                return grouped
