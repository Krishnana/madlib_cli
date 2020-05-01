import sys, os
import re

def print_welcome():
    welcome_message = """Let's play a game. 
    1) Answer the questions
    2) See a funny response on that
    """

def read_template(file_path):
    template = open(file_path + "\\template.txt", "r")
    template_content = template.read()
    template.close()
    return(template_content)

def find_keywords(template_content):
    return re.findall('\{([^}]+)', template_content) 

def prompt_user_for_inputs(keywords):
    dictList = []
    answers = []
    for i in range(len(keywords)):
        answers.append(input(f"Enter a {keywords[i]}"))
        dictList.append(dict(zip(keywords, answers)))
    return dictList

def frame_sentence(template_content,keywords,user_inputs):
    temp_content = template_content
    for i in range(len(user_inputs)):
      keyword = keywords[i]
      user_input = user_inputs[i][keyword]
      keyword_to_replace = "{" + keyword + "}"
      temp_content = temp_content.replace(keyword_to_replace,user_input,1)

    return temp_content

def write_output(framed_sentence):
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