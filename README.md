Chamomile
=========
A small script to help you sleep
--------------------------------
Chamomile is a small, console-based Python script that tells you when you should go to sleep and/or when you should wake up. 

It owes a great debt to [David Shaw's][] [sleepyti.me][] project.


Usage
-----

    chamomile.py [-h] [-v] [-c MINS] [-d MINS] [-w TIME | BEDTIME]

If you just run `$ chamomile.py` with no arguments, it tells you when you should wake up if you were to go to bed immediately.

If you pass Chamomile a time in HH:MM (24-hour) format, e.g. `$ chamomile.py 10:00` it assumes you want to wake up at that time and tells you when you should go to bed. 

However, if you use the `-w` or `--wakeup` flag before entering a time, Chamomile will assume you want to go to sleep at that time, and will tell you when to wake up.

The `-c` or `--cycle` flag allows you to specify in minutes the length of the sleep cycle (default=90).

The `-d` or `--delay` flag likewise lets you specify in minutes how long it takes you to fall asleep (default=14).

The remaining flags, `-h`/`--help` and `-v`/`--version` output a detailed help message and version information, respectively.


Todo
-------
* Improve documentation
* Allow for configuration files (using configparser?)
* Allow for inputting times in more flexible formats (incl. 12 hour)


License
-------
Chamomile uses the [ISC License][]. 
See `LICENSE` for the actual contents.


<!-- Links -->
[David Shaw's]: http://dshaw.net/ "David Shaw's personal website"
[sleepyti.me]: http://sleepyti.me/ "Sleepyti.me bedtime calculator"
[ISC License]: https://en.wikipedia.org/wiki/ISC_license "Wikipedia page for the ISC License"
