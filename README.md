# accessall

This is a little tool for exporting your Google Music (All Access or otherwise)
library. It is written in Python and creates a file called `export.json`
containing a line delimited sequence of json hashes of song info.

## Usage

You can use `pip` to install accessall!

```
[sudo] pip install accessall
```

`easy_install` should also work.

Once you've got it installed you should have an executable, `accessall`. Just
run it like so:

```
accessall youremail@you.tld
```

It will prompt you for your password and then start dumping to `export.json`.
