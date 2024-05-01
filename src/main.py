# import connection scripts
from utils.connections.get_addresses   import retrieve as retrieve_addresses
from utils.connections.get_application import retrieve as retrieve_application

# import necessary modules
import keyboard  
import threading 
from scapy.all import sniff, IP, TCP, Raw, send


# https://github.com/ceccopierangiolieugenio/pyTermTk

'''
    Capture class
'''
class Capture():
    def __init__(self):
        # initialize the host and port to filter packets 
        self.port   = 0        
        self.host   = '' 
        self.client = ''
        self.configure()
        
        # packet translation structures
        self.structures = {
            'message'  : b'\x04A\x00', # avatar message
            'movement' : b'flatctrl',  # avatar movement
        }
        
    # ==============================================
    #        Setup application port and host
    # ==============================================        
    def configure(self):
        _info = retrieve_application()[0]
        ip_port_segment = _info.split('->')[-1].strip()
        self.host =  ip_port_segment.split(':')[0].strip()
        self.port =  int(ip_port_segment.split(':')[1].replace("(ESTABLISHED)", ""))
        
    # ==============================================
    #              Initialize Capture
    # ==============================================
    def start_capture(self):
        # Capturing IP packets on the specified interface
        sniff(filter="ip", prn=self.capture, iface="enp3s0")

    # ==============================================
    #          Capture and process packets
    # ==============================================
    def capture(self, packet):
        # check if the packet contains IP and TCP layers
        if IP in packet and TCP in packet:
            
            # extract source and destination IP addresses
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            
            # set client IP if not already set
            if self.client == '' and src_ip.startswith('192'):
                self.client = src_ip
            
            # only process packets from client/server
            if src_ip != self.host and src_ip != self.client:
                return
            
            # packet information
            self.info = {
                'src_ip'    : src_ip,
                'dst_ip'    : dst_ip,
                'src_port'  : packet[TCP].sport,
                'dst_port'  : packet[TCP].dport,
                'packet'    : bytes(packet[Raw].load) if packet.haslayer(Raw) else None,
                'direction' : "Incoming" if src_ip == self.host else "Outgoing"
            } 
        
            # check if packet exists and is not empty
            if self.info['packet'] is not None:
                # check if message packet
                if self.structures['message'] in self.info['packet']:
                    # send test packet
                    self.send_packet()
                
                # print packet information with appropriate direction
                print(f"{self.info['direction']} packet:")
                print(f"Packet: {self.info['packet']}\n")


# Entry point
if __name__ == "__main__":
    # Create an instance of the Capture class
    sniffer = Capture()

    # Start capturing packets
    sniffer.start_capture()