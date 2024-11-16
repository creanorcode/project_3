[![Battleship-logga1.webp](https://i.postimg.cc/5tzM1x5j/Battleship-logga1.webp)](https://postimg.cc/nsnWGfPt)

# Welcome to Battleship

Battleship is a terminal-based implementation of the classic game of strategy and skill. The project is designed for players who enjoy turn-based games and want a fun, interactive challenge. 

This implementation of Battleship allows players to customize their game setup, including board size and number of ships. It uses Python libraries **NumPy** and **Rich** to enhance performance and improve the user experience with efficient board management and colorful terminal output.

## Features

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








- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
