import random
class Number_Guessing_Game:
     def __init__(self,min=1,max=100,max_attempts=5):
          self.max=max
          self.min=min
          self.max_attempts=max_attempts
          self.reset_game()
     def reset_game(self):
          self.hidden_number=random.randint(self.min,self.max)
          self.attempts=0
          self.game_over=False
          self.won = False
          self.is_over = False

     def validate_guess(self, guess):
          if not isinstance(guess, int):
               return False, f"Input is not a whole number."
          if guess < self.min or guess > self.max:
               return False, f"(The guess has to be between{self.min} and {self.max}.)"
          return True, ""              
     def check_guess(self, guess):
          if guess == self.hidden_number:
               return "correct"
          elif guess > self.hidden_number:
               return "high"
          else:
               return "low"               
     def make_guess(self, guess_raw):
        try:
            guess = int(guess_raw)
        except ValueError:
            return {"status": "invalid", "message": "Masukkan angka yang valid."}

        valid, msg = self.validate_guess(guess)
        if not valid:
            return {"status": "invalid", "message": msg}

        self.attempts += 1
        result = self.check_guess(guess)

        if result == "correct":
            self.is_over = True
            self.won = True
            score = max(self.max_attempts - (self.attempts - 1), 0)
            return {
                "status": "correct",
                "message": f"Benar! Angka rahasia adalah {self.hidden_number}.",
                "attempts": self.attempts,
                "score": score,
            }

        if self.attempts >= self.max_attempts:
            self.is_over = True
            return {
                "status": "lost",
                "message": f"Kalah. Percobaan habis. Angka rahasia: {self.hidden_number}.",
                "attempts": self.attempts,
            }

        hint = "terlalu tinggi" if result == "high" else "terlalu rendah"
        remaining = self.max_attempts - self.attempts
        return {
            "status": "continue",
            "message": f"Tebakan {hint}. Coba lagi.",
            "attempts": self.attempts,
            "remaining": remaining,
        }

     def play(self):
        print(f"Selamat datang di Tebak Angka! Tebak angka antara {self.min} dan {self.max}.")
        print(f"Kamu punya {self.max_attempts} percobaan.\n")
        while not self.is_over:
            user_input = input(f"Masukkan tebakan ({self.min}-{self.max}): ").strip()
            result = self.make_guess(user_input)

            if result["status"] == "invalid":
                print("Input tidak valid:", result["message"])
                continue

            if result["status"] == "correct":
                print(result["message"])
                print(f"Menang dalam {result['attempts']} percobaan. Skor: {result['score']}")
                break

            if result["status"] == "lost":
                print(result["message"])
                break

            # continue
            print(result["message"])
            print(f"Percobaan: {result['attempts']}. Sisa percobaan: {result['remaining']}\n")


def play_game():
    game = Number_Guessing_Game()
    game.play()


if __name__ == "__main__":
    play_game()