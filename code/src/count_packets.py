import pyshark

CAPTURE_FILENAME = '/home/carl/Code/Network/pcap/http.pcap'

packets_array = []

def counter(*args):
    packets_array.append(args[0])
 
def count_packets():
    cap = pyshark.FileCapture(CAPTURE_FILENAME, keep_packets=False)
    cap.apply_on_packets(counter, timeout=10000)
    return len(packets_array)

print("Packets number:"+str(count_packets()))