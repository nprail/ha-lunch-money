# Lunch Money Home Assistant Integration

This custom integration exposes your Lunch Money asset types (e.g., Cash, Credit, etc.) as Home Assistant sensor entities.

## Installation

1. Copy the `lunch_money` folder into your Home Assistant `custom_components` directory:
   - Example: `/config/custom_components/lunch_money`
2. Install dependencies:
   - Add to your Home Assistant `requirements.txt` (if using a custom venv):
     ```
     aiohttp
     voluptuous
     ```
   - Or install via pip:
     ```sh
     pip install aiohttp voluptuous
     ```
3. Restart Home Assistant.
4. In Home Assistant UI, go to **Settings > Devices & Services > Add Integration** and search for "Lunch Money".
5. Enter your Lunch Money API key when prompted.

## Testing

1. After setup, go to **Developer Tools > States** in Home Assistant.
2. Search for entities starting with `sensor.lunch_money_`.
3. Each asset type from your Lunch Money account will appear as a sensor entity (e.g., `sensor.lunch_money_cash`, `sensor.lunch_money_credit`).
4. Confirm that the values match your Lunch Money dashboard.

## Troubleshooting
- Check Home Assistant logs for errors related to `lunch_money`.
- Ensure your API key is correct and has access to the `/assets` endpoint.

## Reference
- [Lunch Money API Docs](https://lunchmoney.dev/)
