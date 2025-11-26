import logging
from typing import Iterable, Union

Number = Union[int, float]


logging.basicConfig(
    level=logging.INFO,              
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def parse_inputs(raw: Iterable[str], num_type: str) -> list[Number]:

    numbers = []
    for item in raw:
        try:
            if num_type == "int":
                numbers.append(int(item))
            elif num_type == "float":
                numbers.append(float(item))
            else:
                raise ValueError(f"Unsupported number type: {num_type}")
        except ValueError:
            logger.warning(f"Skipping invalid input: {item}")
    return numbers

def add_numbers(numbers: Iterable[Number]) -> Number:
  
    try:
        total = sum(numbers)
        logger.info(f"Sum calculated: {total}")
        return total
    except TypeError as e:
        logger.error(f"Error adding numbers: {e}")
        raise

if __name__ == "__main__":
 
    num_type = input("Enter number type (int/float): ").strip().lower()

   
    raw_values = input("Enter numbers separated by space: ").split()

    
    nums = parse_inputs(raw_values, num_type)

    
    print("Sum:", add_numbers(nums))
