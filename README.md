# fliendly_python_server

A Python client/server application.

Client sends a timezone to the server that returns the date and time of it.

Client's conection is persistent, it means you can send multiple (non-parallel) timezones.

If you type 'close' the server closes the conection with the current client and wait for another one.

That's it! :)
