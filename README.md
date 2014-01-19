# accessall

This is a little tool for exporting your Google Music (All Access or otherwise)
library. It is written in Python and creates a file called `export.json`
containing a line delimited sequence of json hashes of song info.

## Usage

For some reason, `pip` on my machine seems to explode when trying to install one
of accessall's dependencies, gmusicapi, but easy_install works
fine. Nonetheless, you're welcome to give it a shot:

```
[sudo] pip install accessall
```

If that doesn't work, use `easy_install`.

Once you've got it installed you should have an executable, `accessall`. Just
run it like so:

```
accessall youremail@you.tld
```

It will prompt you for your password and then start dumping to `export.json`.
