# One Piece Info Fetcher
It’s a simple command-line based program that fetches detailed information about One Piece characters, swords, fruits, and episodes from the One Piece API and displays it to the user.

## Features
- Fetches detailed information about **characters**, including age, bounty, crew, and devil fruit.
- Fetches information about **swords**, including description, category, and destruction status.
- Fetches information about **fruits**, including type, Japanese name, description, and image.
- Fetches information about **episodes**, including title, description, release date, and chapter.
- Interactive terminal menu for selecting the type of information.
- Handles both name-based and episode number-based queries.

## How the Program Works
Run the program and choose a category from the menu:

- **Characters (Option 1)**: Enter the character's name to get details like age, bounty, crew, and devil fruit.
- **Swords (Option 2)**: Enter the sword's name to get its description, category, and destruction status.
- **Fruits (Option 3)**: Enter the fruit's name to get type, Japanese name, description, and image link.
- **Episodes (Option 4)**: Enter the episode number to get title, description, release date, and chapter.

The program prints all relevant information in a readable format directly in the terminal.

## How to Run the Program
1. Make sure **Python** is installed.
2. Install the required module:
    ```bash
   pip install requests
3. Run the program using:
   ```bash
   python main.py

## File Structure
```bash
project/
│── .python-version
│── main.py
│── pyproject.toml
│── readme.md
│── uv.lock
```
## Technologies Used
- Python
- requests

## Notes
- The program requires an active internet connection to fetch data.
- The program fetches information dynamically from the One Piece API.
- Make sure to enter valid names or episode numbers; otherwise, the program may return no results.

## Author
Muhammad Awais Tariq

---
If you like this project, consider giving it a star on GitHub!
