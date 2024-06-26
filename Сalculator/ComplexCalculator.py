import logging

# Получение логгера для модуля
logger = logging.getLogger(__name__)

# Не настраивать логгер здесь, чтобы не дублировать настройки

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    
    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

class ComplexCalculator:
    def __init__(self):
        pass
    
    def add(self, num1, num2):
        result_real = num1.real + num2.real
        result_imaginary = num1.imaginary + num2.imaginary
        logger.info(f"Выполнено сложение: {num1} + {num2} = {result_real} + {result_imaginary}i")
        return ComplexNumber(result_real, result_imaginary)
    
    def multiply(self, num1, num2):
        result_real = num1.real * num2.real - num1.imaginary * num2.imaginary
        result_imaginary = num1.real * num2.imaginary + num1.imaginary * num2.real
        logger.info(f"Выполнено умножение: {num1} * {num2} = {result_real} + {result_imaginary}i")
        return ComplexNumber(result_real, result_imaginary)
    
    def divide(self, num1, num2):
        denominator = num2.real**2 + num2.imaginary**2
        result_real = (num1.real * num2.real + num1.imaginary * num2.imaginary) / denominator
        result_imaginary = (num1.imaginary * num2.real - num1.real * num2.imaginary) / denominator
        logger.info(f"Выполнено деление: {num1} / {num2} = {result_real} + {result_imaginary}i")
        return ComplexNumber(result_real, result_imaginary)
