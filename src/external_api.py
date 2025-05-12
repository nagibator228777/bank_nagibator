import os

import requests
from dotenv import load_dotenv

load_dotenv()


def calculate_transaction_amount(transaction):
    """
    Вычисляет сумму транзакции в рублях.

    Args:
        transaction (dict): Словарь, представляющий транзакцию.
                           Обязательные ключи: 'operationAmount' (dict),
                           'operationAmount' содержит 'amount' (str) и 'currency' (dict),
                           'currency' содержит 'code' (str).

    Returns:
        float: Сумма транзакции в рублях.
               Возвращает None в случае ошибки.
    """
    try:
        operation_amount = transaction["operationAmount"]
        amount_str = operation_amount["amount"]
        currency_code = operation_amount["currency"]["code"]

        if not isinstance(amount_str, str) or not isinstance(currency_code, str):
            print("Ошибка: Некорректные данные транзакции")
            return None

        try:
            amount = float(amount_str)
        except ValueError:
            print("Ошибка: Некорректный формат суммы транзакции")
            return None

        if currency_code == "RUB":
            return amount

        api_key = os.getenv("API_KEY")

        if currency_code not in ("USD", "EUR"):
            print(f"Ошибка: Неподдерживаемая валюта: {currency_code}")
            return None

        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        response = requests.get(url, headers={"apikey": api_key})
        response.raise_for_status()
        data = response.json()

        if "result" not in data:
            print("Ошибка: Не удалось получить результат конвертации")
            return None

        return float(data["result"])

    except (KeyError, TypeError) as e:
        print(f"Ошибка: Некорректная структура данных транзакции: {e}")
        return None
