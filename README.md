# distributed-system

This system (presently just an implementation for a simple, single server) uses gRPC for communication between servers.
It is written in Python 3.6.

You may install gRPC using:

```bash
$ pip install grpc
$ pip install grpcio
```

You may then build the system using:

```bash
$ cd src
$ make
```

You may now start a server. To run a server with id `1` listening at port `8080', you may use:

```bash
$ python server.py 1 8080
```

This uses the configured host, which is just `localhost` by default. 
As a result, another server may communicate with this server by creating
a communication channel with `localhost:8080`.

