from generated import person_service_pb2_grpc, person_service_pb2, person_pb2

class PersonService(person_service_pb2_grpc.PersonServiceServicer):
    def SearchPerson(self, request, context):
      person_list = []
      person_list.append(person_pb2.Person(first_name='Joe', last_name='Costa', gender=1))
      person_list.append(person_pb2.Person(first_name='Sara', last_name='John', gender=2))
      return person_service_pb2.SearchPersonResponse(
          success=True,
          message='',
          persons=person_list
        )
      #could use __setattr__