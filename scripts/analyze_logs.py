import pandas as pd

# Define the column names
columns = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service',
           'duration', 'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig', 'local_resp',
           'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes',
           'tunnel_parents']

# Load Zeek connection log with the correct column names
conn_log = pd.read_csv('conn.log', sep='\t', comment='#', na_values='-', low_memory=False, names=columns)

# Print the first few rows
print(conn_log.head())

# Print the column names
print(conn_log.columns)

# Filter for potential anomalies (e.g., connections with a duration of zero)
anomalies = conn_log[conn_log['duration'] == 0]

# Save anomalies to a file
anomalies.to_csv('analysis/anomalies.csv', index=False)
