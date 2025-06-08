# WEBSAVING

### What is it?

WEBSAVING is a Python-based application designed to synchronize save files for the game [WEBFISHING](https://store.steampowered.com/app/3146520/WEBFISHING/) with a GitHub repository. This tool allows you to easily back up and restore your game progress by pushing and pulling save files to/from a remote repository

### Features

- **Clone Repository**: Clone your GitHub repository to sync save files
- **Push Files**: Upload your local save files to the repository
- **Pull Files**: Download save files from the repository to your local machine
- **Git Setup**: Configure Git with your name and email for commits
- **Help**: Additional help
- **Launch WEBFISHING**: Start the game directly from Steam

### How to Use

1) Clone this repository

```
$ git clone https://github.com/Soup-o-Stat/WEBSAVING.git
Cloning into 'WEBSAVING'...
```

2) Run WEBSAVING.exe
3) Enter the URL of your GitHub repository in the "Repository URL" field and click Clone Repository to clone the repository to your local machine
4) Click "Setup Git" and enter your name and email in the pop-up window. These will be used for Git commits
5) Click "Push Files" to upload your local save files to the repository
6) Click "Pull Files" to download save files from the repository to your local machine
7) Click "Launch WEBFISHING" to start the game via Steam

### Save Files

The following save files are synchronized:
* webfishing_general_data.sav
* webfishing_save_slot_0.sav
* webfishing_backup_save_slot_0.backup
* webfishing_save_slot_1.sav
* webfishing_backup_save_slot_1.backup
* webfishing_save_slot_2.sav
* webfishing_backup_save_slot_2.backup
* webfishing_save_slot_3.sav
* webfishing_backup_save_slot_3.backup

These files are located in:

```
C:\Users\{YourUsername}\AppData\Roaming\Godot\app_userdata\webfishing_2_newver
```

### Support

For issues or questions, please open an issue!
