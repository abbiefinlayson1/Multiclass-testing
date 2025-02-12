class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        self.title = title
        self.contents = contents
        self.current_position = 0 

    def count_words(self):
       title_length = self.title.split()
       content_length = self.contents.split()
       return len(title_length) + len(content_length)
    

    def reading_time(self, wpm):
        length = self.count_words()
        return length / wpm

    def reading_chunk(self, wpm, minutes):
        total_words = minutes * wpm #calculates total words able to read
        start = self.current_position # assigned the current postion to the start variable 
        combined_entry = " ".join([self.title, self.contents]) # joins together the title and contents
        words = combined_entry.split() #splits them into a list 
        end = start + total_words #end is the self.current_position amount plus the total words able to read
    
        if end >= len(words): # if the end amount is more or equal to the length of the 
            self.current_position = 0
            chunk = words[start:]  
        else:
            chunk = words[start:end]
            self.current_position = end  
        return " ".join(chunk)
