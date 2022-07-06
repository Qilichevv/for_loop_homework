def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    a = []
    for i in range(1,11):
        a.append(i*price)
    return a
print(main(4.5))
    