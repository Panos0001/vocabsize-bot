# VocabSize

This script automates the process of solving the [VocabSize website](https://vocabsize.xeersoft.co.th/) assignments. It uses the Caesar Cipher method to decrypt the text and then inputs the answer into the website.

## Prerequisites

Before running the script, you need to have the following installed:
- [Python 3](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installing/)

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/<Panos0001>/<vocabsize-bot>.git
    ```
2. Install the required packages:
    ```
    pip install selenium
    ```
3. Download the [ChromeDriver](https://sites.google.com/chromium.org/driver/) for your version of Google Chrome.
4. Extract the `chromedriver.exe` file and place it in the root directory of the repository.

## Usage

1. Run the script:
    ```
    python main.py
    ```
2. Enter your VocabSize login credentials when prompted.
3. Wait for the script to assign you work.
4. Enter the amount of words in the vocabulary list.
5. Wait for the script to solve each word and input the answer.
6. Repeat steps 3-5 until you have completed all your assigned work.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
