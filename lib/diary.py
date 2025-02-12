from lib.diary_entry import *
import math 

class Diary:
    def __init__(self):
        self.diaryentries = [] 

    def add(self, entry):
        self.diaryentries.append(entry)

    def all(self):
        return self.diaryentries

    def count_words(self):
        total_word_count = 0
        for entry in self.diaryentries:
            total_word_count += entry.count_words()
        return total_word_count

        

    def reading_time(self, wpm):
        total_words = self.count_words()
        reading_time = total_words / wpm
        return math.ceil(reading_time)


    def find_best_entry_for_reading_time(self, wpm, minutes):

        total_words = wpm * minutes
        best_entry = None
        best_fit = 0
        
        for entry in self.diaryentries: 
            entry_wordcount = entry.count_words()
            if entry_wordcount <= total_words and entry_wordcount > best_fit:
                best_fit = entry_wordcount
                best_entry = entry
        return best_entry

        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass