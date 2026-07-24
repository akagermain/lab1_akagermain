#!/bin/bash

# This file archives the current grades.csv into a timestamped copy inside archive directory to be created
# Again, it resets grades.csv to a fresh file, and logs every run to organizer.log

ARCHIVE_DIR="archive"
LOG_FILE="organizer.log"
SOURCE_FILE="grades.csv"

# 1. Make sure the archive directory exists
if [ ! -d "$ARCHIVE_DIR" ]; then
    mkdir "$ARCHIVE_DIR"
    echo "Created archive directory: $ARCHIVE_DIR"
fi

# 2. Make sure there is actually a grades.csv to archive
if [ ! -f "$SOURCE_FILE" ]; then
    echo "Error: '$SOURCE_FILE' not found. Nothing to archive."
    exit 1
fi

# 3. Build a timestamp, e.g. 20260722-143205
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# 4. Build the new archived filename
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"

# 5. Move the file into archive/ under its new timestamped name
mv "$SOURCE_FILE" "$ARCHIVE_DIR/$ARCHIVED_NAME"

# 6. Reset the workspace with a fresh, empty grades.csv
touch "$SOURCE_FILE"
