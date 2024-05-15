import os

from pydub import AudioSegment


def load_audio_files(directory):
    """Load all .wav audio files from a given directory."""
    audio_files = {}
    if not os.path.isdir(directory):
        print(f"Directory does not exist: {directory}")
        return audio_files

    for filename in os.listdir(directory):
        if filename.endswith(".wav"):
            key = filename.replace(".wav", "")
            audio_files[key] = AudioSegment.from_wav(os.path.join(directory, filename))
    return audio_files


class AudioLoader:
    """Class to load and manage audio files from directories."""

    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.audio_files = self.load_all_audio_files()

    def load_all_audio_files(self):
        """Load audio files from all predefined directories."""
        directories = ["stacje", "perony_i_tory", "do_z_stacji"]
        all_audio_files = {}
        for dir_name in directories:
            directory = os.path.join(self.base_dir, dir_name)
            all_audio_files.update(load_audio_files(directory))
        return all_audio_files