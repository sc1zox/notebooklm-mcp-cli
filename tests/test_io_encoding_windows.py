"""Windows stdio UTF-8 bootstrap (Issue #156)."""

import sys
from unittest.mock import MagicMock


def test_configure_stdio_noop_on_non_windows(monkeypatch):
    from notebooklm_tools.utils.io_encoding import configure_stdio_utf8_on_windows

    monkeypatch.setattr(sys, "platform", "linux")
    fake = MagicMock()
    monkeypatch.setattr(sys, "stdout", fake)
    configure_stdio_utf8_on_windows()
    fake.reconfigure.assert_not_called()


def test_configure_stdio_calls_reconfigure_on_windows(monkeypatch):
    from notebooklm_tools.utils.io_encoding import configure_stdio_utf8_on_windows

    monkeypatch.setattr(sys, "platform", "win32")
    out = MagicMock()
    err = MagicMock()
    monkeypatch.setattr(sys, "stdout", out)
    monkeypatch.setattr(sys, "stderr", err)

    configure_stdio_utf8_on_windows()

    out.reconfigure.assert_called_once_with(encoding="utf-8", errors="replace")
    err.reconfigure.assert_called_once_with(encoding="utf-8", errors="replace")
