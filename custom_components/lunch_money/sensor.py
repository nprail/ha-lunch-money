"""
Sensor platform for Lunch Money integration.
"""
import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CURRENCY_DOLLAR
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up Lunch Money sensors."""
    # Placeholder: In a full integration, use config entry setup
    pass

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Lunch Money sensors from a config entry."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]
    balances = await api.async_get_balances()
    sensors = []
    for type_name, value in balances.items():
        sensors.append(
            LunchMoneyBalanceSensor(type_name, value)
        )
    async_add_entities(sensors, True)

from datetime import timedelta

class LunchMoneyBalanceSensor(SensorEntity):
    _attr_scan_interval = timedelta(hours=1)

    def __init__(self, type_name, value):
        self._attr_name = f"Lunch Money {type_name}"
        self._attr_native_value = value
        self._attr_unique_id = f"lunch_money_{type_name.lower().replace(' ', '_')}"
        self._attr_native_unit_of_measurement = CURRENCY_DOLLAR

    async def async_update(self):
        # In a full implementation, update from API
        pass
