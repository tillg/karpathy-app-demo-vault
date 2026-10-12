"""Brew ratio helper: grams of water for a given dose."""

RATIO = 16  # see [[brew-ratio]] — this stays plain text in a .py file


def water_for(dose_g: float, ratio: float = RATIO) -> float:
    return round(dose_g * ratio, 1)


if __name__ == "__main__":
    for dose in (15, 18, 20):
        print(f"{dose} g coffee -> {water_for(dose)} g water")
