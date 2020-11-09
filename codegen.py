from grpc.tools import protoc
proto_files = [
  "./src/proto/date.proto", 
  "./src/proto/person.proto"
]

proto_files_service = [
  "./src/proto/person_service.proto"]

for file in proto_files:
  protoc.main([
          '',
          '-I=src/proto',
          '--python_out=src/generated',
          file
  ])

for file in proto_files_service:
  protoc.main([
          '',
          '-I=src/proto',
          '--python_out=src/generated',
          '--grpc_python_out=src/generated',
          file
  ])

#Note: After code gen, module adjustment required. import generated. Solution for that?