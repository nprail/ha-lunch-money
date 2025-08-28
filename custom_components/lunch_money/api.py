"""
Lunch Money API client for Home Assistant integration.
"""
import aiohttp

class LunchMoneyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://dev.lunchmoney.app/v1"

    async def async_get_balances(self):
        """Fetch and group balances from both assets and Plaid accounts."""
        url = f"{self.base_url}/assets"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        grouped = {}
        async with aiohttp.ClientSession() as session:
            # Fetch assets
            async with session.get(url, headers=headers) as resp:
                resp.raise_for_status()
                data = await resp.json()
                for asset in data.get("assets", []):
                    if asset.get("closed_on"):
                        continue
                    type_name = asset.get("type_name", "Other")
                    balance = asset.get("to_base", 0)
                    try:
                        balance = float(balance)
                    except Exception:
                        balance = 0
                    grouped[type_name] = grouped.get(type_name, 0) + balance
            # Fetch Plaid accounts
            plaid_url = f"{self.base_url}/plaid_accounts"
            async with session.get(plaid_url, headers=headers) as resp:
                resp.raise_for_status()
                plaid_data = await resp.json()
                for account in plaid_data.get("plaid_accounts", []):
                    # Only ignore accounts with status 'inactive', include all others
                    if account.get("status") == "inactive":
                        continue
                    type_name = account.get("type", "Other")
                    balance = account.get("to_base", 0)
                    try:
                        balance = float(balance)
                    except Exception:
                        balance = 0
                    grouped[type_name] = grouped.get(type_name, 0) + balance
        return grouped
