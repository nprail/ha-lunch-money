"""
Home Assistant custom integration for Lunch Money.
"""
from .const import DOMAIN
from .api import LunchMoneyAPI

async def async_setup_entry(hass, entry):
    """Set up Lunch Money from a config entry."""
    api_key = entry.data["api_key"]
    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = {"api": LunchMoneyAPI(api_key)}
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass, entry):
    return True
