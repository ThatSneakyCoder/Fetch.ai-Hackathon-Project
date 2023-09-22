import requests
import json
from plyer import notification
from uagents import Agent, Context
from gui_interface import create_gui

currency_checker = Agent(name="currency_checker", seed="currency recovery phrase")


@currency_checker.on_interval(period=60.0)
async def fetch_currency_rate(ctx: Context):

    for i in range(0, len(base_currency), 1):

        base_currency_var = base_currency[i].upper()
        target_currency_var = target_currency[i].upper()
        end = float(max_values_float[i])
        print(end)
        start = float(min_values_float[i])
        print(start)

        api_url = f"https://theforexapi.com/api/latest?base={base_currency_var}&symbols={target_currency_var}%20HTTP/2"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = json.loads(response.text)
            exchange_rate = float(data['rates'][target_currency_var])
            print(f"Current exchange rate is {exchange_rate}")

            if exchange_rate < start or end < exchange_rate:
                print("If condition entered")
                notification.notify(
                    title=f'Currency Update: {base_currency_var} to {target_currency_var}',
                    message=f"Exchange rate of 1 {base_currency_var} is {exchange_rate} {target_currency_var}",
                    app_name='CurrencyChecker',
                    timeout=2
                )
        else:
            print("Failed to fetch data")


def start_agent():
    currency_checker.run()


if __name__ == "__main__":
    base_currency, target_currency, max_values_float, min_values_float = create_gui()
    start_agent()
