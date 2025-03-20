FROM python:3.10
WORKDIR /app
COPY scripts/ /app/
RUN pip install scapy
CMD ["python", "network_monitor.py"]
