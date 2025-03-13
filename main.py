import os
import tkinter as tk
from tkinter import messagebox
from git import Repo, GitCommandError
import shutil
import webbrowser

SAVE_FILES = [
    "webfishing_general_data.sav",
    "webfishing_save_slot_0.sav",
    "webfishing_backup_save_slot_0.backup",
    "webfishing_save_slot_1.sav",
    "webfishing_backup_save_slot_1.backup",
    "webfishing_save_slot_2.sav",
    "webfishing_backup_save_slot_2.backup",
    "webfishing_save_slot_3.sav",
    "webfishing_backup_save_slot_3.backup",
]
SAVE_DIR = os.path.join(os.getenv('APPDATA'), 'Godot', 'app_userdata', 'webfishing_2_newver')
REPO_DIR = "repo"

def clone_repo():
    repo_url = repo_entry.get()
    if not repo_url:
        messagebox.showerror("Error", "Please enter the repository URL")
        return

    try:
        Repo.clone_from(repo_url, REPO_DIR)
        messagebox.showinfo("Success", "Repository cloned successfully")
    except GitCommandError as e:
        messagebox.showerror("Error", f"Error cloning repository: {e}")

def push_files():
    try:
        repo = Repo(REPO_DIR)
        for file in SAVE_FILES:
            src = os.path.join(SAVE_DIR, file)
            dst = os.path.join(REPO_DIR, file)
            if os.path.exists(src):
                shutil.copy2(src, dst)
        repo.git.add(A=True)
        repo.index.commit("Update save files")
        origin = repo.remote(name="origin")
        origin.push()
        messagebox.showinfo("Success", "Files successfully pushed to the repository")
    except GitCommandError as e:
        messagebox.showerror("Error", f"Error pushing files: {e}")

def pull_files():
    try:
        repo = Repo(REPO_DIR)
        origin = repo.remote(name="origin")
        origin.pull()
        for file in SAVE_FILES:
            src = os.path.join(REPO_DIR, file)
            dst = os.path.join(SAVE_DIR, file)
            if os.path.exists(src):
                shutil.copy2(src, dst)
        messagebox.showinfo("Success", "Files successfully pulled from the repository")
    except GitCommandError as e:
        messagebox.showerror("Error", f"Error pulling files: {e}")

def setup_git():
    setup_window = tk.Toplevel(root)
    setup_window.title("Git Setup")
    setup_window.geometry("300x100")

    name_label = tk.Label(setup_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(setup_window, width=30)
    name_entry.pack()

    email_label = tk.Label(setup_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(setup_window, width=30)
    email_entry.pack()

    def confirm_git_setup():
        name = name_entry.get()
        email = email_entry.get()
        if not name or not email:
            messagebox.showerror("Error", "Please enter both name and email")
            return

        try:
            repo = Repo(REPO_DIR)
            repo.config_writer().set_value("user", "name", name).release()
            repo.config_writer().set_value("user", "email", email).release()
            messagebox.showinfo("Success", "Git configured successfully")
            setup_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error configuring Git: {e}")

    confirm_button = tk.Button(setup_window, text="Confirm", command=confirm_git_setup)
    confirm_button.pack()

def open_help():
    webbrowser.open("https://github.com/Soup-o-Stat/WEBSAVING/blob/main/README.md")

def launch_webfishing():
    webbrowser.open("steam://rungameid/3146520")

root = tk.Tk()
root.title("WEBSAVING")

try:
    root.iconbitmap("icon.ico")
except Exception as e:
    print(f"Icon not found: {e}")

repo_label = tk.Label(root, text="Repository URL:")
repo_label.pack()
repo_entry = tk.Entry(root, width=50)
repo_entry.pack()

clone_button = tk.Button(root, text="Clone Repository", command=clone_repo)
clone_button.pack()

setup_git_button = tk.Button(root, text="Setup Git", command=setup_git)
setup_git_button.pack()

push_button = tk.Button(root, text="Push Files", command=push_files)
push_button.pack()

pull_button = tk.Button(root, text="Pull Files", command=pull_files)
pull_button.pack()

help_button = tk.Button(root, text="Help", command=open_help)
help_button.pack()

launch_button = tk.Button(root, text="Launch WEBFISHING", command=launch_webfishing)
launch_button.pack()

root.mainloop()