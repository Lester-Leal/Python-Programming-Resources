# IMPORTANT: pip install tinytag
# Scans the current working directory for audio files, extracts the artist and album metadata from each file,
# creates folders based on the metadata, and moves the files into the respective folders.
# This helps in organizing the audio files by artist and album.
# This code assumes that the audio file has embedded metadata in it.

# NOTE: Optimized for windows only, but still can use in unix
# UNSUPPORTED: '.wav'

# Author: Jorn Blaedel Garbosa

import os
import shutil
from tinytag import TinyTag
import re

# Current directory as the source directory
source_directory = os.getcwd()

# Function to sanitize and capitalize folder names


def sanitize_and_capitalize_folder_name(name):
    # Remove characters not allowed in Windows file names
    sanitized_name = re.sub(r'[<>:"/\\|?*]', "", name)

    # Split the name into words and capitalize words outside parentheses or brackets
    words = sanitized_name.split()
    capitalized_words = []
    capitalize_next_word = True

    for word in words:
        if '(' in word or '[' in word:
            capitalize_next_word = False

        if capitalize_next_word:
            word = word.capitalize()

        capitalized_words.append(word)

        if ')' in word or ']' in word:
            capitalize_next_word = True

    capitalized_name = ' '.join(capitalized_words)
    return capitalized_name.strip()


# Iterate over each file in the source directory
for file_name in os.listdir(source_directory):
    file_path = os.path.join(source_directory, file_name)

    # Check if the file is an audio file using tinytag
    if os.path.isfile(file_path) and TinyTag.is_supported(file_path):
        audio = TinyTag.get(file_path)

        # Extract the artist and album from the audio file's metadata
        artist = audio.artist
        album = audio.album

        # Skip the file if artist or album metadata is missing
        if not artist or not album:
            print(
                f"Skipping file: {file_name} (Missing artist or album metadata)")
            continue

        # If the artist field contains multiple artists separated by a delimiter, select the first artist
        artist = artist.split('/')[0]

    else:
        continue

    # Format and sanitize the folder names as artist and album, and capitalize them
    artist_folder_name = sanitize_and_capitalize_folder_name(artist)
    album_folder_name = sanitize_and_capitalize_folder_name(album)

    # Create the artist folder if it doesn't exist
    artist_folder = os.path.join(source_directory, artist_folder_name)
    if not os.path.exists(artist_folder):
        os.makedirs(artist_folder)
        print(f"Created folder: {artist_folder_name}")

    # Create the album folder inside the artist folder if it doesn't exist
    album_folder = os.path.join(artist_folder, album_folder_name)
    if not os.path.exists(album_folder):
        os.makedirs(album_folder)
        print(f"Created folder: {album_folder_name}")

    # Move the file to the album folder
    destination_path = os.path.join(album_folder, file_name)
    shutil.move(file_path, destination_path)
    print(
        f"Moved file: {file_name} to {os.path.join(artist_folder_name, album_folder_name)}")
