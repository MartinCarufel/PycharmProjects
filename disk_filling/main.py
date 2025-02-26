import os
import shutil

# Configuration
usb_path = "D:\\"  # Change this to your USB drive path
leave_space = 5 * 1024  # 9 KB

def get_free_space_bytes(path):
    """Returns the available free space in bytes on Windows."""
    total, used, free = shutil.disk_usage(path)
    return free

def fill_usb_with_random_data(path, leave_bytes):
    """Fills the USB with random data leaving specified free space."""
    free_space = get_free_space_bytes(path)
    print(free_space)
    write_size = free_space - leave_bytes  # Space to fill

    if write_size <= 0:
        print("Not enough space to write data.")
        return

    # file_path = os.path.join(path, "random_fill.bin")
    file_path = get_unique_filename(path)
    with open(file_path, "wb") as f:
        chunk_size = 1024 * 1024  # 1MB per write
        written = 0

        while written < write_size:
            chunk = min(chunk_size, write_size - written)
            f.write(os.urandom(chunk))
            written += chunk
            print(f"Written {written}/{write_size} bytes...", end="\r")

    print("\nUSB drive filled with random data.")

def get_unique_filename(directory, base_name="random_fill", extension=".bin"):
    """Generate a unique file name with an incremental suffix if needed."""
    file_path = os.path.join(directory, f"{base_name}{extension}")

    if not os.path.exists(file_path):
        return file_path  # Return if no conflict

    # If file exists, increment suffix
    counter = 1
    while True:
        file_path = os.path.join(directory, f"{base_name}_{counter}{extension}")
        if not os.path.exists(file_path):
            return file_path
        counter += 1

if __name__ == "__main__":
    fill_usb_with_random_data(usb_path, leave_space)
