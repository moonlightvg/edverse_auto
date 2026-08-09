from datetime import datetime

def current_timestamp() -> str:
    """Текущее время для уникальных имён: 20260809_223000."""
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def unique_screenshot_name(prefix: str) -> str:
    """Имя скриншота с timestamp — файлы не перезаписываются."""
    return f"{prefix}_{current_timestamp()}.png"
