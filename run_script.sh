#!/usr/bin/bash

# Find the repository directory dynamically
REPO_NAME="ci-cd-html-project"
REPO_PATH=$(find ~ -type d -name "$REPO_NAME" 2>/dev/null | head -n 1)

# Check if the repo was found
if [ -z "$REPO_PATH" ]; then
    echo "❌ Error: Repository '$REPO_NAME' not found. Exiting."
    exit 1
fi

echo "✅ Repository found at: $REPO_PATH"

# Define source and destination paths
SRC_FILE="$REPO_PATH/index.html"
DEST_FILE="/var/www/html/index.html"

# Ensure the repository directory exists
if [ ! -d "$REPO_PATH" ]; then
    echo "❌ Error: Repository directory $REPO_PATH does not exist. Exiting."
    exit 1
fi

# Ensure the source file exists
if [ ! -f "$SRC_FILE" ]; then
    echo "❌ Error: Source file $SRC_FILE does not exist. Exiting."
    exit 1
fi

# Backup the existing file in /var/www/html (if it exists)
if [ -f "$DEST_FILE" ]; then
    echo "🛠 Backing up existing index.html to index.html.bak"
    mv "$DEST_FILE" "${DEST_FILE}.bak"
fi

# Copy the new file to the web directory
cp "$SRC_FILE" "$DEST_FILE"

# Verify the copy operation
if [ $? -eq 0 ]; then
    echo "✅ index.html has been successfully replaced."
else
    echo "❌ Failed to replace index.html."
    exit 1
fi
