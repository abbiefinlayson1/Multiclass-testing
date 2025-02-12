from lib.diary import *
from lib.diary_entry import *


"""
When a diary entry is added 
A list of instances is returned 
"""
def test_diary_entry_integration():
    diary = Diary()
    diary_entry = DiaryEntry("title","content")
    diary.add(diary_entry)
    result = diary.all()
    assert result == [diary_entry]

"""
Using the diary entries, an integer representing the number of words in all diary entries is returned
"""
def test_diary_integration_count_words():
    diary = Diary()
    diary_entry1 = DiaryEntry("title","content")
    diary_entry2 = DiaryEntry("title1","content1")
    diary_entry3 = DiaryEntry("title2","content2")
    diary_entry4 = DiaryEntry("title3","content3")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    diary.add(diary_entry4)
    result = diary.count_words()
    assert result == 8


def test_diary_integration_reading_time():
    diary = Diary()
    diary_entry1 = DiaryEntry("title","content")
    diary_entry2 = DiaryEntry("title1","content1")
    diary_entry3 = DiaryEntry("title2","content2")
    diary_entry4 = DiaryEntry("title3","content3")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    diary.add(diary_entry4)
    result = diary.reading_time(4)
    assert result == 2

def test_diary_integration_best_entry():
    diary = Diary()
    diary_entry1 = DiaryEntry("title1", "content with a few words")
    diary_entry2 = DiaryEntry("title2", "content with more words than the first one")
    diary_entry3 = DiaryEntry("title3", "content with even more words, a bit longer")
    diary_entry4 = DiaryEntry("title4", "content with a significant number of words. It will be the longest entry.")
    diary.add(diary_entry1)
    diary.add(diary_entry2)
    diary.add(diary_entry3)
    diary.add(diary_entry4) 
    result = diary.find_best_entry_for_reading_time(10, 1)
    assert result.title == diary_entry2.title
    assert result.contents == diary_entry2.contents