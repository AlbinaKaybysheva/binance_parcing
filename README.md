# Main Info
This program reads current price of XRP/USDT futures on Binance in real time.
If the price has fallen by 1% of the maximum price of the last hour, program display a message in the console.
In this case, the program continues to work, constantly reading the current price.

# Technologies
The program is using websockets and Binance API to get real-time futures price.

# Setup
1. Clone this repo, switch to dev branch, pull changes.

2. Create a virtual environment. To do that, run the command:

python -m venv .venv   # windows
python3 -m venv .venv  # linux or macos

3. Then activate your venv:

.venv\Scripts\activate.bat  # windows
source .venv/bin/activate   # linux or macos

4. Install all required libraries:
pip install - r requirements.txt
