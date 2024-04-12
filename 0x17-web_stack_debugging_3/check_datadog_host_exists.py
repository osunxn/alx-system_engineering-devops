import requests

# Datadog API endpoint for listing hosts
url = "https://api.datadoghq.com/api/v1/hosts"

# Datadog API key
api_key = "YOUR_API_KEY_HERE"

# Function to check if the host exists
def check_host_exists(api_key, hostname):
    headers = {
        "Content-Type": "application/json",
        "DD-API-KEY": api_key
    }
    params = {
        "filter": f"host:{hostname}"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        hosts = response.json().get("host_list")
        if hosts:
            return True
    return False

# Main function
def main():
    hostname = "web-01"
    if check_host_exists(api_key, hostname):
        print("Host exists")
    else:
        print("Host does not exist")

if __name__ == "__main__":
    main()
