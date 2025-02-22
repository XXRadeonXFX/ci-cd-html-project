#!/bin/bash

# Define source and destination paths
SRC_FILE="/var/www/html/index.html"
DEST_FILE="$(pwd)/index.html"

# Check if the source file exists
if [ ! -f "$SRC_FILE" ]; then
    echo "Source file $SRC_FILE does not exist. Exiting."
    exit 1
fi

# Backup the existing file in the current directory (if it exists)
if [ -f "$DEST_FILE" ]; then
    echo "Backing up existing index.html to index.html.bak"
    mv "$DEST_FILE" "${DEST_FILE}.bak"
fi

# Copy the new file from /var/www/html to the current directory
cp "$SRC_FILE" "$DEST_FILE"

# Verify the copy operation
if [ $? -eq 0 ]; then
    echo "index.html has been successfully replaced."
else
    echo "Failed to replace index.html."
    exit 1
fi
