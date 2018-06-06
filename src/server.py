from concurrent import futures

import grpc
import logging
import sys
import time

import config
import system_pb2
import system_pb2_grpc


class Server(system_pb2_grpc.ServerServicer):

    def __init__(self, id, port):
        self.id = id
        self.port = port

    def Greet(self, request, context):
        logging.info("Message: %s from %s.", request.message, request.sender)
        return system_pb2.Greeting()


def main():
    server_id = sys.argv[1]
    server_port = sys.argv[2]

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    system_pb2_grpc.add_ServerServicer_to_server(
        Server(server_id, server_port), server
    )

    port_address = "{}:{}".format(config.DEFAULT_HOST, server_port)
    server.add_insecure_port(port_address)

    server.start()
    logging.info("Server %s is listening at port %s.", server_id, server_port)

    try:
        while True:
            time.sleep(config.ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


main()