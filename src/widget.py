"""Модуль для обработки банковских операций."""
from datetime import datetime

from .masks import get_mask_account, get_mask_card_number

# ... (остальной код без изменений)
# ... (остальной код без изменений)


def mask_account_card(account_info: str) -> str:

    """
    Маскирует номер карты/счета в строке.

    Args:
        account_info: Строка формата "Visa Platinum 1234567890123456"
                     или "Счет 12345678901234567890"

    Returns:
        Замаскированная строка
    """
    if "Счет" in account_info:
        parts = account_info.split()
        return f"{' '.join(parts[:-1])} {get_mask_account(parts[-1])}"
    else:
        parts = account_info.split()
        return f"{' '.join(parts[:-1])} {get_mask_card_number(parts[-1])}"


def get_date(date_str: str) -> str:
    """
    Форматирует дату из ISO-формата в 'ДД.ММ.ГГГГ'.

    Args:
        date_str: Дата в формате '2024-03-11T02:26:18.671407'

    Returns:
        Дата в формате '11.03.2024'
    """
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")


if __name__ == "__main__":
    # Примеры использования (для тестирования)
    print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
    print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305
    print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024
