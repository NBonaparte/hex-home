#!/usr/bin/env python3
import toml
import jinja2

config = toml.load("config.toml")

links = sorted(
    [
        {
            "name": name,
            "url": item["url"],
            "icon": f"icons/{name}.svg",
            "color": item["color"] if "color" in item else "",
        }
        for name, item in config["links"].items()
    ],
    key=lambda x: x["name"],
)

loader = jinja2.FileSystemLoader(searchpath=".")
env = jinja2.Environment(loader=loader)
tmpl = env.get_template("template.html")
tmpl.stream(links=links).dump("index.html")
