class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage:
# linked_list = LinkedList()
# linked_list.append(1)
# linked_list.append(2)
# linked_list.append(3)
# linked_list.prepend(0)
# linked_list.print_list()


class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if self.head is None:
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next:
                current_song = current_song.next
            current_song.next = new_song

    def remove_song(self, title):
        current_song = self.head
        if current_song and current_song.title == title:
            self.head = current_song.next
            return
        prev_song = None
        while current_song and current_song.title != title:
            prev_song = current_song
            current_song = current_song.next
        if current_song:
            prev_song.next = current_song.next

    def display_playlist(self):
        current_song = self.head
        while current_song:
            print(f"{current_song.title} - {current_song.artist}")
            current_song = current_song.next

# Example usage:
playlist = Playlist()
playlist.add_song("Song 1", "Artist 1")
playlist.add_song("Song 2", "Artist 2")
playlist.add_song("Song 3", "Artist 3")

print("Initial Playlist:")
playlist.display_playlist()

print("\nAfter removing 'Song 2':")
playlist.remove_song("Song 2")
playlist.display_playlist()
