# Network Traffic Analysis

This project analyzes network traffic for anomalies and suspicious activities using open-source tools.

## Tools Used

- **Ubuntu**:  Or any Debian-based distribution.
- **Python**: For log parsing and analysis.
- **VirtualBox**: For running the virtual machine.
- **TShark**: Command-line version of Wireshark.
- **Zeek**: For network traffic analysis.

## Installation

### Install Required Tools and Dependencies

1. Install Tshark
2. Install zeek
3. Install python dependies
4. 
Update the package list and install necessary packages:

```bash
sudo apt update
sudo apt install -y tshark zeek python3-venv python3-pip
```

## Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/NetworkTrafficAnalysis.git
cd NetworkTrafficAnalysis
```

## Capturing Network Traffic

Capture network traffic using `tshark` and save it to a file:

```bash
sudo tshark -i lo -w captures/network_traffic.pcap
```
- `i lo`: Capture on the loopback interface
- `w captures/network_traffic.pcap`: Write the captured packets to a file

## Analyzing Logs

### Run Zeek on the Capture File

Analyze the captured network traffic using `Zeek`:

```bash
zeek -r captures/network_traffic.pcap
```

This generates various log files, including `conn.log`.

### Analyze the Logs Using Python Script

Run the analysis script to detect anomalies:

```bash
python scripts/analyze_logs.py
```

## Results

Check the `analysis/` directory for the results of the analysis.

## File Structure
```
NetworkTrafficAnalysis/
├── analysis/                  # Directory for analysis results
│   └── anomalies.csv          # Anomalies detected in the logs
├── captures/                  # Directory for captured network traffic
│   └── network_traffic.pcap   # Captured network traffic file
├── scripts/                   # Directory for analysis scripts
│   └── analyze_logs.py        # Python script to analyze logs
└── README.md                  # Project documentation
```

## Troubleshooting


