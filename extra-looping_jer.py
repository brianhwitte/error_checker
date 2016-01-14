#convert text to array

#takes a string returns an array of strings broken by new line and by a max number count

#follow up function

#be able to go through that array character by character

text_array = "Several Lines of text.\nThat we want to try and fit on to a certain size screen.\nSo we want to draw one line up until the new line, unless the length of the line is longer then the screen size, then we need to break that line up into items in that array"


def print_screen(array_lines):
    for line in array_lines:
        print line

def first(text):
    if not text:
        return ""

    return text[0]

def rest(text):
    if not text:
        return ""
    return text[1:]


def text_to_array(text,current_text,screen_width):
    
    c = first(text)

    if len(c) == 0:
        return [current_text]

    if c == '\n' or len(current_text+c) == screen_width:
        return [current_text+c] + text_to_array(rest(text),"",screen_width)

    return text_to_array(rest(text),current_text+c,screen_width)

        



