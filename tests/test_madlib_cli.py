from madlib_cli import __version__
from madlib_cli.madlib import read_template
from madlib_cli.madlib import find_keywords
from madlib_cli.madlib import frame_sentence
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_read_template():
    file_path = "madlib_cli"
    assert "I am the {noun}" in read_template(file_path)

def text_file_not_found_exception():
    with pytest.raises(FileNotFoundError):
        file_path = "madlib_cli"
        read_template(file_path)

@pytest.mark.parametrize("template_content,expected",[("I am the {noun}",["noun"]),("I am a {adjective} {noun}",["adjective","noun"])])
def test_find_keywords(template_content,expected):
    assert find_keywords(template_content) == expected

@pytest.mark.parametrize("template_content,keywords,user_inputs,expected",[("I am the {noun}",["noun"],[{"noun":"king"}],"I am the king"),("I am a {adjective} {noun}",["adjective","noun"],[{"adjective":"great"},{"noun":"king"}],"I am a great king")])
def test_frame_sentence(template_content,keywords,user_inputs,expected):
    assert frame_sentence(template_content,keywords,user_inputs) == expected