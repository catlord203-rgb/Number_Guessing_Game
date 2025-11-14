# ...existing code...
import random


class NumberGuessingGame:
    def __init__(self, min_num=1, max_num=100, max_attempts=10):
        self.min_num = min_num
        self.max_num = max_num
        self.max_attempts = max_attempts
        self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(self.min_num, self.max_num)
        self.attempts = 0
        self.is_over = False
        self.won = False

    def validate_guess(self, guess):
        if not isinstance(guess, int):
            return False, f"Input bukan angka bulat."
        if guess < self.min_num or guess > self.max_num:
            return False, f"Tebakan harus antara {self.min_num} dan {self.max_num}."
        return True, ""

    def check_guess(self, guess):
        if guess == self.secret_number:
            return "correct"
        if guess > self.secret_number:
            return "high"
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
                "message": f"Benar! Angka rahasia adalah {self.secret_number}.",
                "attempts": self.attempts,
                "score": score,
            }

        if self.attempts >= self.max_attempts:
            self.is_over = True
            return {
                "status": "lost",
                "message": f"Kalah. Percobaan habis. Angka rahasia: {self.secret_number}.",
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
        print(f"Selamat datang di Tebak Angka! Tebak angka antara {self.min_num} dan {self.max_num}.")
        print(f"Kamu punya {self.max_attempts} percobaan.\n")
        while not self.is_over:
            user_input = input(f"Masukkan tebakan ({self.min_num}-{self.max_num}): ").strip()
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
    game = NumberGuessingGame()
    game.play()


if __name__ == "__main__":
    play_game()
# ...existing code...