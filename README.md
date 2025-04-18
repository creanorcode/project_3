[![Battleship-logga1.webp](https://i.postimg.cc/5tzM1x5j/Battleship-logga1.webp)](https://postimg.cc/nsnWGfPt)

# Welcome to Battleship

Battleship is a terminal-based implementation of the classic game of strategy and skill. The project is designed for players who enjoy turn-based games and want a fun, interactive challenge. 

[![Battleship-mockup.png](https://i.postimg.cc/pVScmpvT/Battleship-mockup.png)](https://postimg.cc/4nzQM4mk)

This implementation of Battleship allows players to customize their game setup, including board size and number of ships. It uses Python libraries **NumPy** and **Rich** to enhance performance and improve the user experience with efficient board management and colorful terminal output.

## Features

In this section, we outline the different parts of the project, describing what each provides to the user. The focus is on the player experience and how the features meet their needs.

### Existing Features

- **Dynamic Board Sizes**
  - Players can choose from four different board sizes: 5x5, 8x8, 10x10, or 12x12.
  - Each size supports a range of ship counts for optimal gameplay balance.

- **Customizable Ship Setup**
  - Players can select the number of ships based on the chosen board size:
    - **5x5**: 2–3 ships
    - **8x8**: 3–4 ships
    - **10x10**: 4–5 ships
    - **12x12**: 5–7 ships
  - Ships have varying lengths and types, including destroyers, cruisers, battleships, and submarines.

- **Interactive Gameplay**
    - Players manually place their ships on the board by specifying starting coordinates and direction (horizontal or vertical).
    - Each turn, the player and computer take turnstp target enemy ships.

- **Visual Feedback**
    - **Rich** provides colorful output in the terminal:
        - **Blue cells** represent water.
        - **Green cells** show your own ships.
        - **Red cells** mark hits.
        - **Gray cells** indicate misses.

- **Enhanced Validations**
    - Robust boundary checks ensure ships fit entirely on the board.
    - Overlapping ships are prevented, and invalid inputs prompt the player to try again.

- **Computer AI**
  - The computer places its ships strategically and playes against the player with random targeting.

## Gameplay

The game consists of several phases that guide the player through setup and gameplay. Each phase is described below with accompanying examples to illustrate how it looks in the terminal.

### 1. Select board size:
  - The game will prompt you to select a board size (5x5, 8x8, 10x10 or 12x12).

  [![Battleship-boardsize.png](https://i.postimg.cc/zB4gwmps/Battleship-boardsize.png)](https://postimg.cc/34CN7cs1)


### 2. Choose number of ships:
  - Based on the selected board size, you will be asked to choose the number of ships to play with.

  [![Battleship-number-Ships.png](https://i.postimg.cc/kG8tfjpB/Battleship-number-Ships.png)](https://postimg.cc/JHrnhQmL)


### 3. Place ships manually:
  - Players manually place their ships on the board. For each ship, the player is asked to enter:
    - **Starting position:** Row and column (e.g., 2 3)

    [![Battleships-place-Ships1.png](https://i.postimg.cc/Jh2DmVws/Battleships-place-Ships1.png)](https://postimg.cc/HJbs4Nkm)

    - **Direction:** Horizontal (h) or vertical (v).

    [![Battleship-place-Ships2.png](https://i.postimg.cc/RCnfSFZ4/Battleship-place-Ships2.png)](https://postimg.cc/8sNswTv0)

  - Ships must fit entirely on the board and cannot overlap with other ships. Boundary checks and validations ensure correct placement.

  [![Battleship-place-Ships3.png](https://i.postimg.cc/DyrXGMGN/Battleship-place-Ships3.png)](https://postimg.cc/crJCyTX7)


### 4. Take turns:
  - The player and computer take turns to target cells on the opponent's board.
    - **Hit:** If the cell contains part of a ship, it is marked with 'X'.
    - **Miss:** If the cell is empty, it is marked with 'O'.

    [![Battleship-take-Turn2.png](https://i.postimg.cc/L8mZ33B8/Battleship-take-Turn2.png)](https://postimg.cc/w7bv6JGC)

    [![Battleship-take-Turn3.png](https://i.postimg.cc/1ztnLRdx/Battleship-take-Turn3.png)](https://postimg.cc/NK3jXtYb)


### 5. End Game:
  - The game ends when all ships of one player are sunk.
  - A victory message is displayed for the winner.

  [![Battleship-end-Game.png](https://i.postimg.cc/ZKtNCSW3/Battleship-end-Game.png)](https://postimg.cc/23GyKgF8)
  

## Features Left to Implement

- **Save and Load Game**
    - Allow players to save their progress and resume later.
- **Multiplayer Mode**
    - Enable two players to compete on the same machine or over a network.
- **Graphical User Interface**
    - Use Pygame or similar library to create a graphical version of the game.

## Future Enhancements

### Introduce Data Classes for Ship Management
- **Description**: Replace multiple function arguments related to ship placement (e.g., `row`, `col`, `length`, `direction`) with a single `Ship` data class. This will group ship-related attributes into a single object.
- **Benefits**:
  1. Improves code readability and maintainability by reducing the number of arguments passed to functions.
  2. Makes the code more scalable for future features, such as adding additional ship attributes like health, name, or type.
  3. Aligns the code with modern Python practices using `dataclasses`, which provide a lightweight and efficient way to manage related data.
- **Implementation Plan**:
  - Define a `Ship` data class with attributes like `row`, `col`, `length`, and `direction`.
  - Update functions such as `place_ship_on_board` to accept a `Ship` object instead of individual attributes.
  - Test and validate changes to ensure functionality remains intact.

## Code Quality and Linter Testing

During development, the code was tested using [Pyrfecter.com](https://pyrfecter.com), a Python linter. The linter flagged a complexity issue in the function 'place_ship_manually'. Specifically, it pointed out that the function was too complex due to nested logic and repeated patterns for horizontal and vertical ship placement.

### Refactoring Details

To adress this issue, the function was refactored as follows:
- **Helper functions** were introduced:
  - 'is_position_valid': Validates whether the ship fits on the board and does not overlap.
  - 'place_ship_on_board': Handles the actual placement of the ship on the board.
- This reduced the number of logical branches in 'place_ship_manually', improving readability and reusability.

After the refactor, the code was re-tested with Pyrfecter, and it passed without any issues.

- The original code: [![place-ship-manually-orig.png](https://i.postimg.cc/rph7R9W0/place-ship-manually-orig.png)](https://postimg.cc/PLwSBYST)

- The refactored code: [![function-refac.png](https://i.postimg.cc/hP6Fps39/function-refac.png)](https://postimg.cc/xcvFdvQC) [![function-refac2.png](https://i.postimg.cc/52ChGzZD/function-refac2.png)](https://postimg.cc/jDR3nDqh)

## Testing

In this section, we detail the steps and methods used to verify the project's functionality.

### Validator Testing

- **Python Linter:** Used webbased Pyrfecter.com. Verified using 'pylint' in the terminal to ensure code adheres to PEP 8 standards. Tested the code in Code Institute´s CI Python Linter with no issues.

[![run-py-no-errors.png](https://i.postimg.cc/cC5MZLng/run-py-no-errors.png)](https://postimg.cc/ctw8BZT0)

- **Functionality Testing:**
  - Tested user input validation, including invalid coordinates, out-of bound positions, and overlapping ships.
  - Confirmed correct behavior for hits, misses and victory conditions.
- **Accessibility:**
  - I confirmed the program and site accessible by running it through Lighthouse in devtools.
  [![Lighthouse-performance.png](https://i.postimg.cc/G3PVkrkn/Lighthouse-performance.png)](https://postimg.cc/grJgWCSg)

### Test plan
  - This project was verified through a manual testing.

- **Objectives**
  - Ensure core game mechanics work as intended.
  - Validate input handling and boundary checks.
  - Test the game-over logic.

- **Functional Test Scenarios**

| Features                | Testing Method          | Status |
|-------------------------|-------------------------|--------|
| Board size selection    | Manual                  | ✅ OK  |
| Ship count selection    | Manual                  | ✅ OK  |
| In-bounds placement     | Manual                  | ✅ OK  |
| Overlapping ships       | Manual                  | ✅ OK  |
| Player turns (hit/miss) | Manual                  | ✅ OK  |
| Computer turns          | Manual + random check   | ✅ OK  |
| Game over logic         | Manual                  | ✅ OK  |
| Input validation        | Manual                  | ✅ OK  |

### Unfixed Bugs

- None indentified at this stage. The game has been thoroughly tested for edge cases and invalid input scenarios.

## Deployment

- This project was written in Github and deployed to Heroku for easy access and demonstration.
  - This project was built using the `Code-Institute-Org/p3-template` as a starting point, providing a structured foundation for deployment and configuration.
    - All code was put in `run.py` and all libraries was installed and listed in `requirements.txt`.
  - In Heroku a app was created.
    - Added Config var `PORT`with value `8000`.
    - Connected my Github account to Heroku and serched for `project_3`.
    - Did a manual deployment of the project and the app was built.

Here are a link to the game, enjoy! [Battleship](https://battleship-version1-1fd9e9cf7970.herokuapp.com/)

### Local Deployment

1. Clone the repository to your local machine:
  `git clone https://github.com/creanorcode/project_3`

2. Navigate to the project directory:
  `cd project_3`

3. Install the required dependencies:
  `pip install numpy rich`

4. Run the game:
  `python run.py`

## Credits
- In this section, we provide acknowledgments for resources and inspiration.

### Content
- Game rules inspired by the traditional **Battleship** board game.
- Boundary check improvements and enhanced visuals were added based on user feedback.
- Libraries, NumPy and Rich
- Coe Institute template [Code-Institute-Org/p3-template](https://github.com/Code-Institute-Org/p3-template)

### Media
- The logo-picture in the beginning of this README.md-file was created by a AI service.

## Acknowledgments
- Special thanks to the creators of NumPy and Rich for making terminal-based games more efficient and visually engaging.
- Inspiration for structuring this README was drawn from [README.template from Code Institute](https://github.com/Code-Institute-Solutions/readme-template).


Enjoy the game and sink some ships!
