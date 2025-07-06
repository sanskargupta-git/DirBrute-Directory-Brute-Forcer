# 🕵️ DirBrute – Directory Brute-Forcer (Python)

**DirBrute** is a fast and multithreaded directory brute-forcing tool written in Python. It helps ethical hackers and bug bounty hunters discover hidden directories on web servers.

## 🚀 Features

- Multithreaded directory scanning
- Smart status code filtering (200, 301, 403)
- Saves results to output file
- Easy command-line usage with `argparse`
- Beginner-friendly and fully open-source

## 🔧 Usage

```bash
python dirbrute.py -u https://example.com -w dirs.txt -o output.txt
