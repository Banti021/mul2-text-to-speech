from pydub import AudioSegment

from modules.TextNormalizer import TextNormalizer


class AnnouncementCreator:
    """Class to create an announcement from text and audio files."""

    def __init__(self, audio_files):
        self.audio_files = audio_files

    def find_phrases(self, text):
        """Find and return matching phrases in the audio files."""
        words = text.split('_')
        phrases = []
        i = 0
        while i < len(words):
            found = False
            for j in range(len(words), i, -1):
                phrase = '_'.join(words[i:j])
                if phrase in self.audio_files:
                    phrases.append(phrase)
                    i = j
                    found = True
                    break
            if not found:
                raise ValueError(f"Audio file for '{words[i]}' not found")
        return phrases

    def create_announcement(self, text):
        """Create an announcement audio segment from the given text."""
        normalized_text = TextNormalizer.normalize(text)
        try:
            phrases = self.find_phrases(normalized_text)
            announcement = AudioSegment.silent(duration=1000)
            for phrase in phrases:
                announcement += self.audio_files[phrase] + AudioSegment.silent(duration=500)
            return announcement
        except ValueError as e:
            print(e)
            return None