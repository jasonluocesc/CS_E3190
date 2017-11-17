def pretty_print(text, max_line_length):
    """For a string and a number, representing maximum line length, return a
       pretty-printed version of the string: replace some spaces with linebreaks
       such that raggedness (=sum((len(line)-max_line_lemgth)**2) excluding the
       last line) is minimized. The cost of the last line is considered to be 0.
    """
    words = text.split()
    # Write your code here. 
    
    # The following is just an example of the correct output format.
    lines = words 
    return lines.join("\n")