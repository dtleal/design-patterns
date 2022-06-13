from abc import ABC, abstractmethod
from video_exporter import IVideoExporter
from audio_exporter import IAudioExporter


class ExporterFactory(ABC):
    """
    Factory that represents a combination of video and audio codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter(self) -> IVideoExporter:
        """Returns a new video exporter belonging to this factory."""

    @abstractmethod
    def get_audio_exporter(self) -> IAudioExporter:
        """Returns a new audio exporter belonging to this factory."""
    