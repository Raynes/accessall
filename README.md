# accessall

This is a little tool for doing things with google music from your command
line. It currently supports downloading songs and exporting libraries.

## Usage

You can use `pip` to install accessall!

```
[sudo] pip install accessall
```

`easy_install` should also work.

### export

```
accessall export youremail@you.tld
```

It will prompt you for your password and then start dumping to `export.json`.

### download

```
accessall download 'Coldplay' 'Mylo Xyloto' 'Paradise'
```

The arguments are artist, album, and song in order. This one doesn't take an
email address because it requires oauth. It'll prompt you with a link where you
authorize it and get a code. This code will be stored in `~/.accessall` and
reused on later runs

## TODO

* uploading
