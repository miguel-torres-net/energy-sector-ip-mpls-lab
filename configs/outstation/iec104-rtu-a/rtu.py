import time
import c104

SERVER_IP = "0.0.0.0"
SERVER_PORT = 2404
CA = 47
IOA_MEAS = 11

server = c104.Server(ip=SERVER_IP, port=SERVER_PORT)
station = server.add_station(common_address=CA)

point = station.add_point(
    io_address=IOA_MEAS,
    type=c104.Type.M_ME_NC_1,
    report_ms=0,
)

point.value = 42.0

server.start()
print(f"RTU listening on {SERVER_IP}:{SERVER_PORT} CA={CA} IOA={IOA_MEAS}")

while True:
    time.sleep(1)
