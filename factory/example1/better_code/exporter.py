from factory import ExporterFactory
from video_exporter import IVideoExporter
from video_quality import LosslessVideoExporter, H264BPVideoExporter, H264Hi422PVideoExporter
from audio_exporter import IAudioExporter
from audio_quality import AACAudioExporter, WAVAudioExporter


class FastExporter(ExporterFactory):
    """Factory aimed at providing a high speed, lower quality export."""

    def get_video_exporter(self) -> IVideoExporter:
        return H264BPVideoExporter()

    def get_audio_exporter(self) -> IAudioExporter:
        return AACAudioExporter()


class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing a slower speed, high quality export."""

    def get_video_exporter(self) -> IVideoExporter:
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self) -> IAudioExporter:
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """Factory aimed at providing a low speed, master quality export."""

    def get_video_exporter(self) -> IVideoExporter:
        return LosslessVideoExporter()

    def get_audio_exporter(self) -> IAudioExporter:
        return WAVAudioExporter()