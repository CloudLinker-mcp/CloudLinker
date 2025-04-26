"""Logging configuration for the application."""

import sys
import structlog

def get_logger(name: str) -> structlog.BoundLogger:
    """Get a logger instance.
    
    Args:
        name: The name of the logger (usually __name__)
        
    Returns:
        A configured structlog logger
    """
    structlog.configure(
        processors=[
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
        wrapper_class=structlog.BoundLogger,
        cache_logger_on_first_use=True,
    )
    
    return structlog.get_logger(name) 