"""
Sensor platform for Lunch Money integration.
"""
import logging
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CURRENCY_DOLLAR
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, CoordinatorEntity
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    # Not used with config entries
    return

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up Lunch Money sensors from a config entry using DataUpdateCoordinator."""
    api = hass.data[DOMAIN][entry.entry_id]["api"]

    async def async_update_data():
        return await api.async_get_balances()

    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="Lunch Money Balances",
        update_method=async_update_data,
        update_interval=timedelta(hours=1),
    )

    await coordinator.async_config_entry_first_refresh()

    sensors = [
        LunchMoneyBalanceSensor(coordinator, type_name)
        for type_name in coordinator.data.keys()
    ]
    async_add_entities(sensors, True)

class LunchMoneyBalanceSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, type_name):
        super().__init__(coordinator)
        self.type_name = type_name
        self._attr_name = f"Lunch Money {type_name}"
        self._attr_unique_id = f"lunch_money_{type_name.lower().replace(' ', '_')}"
        self._attr_native_unit_of_measurement = CURRENCY_DOLLAR

    @property
    def native_value(self):
        return self.coordinator.data.get(self.type_name)
