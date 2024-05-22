#class Book():
#    def read(self):
#        print("Reading of interesting story")
#
#class StoryReader():
#    def __init__(self):
#        self.book = book()
#
#    def tell_story(self):
#        self.book.read()

from abc import ABC, abstractmethod

class StorySources(ABC):
    @abstractmethod
    def get_story(self):
        pass

class Book(StorySources):
    def get_story(self):
        print("Reading of interesting story")

class AudioBook(StorySources):
    def get_story(self):
        print("Reading of interesting story by listening")

class StoryReader():
    def __init__(self, story_source: StorySources):
        self.story_source = story_source

    def tell_story(self):
        self.story_source.get_story()

book = Book()
audiobook = AudioBook()

readerBook = StoryReader(book)

readerAudioBook = StoryReader(audiobook)


readerBook.tell_story()
readerAudioBook.tell_story()