"""
Hex Colours
Estimate: 15 minutes
Actual: 17 minutes
"""

COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlueViolet": "#8a2be2",
    "Brown": "#a52a2a"
}


def main():
    colour_name = input("Enter a colour name: ").strip()
    while colour_name != "":
        colour_key = colour_name.title()
        try:
            print(f"The code for {colour_key} is {COLOUR_TO_HEX[colour_key]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter a colour name: ").strip()


if __name__ == "__main__":
    main()
