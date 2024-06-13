# Network Traffic Analysis

This project provides a basic framework for capturing and analyzing network traffic to detect anomalies and suspicious activities. 

## Tools Used

- **Ubuntu**:  Or any Debian-based distribution.
- **TShark**: Command-line version of Wireshark.
- **Zeek**: For network traffic analysis.
- **Python**: For log parsing and analysis.

## Installation

### Install Required Tools and Dependencies

Install Tshark, Zeek, necessary Python libraries:

```bash
sudo apt update
sudo apt install wireshark
sudo apt install tshark
sudo apt install zeek
sudo apt install python3-venv
sudo apt install python3-pip
pip3 install pandas
```

Follow below installation page if you have trouble with installing Zeek. Ensure all the dependencies are installed.<br>
[Installing Zeek](https://docs.zeek.org/en/master/install.html).


## Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/MenakaGodakanda/NetworkTrafficAnalysis.git
cd NetworkTrafficAnalysis
```

## Capturing Network Traffic

Capture network traffic using `tshark` and save it to a file:

```bash
sudo tshark -i lo -w captures/network_traffic.pcap
```
- `i lo`: Capture on the loopback interface.
- `w captures/network_traffic.pcap`: Write the captured packets to a file


If capturing network traffic on `eth0`
```bash
sudo tshark -i eth0 -w captures/network_traffic.pcap
```

## Analyzing Logs

### Run Zeek on the Capture File

Analyze the captured network traffic using `Zeek`:

```bash
zeek -r captures/network_traffic.pcap
```

This generates various log files, including `conn.log`.
- `conn.log`: Information about network connections.
- `http.log`: Details of HTTP requests and responses.
- `dns.log`: Information about DNS queries and responses.

The generated log files, might look like this:<br>

![Screenshot 2024-06-11 135726](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/e60fb32c-332f-4b30-a9fe-33ead104832b)<br>


### Analyze the Logs Using Python Script

Run the analysis script to detect anomalies:

```bash
python3 scripts/analyze_logs.py
```

This script will read `conn.log`, identify anomalies, and save them in `analysis/anomalies.csv`.

Output from script:
<br>
![Screenshot 2024-06-11 175352](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/1a572c30-1e7a-432e-955b-774a6d6f3f7d)
<br>

## Results

Check the `analysis/` directory for the results of the analysis.<br><br>
![Screenshot 2024-06-11 175756](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/4cd08665-d21d-4409-8141-9e638aa2dbf1)
<br>

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

### Unable to Capture Network Traffic
The "Permission denied" error can occur because the captures directory does not have the appropriate permissions for TShark to write the output file. 
```
mcyber@mcyber-VirtualBox:~/NetworkTrafficAnalysis$ sudo tshark -i lo -w captures/network_traffic.pcap
Running as user "root" and group "root". This could be dangerous.
Capturing on 'Loopback: lo'
tshark: The file to which the capture would be saved ("captures/network_traffic.pcap") could not be opened: Permission denied.
```

You can fix this by adjusting the permissions of the `captures` directory or by running TShark with a different output path.

#### Method 1: Adjust Directory Permissions

Change permissions of the captures directory and retry capturing network traffic:
```
sudo chmod 777 captures
sudo tshark -i lo -w captures/network_traffic.pcap
```

Once the permissions are set correctly, TShark should be able to write the capture file to the captures directory without any issues.

#### Method 2: Run TShark with a Different Output Path

1. Run TShark with an output path that has appropriate permissions (e.g., `/tmp`):
```
sudo tshark -i lo -w /tmp/network_traffic.pcap
```

2. Move the captured file to the captures directory:
```
sudo mv /tmp/network_traffic.pcap captures/network_traffic.pcap
```

3. Verify the Capture File:
```
ls -l captures/network_traffic.pcap
```

### Zeek Installation

Sometimes, the `zeek` cannot properly installed in the system.

#### Ensure Dependencies
First, make sure you update the system and have the necessary dependencies:
```
sudo apt update
sudo apt install cmake make gcc g++ flex bison libpcap-dev libssl-dev python-dev swig zlib1g-dev
```

#### Method 1: Install from the Repository
Add Zeek Repository and Install:
```bash
curl -s https://download.opensuse.org/repositories/security:zeek/xUbuntu_20.04/Release.key | sudo apt-key add -
sudo sh -c "echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_20.04/ /' > /etc/apt/sources.list.d/security:zeek.list"
sudo apt update
sudo apt install zeek
```

#### Method 2: Install from the Source Code
1. Download the latest Zeek source code:
```
wget https://download.zeek.org/zeek-4.2.0.tar.gz
```

2. Extract the downloaded tarball:
```
tar -xvzf zeek-4.2.0.tar.gz
cd zeek-4.2.0
```

3. Build and install Zeek:
```
./configure
make
sudo make install
```

#### Method 3: Zeek Installation Script
```
curl -O https://raw.githubusercontent.com/zeek/zeekctl/master/scripts/install.sh
chmod +x install.sh
sudo ./install.sh
```

#### Verify the Installation
Ensure that Zeek is installed correctly by checking its version:
```
zeek --version
```

### Zeek Command Not Found
A error message can occur when executing `zeek -r captures/network_traffic.pcap` command.
```
mcyber@mcyber-VirtualBox:~/NetworkTrafficAnalysis$ zeek -r captures/network_traffic.pcap
Command 'zeek' not found, did you mean:
  command 'zerk' from deb gpsd-clients (3.25-2ubuntu2)
  command 'peek' from deb peek (1.5.1+git20230114-1)
Try: sudo apt install <deb name>
```
The error message indicates that the zeek command is not found, meaning Zeek (formerly known as Bro) is not properly installed on your system. Or 'zeek' is installed but not found.

#### Method 1: Troubleshoot Zeek Path Issues

If `Zeek` is installed but not found, ensure it is in your PATH:

1. Find the installation path:
```bash
sudo find / -name zeek
```

2. Add Zeek to PATH:
```bash
echo 'export PATH=/path/to/zeek/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

Replace /path/to/zeek with the actual path found in the previous step.


#### Method 2: Ensure Zeek Path

If you still encounter issues where `zeek` is not found, it could be due to the PATH not being updated correctly. Ensure that `/usr/local/zeek/bin` (or the actual installation path) is included in your PATH environment variable.

You can manually check if Zeek is in the expected location:

```bash
ls /usr/local/zeek/bin
```

You should see zeek listed in the output.


#### Method 3: Adding Zeek Path

Sometimes, Zeek is installed but is not in your system's PATH. Let's find where Zeek is installed and ensure it is correctly added to your PATH.

1. Locate Zeek
Search for the Zeek binary on your system:

```bash
sudo find / -name zeek 2>/dev/null
```

This command will search the entire file system for the `zeek` executable and should provide its location.

2. Add Zeek to Your PATH
Once you have the path to the Zeek binary, you need to add it to your PATH. Suppose the path is `/usr/local/zeek/bin`. Here’s how you can add it to your PATH:

- Open your bash configuration file:

```bash
nano ~/.bashrc
```

- Add the Zeek path:

Add the following line at the end of the file:
```bash
export PATH=/usr/local/zeek/bin:$PATH
```

Replace `/usr/local/zeek/bin` with the actual path you found.

- Save and close the file:

Press `CTRL + X`, then `Y`, and then `ENTER`.

- Reload your bash configuration:

```bash
source ~/.bashrc
```
<br>![Screenshot 2024-06-11 135605 - Copy](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/91923999-aeee-44cf-a725-c113d4a7b5a5)
<br>

### Permission Denied for Capture File

There can be permissions issue with the captures/network_traffic.pcap file. 

```
mcyber@mcyber-VirtualBox:~/NetworkTrafficAnalysis$ zeek -r captures/network_traffic.pcap
fatal error: problem with trace file captures/network_traffic.pcap (unable to open captures/network_traffic.pcap: Permission denied)
```

Let's fix the file permissions and then try running Zeek again.

#### Check and Set Permissions for the Capture File

1. Check the current permissions of the file:

```bash
ls -l captures/network_traffic.pcap
```

This will show the permissions of the file. If the permissions do not allow read access, we will need to change them.

2. Change the file permissions to ensure it is readable:

```bash
sudo chmod 644 captures/network_traffic.pcap
```

#### Verify the Permissions

Ensure that the permissions are correctly set:

```bash
ls -l captures/network_traffic.pcap
```

You should see something like this:
```
-rw-r--r-- 1 root root <size> <date> captures/network_traffic.pcap
```

This means the file is readable by everyone.<br>
![Screenshot 2024-06-11 135648 - Copy](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/cb326949-9d3a-476e-a90f-f549c06856ea)
<br>

#### Run Zeek Again

Now try running Zeek on the capture file again:

```bash
zeek -r captures/network_traffic.pcap
```

###  Pandas Module Not Found

The error can occur when the pandas library is not installed in your Python environment.

```
mcyber@mcyber-VirtualBox:~/NetworkTrafficAnalysis$ python3 scripts/analyze_logs.py
Traceback (most recent call last):
  File "/home/mcyber/NetworkTrafficAnalysis/scripts/analyze_logs.py", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

#### Install pip

You can install it using pip, the Python package installer. Let's go through the steps to install pandas.

1. Install pip (if not already installed)
First, make sure that `pip` is installed on your system. You can check this by running:

```bash
pip3 --version
```

If `pip3` is not installed, you can install it using:

```bash
sudo apt update
sudo apt install python3-pip
```

2. Install pandas

Use pip3 to install the pandas library:

```bash
pip3 install pandas
```

3. Verify the Installation

You can verify that pandas is installed correctly by starting a Python shell and importing pandas:

```bash
python3 -c "import pandas as pd; print(pd.__version__)"
```

4. Run the Analysis Script Again

Now, try running your analysis script again:

```bash
python3 scripts/analyze_logs.py
```

#### Create a Virtual Environment

Sometimes your Python environment is configured to prevent installing packages globally using pip3. To work around this, you can create a virtual environment. Virtual environments allow you to manage dependencies for your project without affecting the global Python environment.

1. Create a Virtual Environment

- Install the `python3-venv package` (if not already installed):

```bash
sudo apt update
sudo apt install python3-venv
```

- Create a virtual environment:

```bash
python3 -m venv venv
```

- Activate the virtual environment:

```bash
source venv/bin/activate
```

2. Install pandas in the Virtual Environment

With the virtual environment activated, you can now install `pandas` using `pip`:

```bash
pip install pandas
```

3. Run the Analysis Script

After installing `pandas`, you can run your analysis script within the virtual environment:

```bash
python scripts/analyze_logs.py
```
<br>![Screenshot 2024-06-11 175407](https://github.com/MenakaGodakanda/NetworkTrafficAnalysis/assets/156875412/69855378-a67c-4c54-8fcd-8d22e9fab83c)
<br>

4. Deactivate the Virtual Environment

When you are done, you can deactivate the virtual environment by simply running:

```bash
deactivate
```

## License

This project is licensed under the MIT License.






