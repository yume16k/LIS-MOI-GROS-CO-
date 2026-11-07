#!/usr/bin/env python3
"""Convertit une température en degrés Celsius en degrés Fahrenheit."""


def main() -> None:
    try:
        celsius = float(input("Température en °C : ").replace(",", "."))
    except ValueError:
        print("Erreur : entre une température valide, par exemple 21.5.")
        return

    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius:g} °C = {fahrenheit:.1f} °F")


if __name__ == "__main__":
    main()
