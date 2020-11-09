import logging
import sys
from concurrent import futures
import grpc
from person_service import PersonService
from generated import person_service_pb2_grpc

logger = logging.getLogger('grpc')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_service_pb2_grpc.add_PersonServiceServicer_to_server(PersonService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logger.info(f"Server started at port 50051")
    server.wait_for_termination()
    

if __name__ == '__main__':
    #print('in main')
    serve()