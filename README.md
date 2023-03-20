# Dice Game (ひとりすごろく)

[![Stars](https://img.shields.io/github/stars/chouusin/DiceGame.svg?logo=github)](https://github.com/chouusin/DiceGame)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/chouusin/DiceGame/actions/workflows/ci.yml/badge.svg)](https://github.com/chouusin/DiceGame/actions/workflows/ci.yml)
[![codecov](https://codecov.io/github/chouusin/DiceGame/branch/main/graph/badge.svg?token=tkq655ROg3)](https://app.codecov.io/github/chouusin/DiceGame)

このページをご覧いただき、ありがとうございます。

This project is only for demonstration purpose. Please do not use it for anything else.

## TL;DR

There is an all in one python file for this whole project located at `Scripts/dicegame.py` so that you don'tneed to go through the package setup process.

```
cd Scripts
python dicegame.py
```

## Installation

This project runs on Python `3.7+`. It requires no external dependencies.

### 1. cloning the project

```
git clone https://github.com/chouusin/DiceGame
cd DiceGame
```

### 2. Setup virtual environment (recommended)

By setting up a virtual environment, it could help avoid permission issues while installing

2.1 Using python3 built-in module to initilize the vitrual environment

```
python -m venv venv
```

2.2 Activate the virtual environment

-   Linux

    -   `bash`
        ```
        source venv/bin/activate
        ```

-   Windows

    -   `Bash on Windows`

        ```
        source venv/Scripts/activate
        ```

    -   `Command Prompt`

        ```
        Call venv\Scripts\activate.bat
        ```

### 3. Install the package

```
pip install .
```

Or the following to install as user site package if permission issues occurred

```
pip install . --user
```

## Usage

After successfully installing the package. The command line interface can be accessed by

### 1. Command

```
dicegame
```

### 2. Python module

```
python -m dicegame
```

Or the following if you installed the package as user site package.

```
python -m dicegame --user-site
```

### 3. Python code

```python
from dicegame.cmdline import main

main()
```

Thank you for taking the time to review my project.
If you have any feedback or questions, please don't hesitate to contact me.

最後までご覧いただきありがとうございました。
もし何かご質問やご意見がありましたら、お気軽にご連絡ください。
