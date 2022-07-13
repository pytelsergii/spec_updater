def str_price_to_float(price_str: str) -> float:
    """
    Convert str price to float
    Example 7 865,00 грн -> 7865
    """
    price_str = price_str.replace(',', '.')
    formatted_price = ''.join(i for i in price_str if i.isdigit() or i == '.')
    if formatted_price.endswith('.'):
        formatted_price = formatted_price[:-1]
    try:
        price = float(''.join(formatted_price))
    except ValueError:
        price = 0
    return price
