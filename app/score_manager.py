import json
import os.path

class ScoreManager:
    def __init__(self, score_file="high_score.json"):
        self.score_file = score_file
        self.high_score = self.load_high_score()
        self.current_score = 0

    def load_high_score(self):
        try:
            if os.path.exists(self.score_file):
                with open(self.score_file, "r") as file:
                    data = json.load(file)
                    return data.get("high_score", 0)
        except (json.JSONDecodeError, FileNotFoundError):
            print("Error loading high score. Initializing to 0.")
        return 0

    def save_high_score(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            try:
                with open(self.score_file, "w") as file:
                    json.dump({"high_score": self.high_score}, file)
            except IOError:
                print("Error saving high score.")

    def update_score(self, points):
        self.current_score += points

    def reset_score(self):
        self.current_score = 0
