import requests
import threading
import argparse
from urllib.parse import urljoin

# Lock for thread-safe output
print_lock = threading.Lock()
found_paths = []

def check_directory(base_url, directory):
    url = urljoin(base_url, directory.strip())
    try:
        response = requests.get(url, timeout=5)
        if response.status_code in [200, 301, 302, 403]:
            with print_lock:
                print(f"[{response.status_code}] {url}")
                found_paths.append((url, response.status_code))
    except requests.RequestException:
        pass  # Ignore errors (timeout, connection issues)

def main():
    parser = argparse.ArgumentParser(description="🕵️ DirBrute - Directory Brute-Forcer")
    parser.add_argument("-u", "--url", required=True, help="Target base URL (e.g. https://example.com/)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("-o", "--output", help="Output file to save found paths")
    args = parser.parse_args()

    try:
        with open(args.wordlist, "r") as f:
            directories = f.read().splitlines()

        print(f"\n🔍 Starting directory scan on: {args.url}\n")

        threads = []
        for directory in directories:
            t = threading.Thread(target=check_directory, args=(args.url, directory))
            t.start()
            threads.append(t)

        for thread in threads:
            thread.join()

        print(f"\n✅ Scan Complete. Found {len(found_paths)} valid paths.")

        if args.output:
            with open(args.output, "w") as f:
                for path, code in found_paths:
                    f.write(f"[{code}] {path}\n")
            print(f"📁 Results saved to: {args.output}")

    except FileNotFoundError:
        print("❌ Wordlist file not found.")

if __name__ == "__main__":
    main()
