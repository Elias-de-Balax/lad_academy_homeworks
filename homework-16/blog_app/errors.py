class DuplicateError(Exception):
    """Ошибка дублирования данных в списке"""
    pass

class ParameterNotFoundError(Exception):
    """Параметр функции не найден"""
    pass

class ValidationError(Exception):
    """Ошибка валидации данных"""
    pass