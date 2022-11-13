<samp>
  <div style="align-items: center; justify-content: center;">
    ![icon](/space-invaders/graphics/red.png?raw=true "icon")
  <div>
  <h2>Summary</h2>
  <p>
    Piway's Game of Life is a <a href="https://www.raspberrypi.org/">Raspberry Pi</a>-developed cellular automaton <a href="https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life">Conway's Game of Life</a> style game made in <a href="https://www.python.org/">Python</a> using <a href="https://www.pygame.org/">pygame</a>. Therefore, graphics and visual resources are at their minimum, extracting the most performance from the computer.
  </p>
  <h2>Play</h2>

  ```bash
  # clone the game's repository
  $ git clone https://github.com/obielwb/space-invaders.git

  # cd into the game's directory
  $ cd space-invaders

  # create the game's virtual environment
  $ python -m venv venv

  # activate the game's virtual environment
  $ source ./venv/bin/activate
  # or
  $ ./venv/Scripts/activate.bat

  # install the game's required libraries
  $ pip install -r requirements.txt

  # launch the game
  $ python ./space-invaders/game.py
  ```
  <b>Note:</b> Python is <i>required</i> in order to run Piway's Game of Life.

  <h2>References</h2>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://www.pygame.org/">pygame</a></li>
    <li><a href="https://www.raspberrypi.org/">Raspberry Pi</a></li>
  </ul>
  </ul>
</samp>