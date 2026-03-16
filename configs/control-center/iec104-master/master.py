import time
import c104

RTU_IP = "172.16.1.100"
RTU_PORT = 2404
CA = 47
IOA_MEAS = 11

client = c104.Client(tick_rate_ms=1000, command_timeout_ms=5000)
conn = client.add_connection(ip=RTU_IP, port=RTU_PORT, init=c104.Init.INTERROGATION)
station = conn.add_station(common_address=CA)

point = station.add_point(
    io_address=IOA_MEAS,
    type=c104.Type.M_ME_NC_1,
)

def on_state_change(connection: c104.Connection, state: c104.ConnectionState) -> None:
    print(f"STATE -> {state}")

conn.on_state_change(on_state_change)

client.start()
time.sleep(3)

ok = conn.interrogation(common_address=CA)
print(f"GI sent: {ok}")

while True:
    print(f"value={point.value}")
    time.sleep(5)
