from main import main_menu
from io import StringIO
import sys 

def test_main_menu_exit_game(monkeypatch):
    # lambda is a keyword function that can take any number of argument but only one expression
    # monkeypatch.setattr is temporarily replace the behaviour of the input
    monkeypatch.setattr('builtins.input', lambda _: "4")

    # stdout transfers to a strinIO object
    sys.stdout = StringIO()

    # calls the Main_menu funtion
    main_menu()

    # Fetches the captured output
    captured = sys.stdout.getvalue()

    # check if the objected in captured
    assert "Thank you for playing hope to see you soon!!!" in captured

    # Resets stdout back to original value
    sys.stdout = sys.__stdout__

# Capsys alows us to capture the output printed to stdout
def test_main_menu_prints_welcome_message_and_options(monkeypatch, capsys):
    # 
    monkeypatch.setattr('builtins.input', lambda _: "4")

    # Calls main menu function
    main_menu()

    # Fetches the captured output
    captured = capsys.readouterr()

    # Capture objects and expected welcome messages and options are checked
    assert "Welcome to this mutliple choice quiz game!!!" in captured.out
    assert "1) Movie Quiz 🎥" in captured.out
    assert "2) Cartoon Quiz 🐱" in captured.out
    assert "3) View HighScore 🏆" in captured.out
    assert "4) Exit Game ❌" in captured.out

    # Reset stdout back to it original value
    sys.sydout = sys.__stdout__