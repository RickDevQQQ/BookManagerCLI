

class ApplicationException(Exception):
    """Ошибка приложения"""
    pass


class NotFoundEntityError(ApplicationException):
    """Не найдена сущность"""
    pass


class ParseException(ApplicationException):
    """Ошибки парсинга"""
    pass


class MissingRequiredArgsError(ParseException):
    """Отсутствуют обязательные аргументы"""
    pass


class TransformError(ParseException):
    """Ошибка при попытке трансформировать"""
    pass


class NotFoundCommandError(ApplicationException):
    """Ошибка не найдена команда"""
    pass
