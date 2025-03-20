from scapy.all import sniff, IP

def process_packet(packet):
    if IP in packet:
        print(f"Packet: {packet[IP].src} -> {packet[IP].dst}")

sniff(prn=process_packet, store=False, iface="eth0")
