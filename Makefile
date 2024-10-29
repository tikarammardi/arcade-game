# Set the executable name and source files
EXECUTABLE_NAME = ArcadeGame
SOURCE_FILE = app/game.py
ASSET_DIRS = app/images app/sounds

# Default target
all: clean build

# Clean up previous builds
clean:
	@echo "Cleaning up previous builds..."
	rm -rf build/ dist/ $(EXECUTABLE_NAME).spec

# Build the executable with pyinstaller, including asset directories
build:
	@echo "Building the executable..."
	poetry run pyinstaller --onefile --name $(EXECUTABLE_NAME) \
		$(foreach dir, $(ASSET_DIRS), --add-data "$(dir):$(notdir $(dir))") \
		$(SOURCE_FILE)

# Help command
help:
	@echo "Makefile targets:"
	@echo "  all      - Cleans up and builds the executable."
	@echo "  clean    - Removes previous builds."
	@echo "  build    - Builds the executable including assets."
	@echo "  help     - Shows this help message."

.PHONY: all clean build help
