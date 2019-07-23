[![made-with-python](https://img.shields.io/badge/made%20with-python-blue.svg)](https://www.python.org/)
# py-trains
A python program that scrapes data from [railyatri.in](https://www.railyatri.in/train-ticket) to find trains for a given source and destination on a given date.

## Installation
To run py-trains, you will need python3 and some additional packages.
To install those packages, simply use the following command:

```$ pip3 install -r requirements.txt```

## Usage
You need to pass arguments using the CLI itself to use py-trains

e.g. To get trains from Mumbai Bandra Terminus to Pune Junction on 22nd December, 2019:

```$ python3 trains.py BDTS PUNE 22 12 2019```
