
import os
import pytest
from app.score_manager import ScoreManager

@pytest.fixture
def score_manager():
    # Setup: Create a ScoreManager instance and a temporary high score file
    manager = ScoreManager(score_file="temp_high_score.json")
    yield manager
    # Teardown: Remove the temporary file after each test
    if os.path.exists("temp_high_score.json"):
        os.remove("temp_high_score.json")

def test_initial_high_score(score_manager):
    assert score_manager.high_score == 0

def test_update_score(score_manager):
    score_manager.update_score(10)
    assert score_manager.current_score == 10

def test_save_and_load_high_score(score_manager):
    score_manager.update_score(50)
    score_manager.save_high_score()
    assert score_manager.high_score == 50

    # Create a new instance to load the high score
    new_manager = ScoreManager(score_file="temp_high_score.json")
    assert new_manager.high_score == 50

def test_reset_score(score_manager):
    score_manager.update_score(20)
    score_manager.reset_score()
    assert score_manager.current_score == 0
