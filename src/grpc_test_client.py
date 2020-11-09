import logging
import sys
import argparse
import grpc
import logging

from generated import person_service_pb2, person_service_pb2_grpc

logger = logging.getLogger('grpc')
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

def run(host, port):
  channel = grpc.insecure_channel('%s:%d' % (host, port))
  stub = person_service_pb2_grpc.PersonServiceStub(channel)
  response = stub.SearchPerson(person_service_pb2.SearchPersonRequest(name_contains='man'))
  logger.info(response.persons)

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--host', help='server host name',
                      default='localhost',
                      type=str)
  parser.add_argument('--port', help='server port number',
                      default=50051,
                      type=int)
  args = parser.parse_args()
  run(args.host, args.port)