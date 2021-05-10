# Solution - The Case of the 50ms request

A common problem that can occur while using TCP is a ~40ms latency problem caused by the combination of Nagle's algorithm and TCP delayed acknowledgment used by the Linux kernel.

## Possible solutions

### Disabling Nagle's algorithm

In nodejs you can disable Nagle's algorithm using the following command,

```javascript
req.setNoDelay(true);
```

### Disabling delayed ACKs

In the `server.py` you can see the socket option,

```python
setsockopt(socket.IPPROTO_TCP, socket.TCP_QUICKACK, 0)
```

to disable delayed ACKs by setting this option to 1, but notice that this can be changed by the protocol level implementation (see `man 7 tcp`).

### Not splitting the POST request

In `slow.js` one can notice that the following line,

```javascript
req.flushHeaders();
```

this forces the headers of the POST request without the data and only after sending the data. Removing this line will make the request sent in one packet preventing this bug.
