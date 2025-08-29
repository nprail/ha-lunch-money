# Lunch Money Home Assistant Integration

This custom integration exposes your Lunch Money asset types (e.g., Cash, Credit, etc.) as Home Assistant sensor entities.

## Installation

### HACS (Recommended)

1. Go to **HACS > Integrations** in your Home Assistant UI.
2. Click the three dots in the top right and select **Custom repositories**.
3. Add this repository's URL and select **Integration** as the category.
4. Search for "Lunch Money" in HACS and install the integration.
5. Restart Home Assistant.
6. Go to **Settings > Devices & Services > Add Integration** and search for "Lunch Money".
7. Enter your Lunch Money API key when prompted.

### Manual

1. Copy the `lunch_money` folder into your Home Assistant `custom_components` directory:
   - Example: `/config/custom_components/lunch_money`
2. Restart Home Assistant.
3. In Home Assistant UI, go to **Settings > Devices & Services > Add Integration** and search for "Lunch Money".
4. Enter your Lunch Money API key when prompted.
