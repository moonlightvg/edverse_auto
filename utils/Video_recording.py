# utils/Video_recording.py
import allure
from pathlib import Path


def attach_video(page, name: str = "Видео теста") -> None:
    """Прикрепляет видео сеанса к отчёту Allure (если запись включена)."""
    if page.video is None:          # запись не включена — выходим
        return
    path = page.video.path()
    if path and Path(path).exists():
        allure.attach.file(
            str(path),
            name=name,
            attachment_type=allure.attachment_type.WEBM,
        )