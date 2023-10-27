from typing import Union

def divide(dividend : Union[int,float], divisor: Union[int, float]):
    if divisor == 0:
        raise ValueError("The divisor can not be 0.")
    return dividend / divisor