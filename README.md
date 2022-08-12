[![price-predictor PyPI Project Page](https://img.shields.io/pypi/v/price-predictor.svg)](https://pypi.org/project/price-predictor/)
[![MIT License](https://img.shields.io/github/license/ludovicolemma/price-predictor.svg)](https://github.com/ludovicolemma/price-predictor/blob/main/LICENSE)
![Supported Python Versions](https://img.shields.io/pypi/pyversions/price-predictor.svg)

Quickly predict the future prices of financial instruments with a customizable LSTM Recurrent Neural Network

**Price-Predictor**

- You need only a **valid yahoo finance** symbol like:
"[EURUSD=X](https://it.finance.yahoo.com/quote/EURUSD=X?p=EURUSD=X)", 
"[^DJI](https://it.finance.yahoo.com/quote/^DJI?p=^DJI)" or 
"[AMZN](https://it.finance.yahoo.com/quote/AMZN?p=AMZN)"

- Download temporarily the financial data from the optionally 
specified date (if not specified it starts from july 2010)

- A LSTM RNN will be trained and it will **automatically predict** 
the next **opening price** of the instrument

## Installation

With Python and Pip installed, do:

```sh
pip3 install price-predictor
```

Wait for the dependencies to be installed, tensorflow may need a few minutes.

## Usage

**Command-line**
Just write the command from your shell
```sh
price_predictor
```

**Python Library**
```sh
from price_predictor import price_predictor as pp
```
Then you can use the same function as in the command line and a few more tools.


## Disclaimer

I am in no way affiliated with, authorized, maintained or
endorsed by Yahoo Finance or any of its affiliates or subsidiaries. This is
an independent and unofficial project.

It is licensed under an MIT license. Refer to the `LICENSE` file
for more information.
