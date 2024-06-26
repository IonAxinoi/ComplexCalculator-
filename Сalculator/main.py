from ComplexCalculator import ComplexCalculator, ComplexNumber
import logging

# Настройка логгера для main.py
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    calculator = ComplexCalculator()
    
    num1 = ComplexNumber(2, 3)
    num2 = ComplexNumber(1, 4)
    
    result_add = calculator.add(num1, num2)
    logger.info(f"Результат сложения: {result_add}")
    
    result_multiply = calculator.multiply(num1, num2)
    logger.info(f"Результат умножения: {result_multiply}")
    
    result_divide = calculator.divide(num1, num2)
    logger.info(f"Результат деления: {result_divide}")

if __name__ == "__main__":
    main()
