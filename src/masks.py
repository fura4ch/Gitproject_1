"""Модуль для маскировки номеров банковских карт и счетов."""


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты по шаблону XXXX XX** **** XXXX.

    Показывает первые 6 и последние 4 цифры номера карты,
    остальные символы заменяются на звездочки. Номер разбивается
    на блоки по 4 цифры, разделенные пробелами.

    Args:
        card_number (str): Номер карты в виде строки (только цифры).
                          Должен содержать ровно 16 цифр.

    Returns:
        str: Замаскированный номер карты в формате XXXX XX** **** XXXX.

    Raises:
        ValueError: Если номер карты не содержит 16 цифр.
    """
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен содержать 16 цифр")

    masked_part = "** ****"
    first_part = card_number[:6]
    last_part = card_number[-4:]

    return f"{first_part[:4]} {first_part[4:6]}{masked_part} {last_part}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета по шаблону **XXXX.

    Показывает только последние 4 цифры номера счета,
    перед которыми стоят две звездочки.

    Args:
        account_number (str): Номер счета в виде строки (только цифры).
                             Должен содержать минимум 4 цифры.

    Returns:
        str: Замаскированный номер счета в формате **XXXX.

    Raises:
        ValueError: Если номер счета содержит менее 4 цифр.
    """
    if len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")

    return f"**{account_number[-4:]}"
