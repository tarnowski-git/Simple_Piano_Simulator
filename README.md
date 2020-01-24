# Simple Piano Simulator

Desktop GUI Piano application with Pyhon using Tkinter graphics module and PyGame library for loading and playing sounds.

## Demo

![piano](https://user-images.githubusercontent.com/34337622/73108270-2023fa00-3f00-11ea-8c38-abf29b89640c.gif)

## Technologies

-   Python 3.7
-   Tkinter module

## Prerequisites

-   [Python](https://www.python.org/downloads/)
-   [pip](https://pip.pypa.io/en/stable/installing/)
-   [pipenv](https://pipenv.readthedocs.io/en/latest/install/#make-sure-you-ve-got-python-pip)

## Installation

-   [Clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) this repo to your local machine using:

```
$ git clone https://github.com/tarnowski-git/Simple_Piano_Simulator.git
```

-   Setup your [local environment](https://thoughtbot.com/blog/how-to-manage-your-python-projects-with-pipenv):

```
# Spawn a shell with the virtualenv activated
$ pipenv shell

# Install dependencies
$ pipenv install

# Run script into local environment
$ pipenv run python piano.py
```

-   Compile with Pyinstaller to exectutable file:

```
# Windows
pyinstaller --onefile --windowed piano.py
```

## Sources

This application is based on [DJ Oamen](https://www.youtube.com/watch?v=CoZSEId-wNA) Tutorial.

## License

This project is licensed under the terms of the [**MIT**](https://github.com/tarnowski-git/Simple_Piano_Simulator/blob/master/LICENSE) license.
