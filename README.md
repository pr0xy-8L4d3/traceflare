# Traceflare

**TraceFlare** is a Python-based tool for analyzing the historical IP addresses of a domain. It helps you track past IPs associated with a domain and identify whether the traffic is routing through Cloudflare service. This can be useful for cybersecurity research and monitoring server exposure.

## Features

- Fetch historical IP data for a domain using the SecurityTrails API.
- Identify if a domain's traffic is going through Cloudflare.
- Summarize and highlight the most recent IP not belonging to Cloudflare.
- Clean and easy-to-read output with color-coded details.

## Installation

### Prerequisites

- Python 3.6 or higher
- A SecurityTrails API key (you can get one by signing up at [SecurityTrails](https://securitytrails.com/)).

### Steps

### 1. Clone the repository: 
```
  git clone https://github.com/pr0xy-8L4d3/traceflare.git
  cd traceflare
```
### 2. Install dependencies:
   ```
    pip install -r requirements.txt
```
### 3. Configure your API key:
   ```
   python3 initialize_traceflare.py
```
### 4. Usage
```
python3 traceflare.py example.com
```
