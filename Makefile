# create a binary
SCRIPT_NAME=seldump

ENTRY_FILE=parser.py
BUILD_DIR=dist

build:
	@echo "Building the executable..."
	pyinstaller --onefile $(ENTRY_FILE) --name $(SCRIPT_NAME)

clean:
	@echo "Cleaning up..."
	rm -rf __pycache__ build $(BUILD_DIR) *.spec

