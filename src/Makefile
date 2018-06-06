# Compile proto definitions.
system_pb2.py system_pb2_grpc.py : protos/system.proto
	python -m grpc_tools.protoc -Iprotos --python_out=. --grpc_python_out=. protos/system.proto

# Cleanup generated servicer files.
clean:
	rm system_pb2.py
	rm system_pb2_grpc.py
