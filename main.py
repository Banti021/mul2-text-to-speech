import os

from modules.AnnouncementCreator import AnnouncementCreator
from modules.AudioLoader import AudioLoader


def main():
    base_dir = os.path.join(os.getcwd(), "data")
    print(f"Current working directory: {base_dir}")

    # Load audio files
    audio_loader = AudioLoader(base_dir)
    audio_files = audio_loader.audio_files

    # Create an announcement
    text = "Pociąg do stacji Warszawa Wschodnia, Przez stacje Kutno, Odjedzie z toru drugiego przy peronie trzecim"
    announcement_creator = AnnouncementCreator(audio_files)
    announcement = announcement_creator.create_announcement(text)

    # Export the announcement if created
    if announcement:
        output_dir = os.path.join(base_dir, "announcements")
        output_file = os.path.join(output_dir, "announcement.wav")
        announcement.export(output_file, format="wav")
        print(f"Announcement saved to {output_file}")
    else:
        print("Failed to create announcement due to missing audio files.")


if __name__ == "__main__":
    main()