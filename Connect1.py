import tkinter as tk
from tkinter import messagebox
import subprocess

def show_popup():
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askquestion("Option", "Click Yes for Volume Controller and No for Virtual Mouse")
    root.destroy()
    return result

def main():
    result = show_popup()
    if result == 'yes':
        import AIVirtualMouse
        import VolumeHandControlAdvance as vhca
        vhca.VolumeHandControlAdvance()
        AIVirtualMouse.main()

    else:
        import MediaPlayerController
        mpc.main()

if __name__ == "__main__":
    main()
