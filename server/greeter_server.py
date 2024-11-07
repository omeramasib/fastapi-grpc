# server/greeter_server.py
from concurrent import futures
import grpc
import grpc_generated.service_pb2 as service_pb2
import grpc_generated.service_pb2_grpc as service_pb2_grpc

# Implement the Greeter Service
class Greeter(service_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        # Business logic for greeting
        return service_pb2.HelloReply(message=f"Hello, {request.name}!")

# gRPC server function
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started on port 50051")
    server.wait_for_termination()