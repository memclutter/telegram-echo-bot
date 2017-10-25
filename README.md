# Telegram Echo Bot

Example bot for Telegram.

## Preparing for launch

You will need either a locally installed `python3` or a `docker`.

## Launch Locally

For local launch, set all dependencies with `pip`. Make sure you are using `python` version `3`.

To avoid clogging your system, use venv.

```bash
# virtual environment
python3 -m venv .venv
source .venv/bin/activate

# python dependencies
pip install --upgrade pip
pip install -r requirements.txt

# run bot
python main.py
```

## Launch in Docker

First you need to build the image. Then, using this image, start the container. That's all it takes.

```bash
docker build -t username/botname .
docker run --rm -t username/botnane
```
