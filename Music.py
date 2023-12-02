import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.playlist = []
        self.current_track_index = 0

    def add_to_playlist(self, song_path):
        self.playlist.append(song_path)

    def play(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        pygame.mixer.music.load(self.playlist[self.current_track_index])
        pygame.mixer.music.play()

    def next_track(self):
        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play()

    def display_playlist(self):
        print("Current Playlist:")
        for i, song in enumerate(self.playlist):
            print(f"{i + 1}. {os.path.basename(song)}")

def main():
    player = MusicPlayer()

    while True:
        print("\nOptions:")
        print("1. Add to Playlist")
        print("2. Play")
        print("3. Next Track")
        print("4. Previous Track")
        print("5. Display Playlist")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            song_path = "D:\\internship\\Music\\"+input("Enter the file Name with .mp3: ")
            player.add_to_playlist(song_path)
        elif choice == "2":
            player.play()
        elif choice == "3":
            player.next_track()
        elif choice == "4":
            player.prev_track()
        elif choice == "5":
            player.display_playlist()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
