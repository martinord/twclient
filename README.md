# Twisted Web Client
## Intro
An implementation of a web client using the [Twisted Framework](https://twistedmatrix.com/trac/) for network application development.

Twisted is an event-driven framework for Python. It uses a `reactor` event loop as the main part, waiting for events to occur.

## Usage

```bash
python twclient.py <command> <url>
```

**Commands:**
* `cat`: Shows the source of the page in the standard output
* `download`: Downloads the source of the page in a temporary file and shows the path


## Packages used
* twisted
* pyopenssl
* crypto


## Licence

Source code can be found on [github](https://github.com/martinord/twclient), licenced under [GPL-3.0](https://opensource.org/licenses/GPL-3.0).

Developed by [Martiño Rivera](https://github.com/martinord)
