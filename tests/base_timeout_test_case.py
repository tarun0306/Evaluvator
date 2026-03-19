import signal
import unittest
from types import FrameType
from typing import Optional


class BaseTimeoutTestCase(unittest.TestCase):
    """Base test case enforcing a strict per-test timeout."""

    def setUp(self) -> None:
        """Start a strict timer for each test."""
        signal.signal(signal.SIGALRM, self._handle_timeout)
        signal.setitimer(signal.ITIMER_REAL, 0.5)

    def tearDown(self) -> None:
        """Disable the timer after each test."""
        signal.setitimer(signal.ITIMER_REAL, 0)

    def _handle_timeout(
        self,
        signal_number: int,
        frame: Optional[FrameType],
    ) -> None:
        """Raise a timeout error when the timer elapses."""
        raise TimeoutError("Test exceeded the 0.5 second timeout.")
