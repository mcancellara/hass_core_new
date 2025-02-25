"""Test ESPHome binary sensors."""


from homeassistant.components.esphome import DomainData
from homeassistant.core import HomeAssistant


async def test_call_active(
    hass: HomeAssistant,
    mock_voice_assistant_v1_entry,
) -> None:
    """Test call active binary sensor."""

    entry_data = DomainData.get(hass).get_entry_data(mock_voice_assistant_v1_entry)

    state = hass.states.get("binary_sensor.test_call_active")
    assert state is not None
    assert state.state == "off"

    entry_data.async_set_assist_pipeline_state(True)

    state = hass.states.get("binary_sensor.test_call_active")
    assert state.state == "on"

    entry_data.async_set_assist_pipeline_state(False)

    state = hass.states.get("binary_sensor.test_call_active")
    assert state.state == "off"
