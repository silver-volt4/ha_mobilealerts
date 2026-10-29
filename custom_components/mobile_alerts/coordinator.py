"""Data update coordinator for the MobileAlerts integration."""
from __future__ import annotations

import logging

from homeassistant.const import Platform
from mobilealerts import Gateway, Sensor, SensorHandler

from .base import MobileAlertesBaseCoordinator
from .binary_sensor import create_binary_sensor_entities
from .sensor import create_sensor_entities

_LOGGER = logging.getLogger(__name__)


class MobileAlertesDataCoordinator(MobileAlertesBaseCoordinator, SensorHandler):
    """Class to manage MobileAlerts data."""

    @property
    def gateway(self) -> Gateway:
        return self._gateway
    
    async def sensor_added(self, sensor: Sensor) -> None:
        _LOGGER.debug("sensor_added %r", sensor)

        binary_add_entities = self._add_entities_callbacks.get(Platform.BINARY_SENSOR)
        if binary_add_entities is not None:
            binary_entities = create_binary_sensor_entities(self, sensor)
            binary_add_entities(binary_entities, True)
            self.add_entities(binary_entities)

        sensor_add_entities = self._add_entities_callbacks.get(Platform.SENSOR)
        if sensor_add_entities is not None:
            sensor_entities = create_sensor_entities(self, sensor)
            sensor_add_entities(sensor_entities, True)
            self.add_entities(sensor_entities)

        self.hass.config_entries.async_update_entry(self._entry)

    async def sensor_updated(self, sensor: Sensor) -> None:
        _LOGGER.debug("sensor_updated %r", sensor)
        self.async_set_updated_data({})
