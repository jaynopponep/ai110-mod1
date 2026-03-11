from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_too_high_message():
    outcome, message = check_guess(80, 50)
    assert outcome == "Too High"
    assert message == "📉Go LOWER!"

def test_too_low_message():
    outcome, message = check_guess(20, 50)
    assert outcome == "Too Low"
    assert message == "📈Go HIGHER!"
