# slack
Slack module for Python

## Install

```bash
pip3 install git+https://github.com/yumaeda/slack.git
```

## Usage

```python
from slack.slack import Slack

# CONSTANTS
API_TOKEN = 'xxxxxxxxxxxx'
CHANNEL   = 'channel1'
FILE      = './customer.xlsx'    
COMMENT   = 'Hello World!'

slack = Slack(API_TOKEN)
slack.send_file(
    channel=CHANNEL,
    file=FILE,
    comment=COMMENT
)
```

## Pylint

```bash
pip3 install pylint
pylint slack/*.py
```

