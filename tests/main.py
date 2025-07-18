from typing import List, Dict, Any


def filter_by_state(
        operations: List[Dict[str, Any]],
        state: str = 'EXECUTED'
) -> List[Dict[str, Any]]:
    """Фильтрует список операций по указанному статусу.

    Args:
        operations: Список словарей с банковскими операциями
        state: Статус для фильтрации (по умолчанию 'EXECUTED')

    Returns:
        Отфильтрованный список операций
    """
    if not operations:
        return []

    return [op for op in operations if op.get('state') == state]


def sort_by_date(
        operations: List[Dict[str, Any]],
        reverse: bool = True
) -> List[Dict[str, Any]]:
    """Сортирует операции по дате.

    Args:
        operations: Список словарей с банковскими операциями
        reverse: Если True - сортировка по убыванию (новые сначала),
                 если False - по возрастанию

    Returns:
        Отсортированный список операций

    Raises:
        KeyError: Если в каком-либо словаре отсутствует ключ 'date'
    """
    if not operations:
        return []

    for op in operations:
        if 'date' not in op:
            raise KeyError(f"Отсутствует ключ 'date' в операции: {op}")

    return sorted(operations, key=lambda x: x['date'], reverse=reverse)


if __name__ == "__main__":
    test_data = [
        {
            'id': 41428829,
            'state': 'EXECUTED',
            'date': '2019-07-03T18:35:29.512364'
        },
        {
            'id': 939719570,
            'state': 'EXECUTED',
            'date': '2018-06-30T02:08:58.425572'
        },
        {
            'id': 594226727,
            'state': 'CANCELED',
            'date': '2018-09-12T21:27:25.241689'
        },
    ]

    print("Фильтрация (EXECUTED):", filter_by_state(test_data))
    print("Фильтрация (CANCELED):", filter_by_state(test_data, 'CANCELED'))
    print("Сортировка (по убыванию):", sort_by_date(test_data))
    print("Сортировка (по возрастанию):", sort_by_date(test_data, False))