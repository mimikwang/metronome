from typing import Self

import numpy as np
import sounddevice as sd


class Speaker:
    def __init__(
        self,
        *,
        device: int | str | None = None,
        bpm: int = 100,
        sample_rate: int = 48_000,
    ):
        """Uses sounddevice to play sounds through the speaker"""
        self._stream = sd.OutputStream(
            device=device,
            channels=1,
            callback=self._callback,
            samplerate=sample_rate,
            blocksize=int(sample_rate * 60 / bpm),
        )

    def _callback(self, outdata: np.ndarray, frames: int, time, status) -> None:
        outdata.fill(0)
        outdata[:10, 0] = 0.5

    def __enter__(self) -> Self:
        self.start()
        return self

    def __exit__(self, *exc_info) -> None:
        self.stop()

    def start(self):
        self._stream.start()

    def stop(self):
        self._stream.stop()
