from lib.diary_entry import *

def test_diary_entry():
    diary_entry = DiaryEntry("title","contents")

def test_count_words():
    diary_entry = DiaryEntry("title","contents")
    result = diary_entry.count_words()
    assert result == 2

def test_count_twowords():
    diary_entry = DiaryEntry("the title","the contents")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("the title","the contents")
    result = diary_entry.reading_time(2)
    assert result == 2

def test_reading_chunk():
    diary_entry = DiaryEntry("the title","the contents the contents the contents the contents the contents the contents the contents the contents the contents")
    result = diary_entry.reading_chunk(2,10)
    assert result == "the title the contents the contents the contents the contents the contents the contents the contents the contents the contents"