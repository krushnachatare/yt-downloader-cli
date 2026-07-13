# YouTube Downloader

A simple and fast YouTube downloader built with Python using **yt-dlp**. Download videos in **MP4** or extract audio in **MP3** format from YouTube.

## Features

* Download YouTube videos in MP4 format
* Download audio in MP3 format
* Supports high-quality downloads
* Simple command-line interface
* Built using `yt-dlp`

## Requirements

Before running the project, make sure you have:

* Python 3.10 or later
* FFmpeg installed and added to your system PATH
* Internet connection

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/krushnachatare/yt-downloader-cli.git
cd yt-downloader-cli
```

### 2. Install Python dependencies

Run the installer:

```bash
install.bat
```

Or install manually:

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg

Download FFmpeg, extract it, and add its `bin` folder to your system PATH.

After installation, verify it by running:

```bash
ffmpeg -version
```

If the version information appears, FFmpeg has been installed correctly.

## Usage

Run the program with:

```bash
python main.py
```

Follow the on-screen instructions to choose the download format and provide the YouTube URL.

## Project Structure

```text
.
├── main.py
├── requirements.txt
├── install.bat
└── README.md
```

## Technologies Used

* Python
* yt-dlp
* FFmpeg

## Future Plans

* Graphical User Interface (GUI)
* Download progress bar
* Better error handling
* Automatic update checking
* Standalone Windows executable
* Playlist support improvements

## Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## License

This project is available under the MIT License.
