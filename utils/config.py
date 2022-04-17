import json
import traceback


def load(filename: str = "config.json"):
    with open(filename, "r", encoding="utf-8") as data:
        return json.load(data)


def trace_back(err, advance: bool = True):
    """debug your code anywhere"""
    _traceback = "".join(traceback.format_tb(err.__traceback__))
    error = "```py\n{1}{0}: {2}\n```".format(type(err).__name__, _traceback, err)
    return error if advance else f"{type(err).__name__}: {err}"
