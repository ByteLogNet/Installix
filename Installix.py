import os
import sys
import time
import pyfiglet
import requests
import colorama
from colorama import Fore, Style
import ctypes  # For checking and requesting admin rights

# Initialize colorama
colorama.init()

# Custom orange color using ANSI escape codes
ORANGE = '\033[38;2;255;165;0m'

# Ascii text
font = pyfiglet.Figlet(font='big')
Installix = font.renderText('Installix')

# Function to clear the terminal
def clear_terminal():
    if sys.platform == "win32":
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For macOS and Linux

# Function to download a file from a URL
def download_file(url, filename):
    try:
        print(ORANGE + f"Downloading {filename}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP request errors
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(ORANGE + f"{filename} downloaded successfully.")
    except Exception as e:
        print(ORANGE + f"Failed to download {filename}: {e}")

# Function to handle download completion
def handle_download_completion():
    # Reset color for the prompt
    print(Style.RESET_ALL + "Press Enter to continue...", end='')
    input()  # Wait for user input
    # Reapply orange color after the input
    print(ORANGE, end='')

# Display browser list
def show_browser():
    clear_terminal()
    print(ORANGE + Installix)
    print(Fore.LIGHTBLUE_EX + "===> A simple installer for Windows <===")
    print()
    print(Style.RESET_ALL + "[-] Browser List:")
    print()
    print(ORANGE + "[1] Arc")
    print(ORANGE + "[2] Brave")
    print(ORANGE + "[3] Chrome")
    print(ORANGE + "[4] Edge")
    print(ORANGE + "[5] Firefox")
    print(ORANGE + "[6] Tor Browser")
    print()
    print(Style.RESET_ALL + "[7] Back to Main Menu")

# Display software list
def show_software():
    clear_terminal()
    print(ORANGE + Installix)
    print(Fore.LIGHTBLUE_EX + "===> A simple installer for Windows <===")
    print()
    print(Style.RESET_ALL + "[-] Software List:")
    print()
    print(ORANGE + "[1] Discord")
    print(ORANGE + "[2] Telegram")
    print(ORANGE + "[3] Visual Studio 2022")
    print(ORANGE + "[4] Spotify")
    print(ORANGE + "[5] Steam")
    print(ORANGE + "[6] Epic Games Launcher")
    print(ORANGE + "[7] WinRAR")
    print()
    print(Style.RESET_ALL + "[8] Back to Main Menu")

# Handle browser choice
def handle_browser_choice(browser_choice):
    if browser_choice == '1':
        download_file("https://releases.arc.net/windows/ArcInstaller.exe", "ArcInstaller.exe")
    elif browser_choice == '2':
        download_file("https://laptop-updates.brave.com/latest/win64", "BraveSetup.exe")
    elif browser_choice == '3':
        download_file("https://dl.google.com/chrome/install/latest/chrome_installer.exe", "ChromeSetup.exe")
    elif browser_choice == '4':
        download_file("https://go.microsoft.com/fwlink/?LinkId=2124703", "EdgeSetup.exe")
    elif browser_choice == '5':
        download_file("https://download.mozilla.org/?product=firefox-latest&os=win&lang=en-US", "FirefoxSetup.exe")
    elif browser_choice == '6':
        download_file("https://www.torproject.org/dist/torbrowser/13.5.1/tor-browser-windows-x86_64-portable-13.5.1.exe", "TorBrowserSetup.exe")
    elif browser_choice == '7':
        return False
    else:
        print(ORANGE + "Invalid option.")
    handle_download_completion()
    return True

# Handle software choice
def handle_software_choice(software_choice):
    if software_choice == '1':
        download_file("https://discord.com/api/download?platform=win", "DiscordSetup.exe")
    elif software_choice == '2':
        download_file("https://telegram.org/dl/desktop/win", "TelegramSetup.exe")
    elif software_choice == '3':
        download_file("https://aka.ms/vs/17/release/vs_installer.exe", "VisualStudioSetup.exe")
    elif software_choice == '4':
        download_file("https://download.scdn.co/SpotifySetup.exe", "SpotifySetup.exe")
    elif software_choice == '5':
        download_file("https://cdn.cloudflare.steamstatic.com/client/installer/SteamSetup.exe", "SteamSetup.exe")
    elif software_choice == '6':
        download_file("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi", "EpicGamesLauncherSetup.msi")
    elif software_choice == '7':
        download_file("https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-610.exe", "WinRARSetup.exe")
    elif software_choice == '8':
        return False
    else:
        print(ORANGE + "Invalid option.")
    handle_download_completion()
    return True

# Handle main choice
def handle_choice(choice):
    if choice == '1':
        while True:
            show_browser()
            browser_choice = input(Style.RESET_ALL + "Your choice: ")
            if not handle_browser_choice(browser_choice):
                break
    elif choice == '2':
        while True:
            show_software()
            software_choice = input(Style.RESET_ALL + "Your choice: ")
            if not handle_software_choice(software_choice):
                break
    elif choice == '3':
        clear_terminal()
        print(ORANGE + "Exiting Installix. Goodbye!")
        sys.exit()
    else:
        clear_terminal()
        print(ORANGE + Installix)
        print(ORANGE + "Invalid option.")
        handle_download_completion()

# Function to check for admin privileges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Function to restart the script with admin privileges
def run_as_admin():
    if sys.platform == "win32" and not is_admin():
        try:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit(0)  # Exit the current instance after launching the elevated process
        except Exception as e:
            print(ORANGE + f"Failed to elevate privileges: {e}")
            sys.exit(1)

# Main program loop
run_as_admin()

clear_terminal()
print(ORANGE + Installix)
# Reset color before the prompt
print(Style.RESET_ALL + "Press Enter to continue...", end='')
input()  # Wait for user input

while True:
    clear_terminal()
    print(ORANGE + Installix)
    print(Fore.LIGHTBLUE_EX + "===> A simple installer for Windows <===")
    print()
    print(Style.RESET_ALL + "[-] What action would you like to perform?")
    print()
    print(ORANGE + "[1] Browsers")
    print(ORANGE + "[2] Software")
    print(ORANGE + "[3] Exit")
    print()

    choice = input(Style.RESET_ALL + "Your choice: ")
    handle_choice(choice)
    time.sleep(1)  # Brief pause to let the user see the message before clearing
