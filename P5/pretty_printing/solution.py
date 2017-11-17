def pretty_print(text, max_line_length):
    """For a string and a number, return a pretty-printed version
       of the string: replace some spaces with linebreaks such 
       that the total amount of wasted space at the ends of lines
       is minimized.
    """
    words = text.split()
    # Write your code here. 
    
    # The following is just an example of the correct output format.
    lines = words 
    return "\n".join(lines)