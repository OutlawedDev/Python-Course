import os
import platform

def shutdown():
    """Attemps to shutdown the system based on ur OS."""
    current_os = platform.system()

    try:
        if current_os == "Windows":
            os.system("shutdown /s /t 1")
        elif current_os == "Darwin":
            os.system("sudo shutdown -h now")
        else:
            print("Shutdown command is not supported on this operating system")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    confirm = input("Are you sure you want to shutdown the system? (yes/no): ").strip().lower()
    if confirm == "yes":
        shutdown()
    else:
        print("Shutdown cancelled.")