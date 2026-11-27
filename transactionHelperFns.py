def convertToUSD( amount: float, currency : str) -> float:
    """
    Convert the given amount from the specified currency to USD.
    
    Parameters:
    amount (float): The amount to be converted.
    currency (str): The currency code of the amount (e.g., 'EUR', 'GBP', 'JPY').
    
    Returns:
    float: The equivalent amount in USD.
    """
    exchange_rates = {
        'EUR': 1.1,  # Example exchange rate
        'GBP': 1.3,
        'JPY': 0.009,
        # Add more currencies and their exchange rates as needed
    }
    
    if currency not in exchange_rates:
        raise ValueError(f"Unsupported currency: {currency}")
    
    usd_amount = amount * exchange_rates[currency]
    return usd_amount