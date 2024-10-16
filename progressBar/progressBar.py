import time, random

PROGRESS_BAR = chr(9608)  # Block symbol for the progress bar

def main():
    print('Progress Bar Simulation\n')

    # User defined download size (default: 4096 bytes)
    download_size = 6000
    bytes_downloaded = 0
    start_time = time.time()

    while bytes_downloaded < download_size:
        # Simulating download by incrementing a random number of bytes
        bytes_downloaded += random.randint(50, 150)
        bytes_downloaded = min(bytes_downloaded, download_size)  # To sEnsure it doesn't exceed the total size
        
        # Print the progress bar
        bar_str = get_progress_bar(bytes_downloaded, download_size)
        print(bar_str, end='', flush=True)
        
        # Simulate network delay
        time.sleep(0.1)

        # Clear the previous progress bar
        print('\b' * len(bar_str), end='', flush=True)

    # Print final progress and download speed
    end_time = time.time()
    duration = end_time - start_time
    print(f"Download complete in {duration:.2f} seconds at {download_size/duration:.2f} bytes/second.")

def get_progress_bar(progress, total, bar_width=40):
    """
    Creates and returns the progress bar string based on current progress.
    """
    # Calculate number of blocks for the progress bar
    filled_length = int(bar_width * progress // total)
    bar = PROGRESS_BAR * filled_length + '-' * (bar_width - filled_length)

    # Calculate percentage completion
    percent_complete = round(progress / total * 100, 1)

    # Format the progress bar string
    progress_bar = f"[{bar}] {percent_complete}% ({progress}/{total} bytes)"
    return progress_bar

if __name__ == '__main__':
    main()
