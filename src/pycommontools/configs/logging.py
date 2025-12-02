import logging


def setup_logger(
    name: str | None = None, level: int | str = logging.INFO
) -> logging.Logger:
    """
    Set up and configure a logger.

    Args:
        name: Logger name. If None, returns the root logger.
        level: Logging level (e.g., logging.DEBUG, logging.INFO, "DEBUG", "INFO").

    Returns:
        Configured logger instance.

    Example:
        >>> logger = setup_logger("myapp", level=logging.DEBUG)
        >>> logger = setup_logger("myapp.module", level="WARNING")
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    handler = logging.StreamHandler()
    handler.setLevel(level)

    formatter = logging.Formatter(
        fmt="[{asctime}] {levelname}: {name} - {message}",
        datefmt="%Y-%m-%d %H:%M:%S",
        style="{",
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
