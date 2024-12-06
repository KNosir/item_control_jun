import logging


logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="files/app.log",
    filemode="a"
)
logger = logging.getLogger("error_loger")


def log_call(func):
    def wrapper(*args, **kwargs):
        logger.info(
            f"Calling {func.__name__} with args: {args} and kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
            raise
    return wrapper
