"""A tool for accessing stuff on google music!

Usage:
  accessall export USER
  accessall download ARTIST ALBUM SONG
  accessall --version | -v
  accessall --help | -h

Options:
  --version, -v    Show version.
  --help

"""
from __future__ import print_function
import os.path
import json
from docopt import docopt
from getpass import getpass
from gmusicapi.clients import Mobileclient, Musicmanager


def select_keys(d, keys):
    """Return a dict that is a subset of d with only
    the keys specified. Any keys that do not exist in
    d are set to None in the returned dict.

    """
    return {key: d.get(key) for key in keys}


def login():
    """Login with oauth. This is required for Musicmanager."""
    manager = Musicmanager()
    path = os.path.expanduser('~/.accessall')
    if os.path.isfile(path):
        creds = path
    else:
        creds = manager.perform_oauth(storage_filepath=path)
    manager.login(oauth_credentials=creds)
    return manager


def exportlib(user, password):
    """Logs into Google Music and exports the user's
    library to a file called 'export.json'.

    """
    keys = ['comment', 'rating', 'composer', 'year', 'album',
            'albumArtist', 'title', 'totalDiscCount', 'trackNumber',
            'discNumber', 'totalTrackCount', 'estimatedSize',
            'beatsPerMinute', 'genre', 'playCount', 'artist',
            'durationMillis']

    client = Mobileclient()
    client.login(user, password)
    with open('export.json', 'w+') as out:
        for songs in client.get_all_songs(incremental=True):
            for song in songs:
                pruned = select_keys(song, keys)
                print(json.dumps(pruned), file=out)


def find_song(manager, song, artist, album):
    """Fetch the user's list of uploaded songs and
    find the one with song, artist, and album that
    matches the ones passed in. This function
    searches for the song incrementally and thus
    should be safe even for very large libraries.

    """
    for songs in manager.get_uploaded_songs(incremental=True):
        for songh in songs:
            match = (
                songh.get('title') == song
                and songh.get('artist') == artist
                and songh.get('album') == album
                )
            if match:
                return songh['id']


def download(manager, song, artist, album):
    """Find the song matching the song, artist,
    and album passed in. Download it to disk in
    the currently directory.

    """
    id = find_song(manager, song, artist, album)
    if id:
        name, stream = manager.download_song(id)
        print('Writing', name)
        with open(name, 'wb') as f:
            f.write(stream)
    else:
        print('Song not found.')


def main():
    """Program entry point."""
    args = docopt(__doc__, version='accessall 1.4')
    if args['export']:
        password = getpass('Password for Google Music: ')
        exportlib(args['USER'], password)
    elif args['download']:
        download(login(), args['SONG'], args['ARTIST'], args['ALBUM'])
