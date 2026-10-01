def calculate_subtotal(prices: list[float]) -> float:
    """Calculate subtotal from a list of prices."""
    total = 0.0
    for price in prices:
        if price < 0:
            raise ValueError(f"Price cannot be negative: {price}")
        total += price
    return round(total, 2)


def apply_tax(amount: float, tax_rate: float) -> float:
    """Apply tax rate to an amount."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
    return round(amount * (1.0 + tax_rate), 2)
