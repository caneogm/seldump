#!/usr/bin/env python3

import json
from seldump import Seldump

import argparse


"""
Example: simple command parser
"""

def ParseCommands(seldump_instance, filename):
	with open(filename, "r") as file:
		data = json.load(file)

	commands = data["commands"]
	for command in commands:
		xpath = command.get("xpath", None)
		timeout = command.get("timeout", None)
		text = command.get("text", None)
		url = command.get("url", None)

		match command["command"]:
			case "wait":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				seldump_instance.command_wait(
					xpath=xpath,
					timeout=timeout
				)

			case "click":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				seldump_instance.command_click(
					xpath=xpath,
					timeout=timeout
				)

			case "sendkeys":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				if text is None:
					raise ValueError("text cannot be none")
				seldump_instance.command_sendkeys(
					text=text,
					xpath=xpath,
					timeout=timeout
				)

			case "get":
				if url is None:
					raise ValueError("url cannot be none")
				seldump_instance.command_get(
					url=url
				)

			case "dumpxpath":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				seldump_instance.command_dumpxpath(
					xpath=xpath
				)

			case "dump":
				seldump_instance.command_dump()

			case "try-wait":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				seldump_instance.command_try_wait(
					xpath=xpath,
					timeout=timeout
				)

			case "try-click":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				seldump_instance.command_try_click(
					xpath=xpath,
					timeout=timeout
				)

			case "try-sendkeys":
				if xpath is None:
					raise ValueError("xpath cannot be none")
				if text is None:
					raise ValueError("text cannot be none")
				seldump_instance.command_try_sendkeys(
					text=text,
					xpath=xpath,
					timeout=timeout
				)

			case _:
				print(f"Unknown command: {command['command']}")


def main():
	parser = argparse.ArgumentParser(description="seldump does shit and then dumps")

	parser.add_argument('-u', '--url', type=str, help="starting point", required=False)
	parser.add_argument('-s', '--script', type=str, help="json script", required=False)

	args = parser.parse_args()


	seldump_instance = Seldump()
	if args.url:
		seldump_instance.command_get(args.url)

	if args.script:
		ParseCommands(seldump_instance, args.script)


if __name__ == "__main__":
    main()
