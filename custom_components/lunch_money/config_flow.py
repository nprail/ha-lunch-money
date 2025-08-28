"""
Config flow for Lunch Money integration.
"""
from homeassistant import config_entries
from .const import DOMAIN
import voluptuous as vol

class LunchMoneyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            # Validate API key (could add real validation)
            return self.async_create_entry(title="Lunch Money", data=user_input)
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("api_key"): str
            }),
            errors=errors
        )
