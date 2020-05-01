import sys, os
import re

def print_welcome():
    """ 
    Description: This method prints welcome message
    """
    welcome_message = """Let's play a game. 
    1) Answer the questions
    2) See a funny response on that
    """

def read_template(file_path):
    """ 
    Attributes : File path where templaet resides
    Description: This method opens the template in the python directory and reads the content
    Return     : Returns content of the file as a string
    """
    template = open(file_path + "\\template.txt", "r")
    template_content = template.read()
    template.close()
    return(template_content)

def find_keywords(template_content):
    """ 
    Attributes : Input string value
    Description: This method will find all keywords within curly braces {} 
    Return     : Returns list of keywords (words within {}) in a string 
    """
    return re.findall('{([^}]+)', template_content) 

def prompt_user_for_inputs(keywords):
    """ 
    Attributes : Keywords for which user input is needed
    Description: This method will get values for each keyword in the template
    Return     : Returns a list of dictionary items with keywords and values from user
    """    
    dictList = []
    answers = []
    for i in range(len(keywords)):
        answers.append(input(f"Enter a {keywords[i]}"))
        dictList.append(dict(zip(keywords, answers)))
    return dictList

def frame_sentence(template_content,keywords,user_inputs):
    """ 
    Attributes : String, List of keywords that should be replaced with user inputs, List of dictionary with user inputs
    Description: This method will frame sentence by replacing keyword in input string with user inputs
    Return     : Returns a string which replaces keywords in input string with user inputs
    """        
    temp_content = template_content
    for i in range(len(user_inputs)):
      keyword = keywords[i]
      user_input = user_inputs[i][keyword]
      keyword_to_replace = "{" + keyword + "}"
      temp_content = temp_content.replace(keyword_to_replace,user_input,1)

    return temp_content

def write_output(framed_sentence):
    """ 
    Attributes : String value that needs to be written to output file
    Description: This method will write input string to output file
    """    
    output_file = open(os.path.join(sys.path[0], "output_file.txt"), "w")
    output_file.write(framed_sentence)
    output_file.close()

def main():
    print_welcome()
    file_path = os.path.join(sys.path[0])
    template_content = read_template(file_path)
    keywords = find_keywords(template_content)
    user_inputs = prompt_user_for_inputs(keywords)
    framed_sentence = frame_sentence(template_content,keywords,user_inputs)
    write_output(framed_sentence)
    print(framed_sentence)

if __name__ == "__main__":
    main()