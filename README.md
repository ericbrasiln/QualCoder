<img src="https://github.com/ccbogel/QualCoder/blob/master/qualcoder.png" width=200 height=200>

# QualCoder
QualCoder is a qualitative data analysis application written in python3 (python 3.6 or newer versions) and pyqt5.

Text files can be typed in manually or loaded from txt, odt, docx, html, htm, epub and  pdf files. Images, video and audio can also be imported for coding. Codes can be assigned to text, images and a/v selections and grouped into categories in hierarchical fashion. Various types of reports can be produced including visual coding graphs, coder comparisons and coding frequencies.

This project has been tested under Ubuntu 20.04 and Windows 10. It has been used on MacOS and various Linux distros.
Instructions and other information are available here: https://qualcoder.wordpress.com/ and on the [Github Wiki](https://github.com/ccbogel/QualCoder/wiki).

_NOTE_ Transcriptions created with QualCoder 2.8 and newer will have a .txt file ending. These transcription files will not be recoginsed in older QualCoder versions (2.7 and earlier). You will have to change the transcription name ending from '.txt' to '.transcribed' before opening any audio/video files to view or code if opening the project in older versions. In Sql Statements run this to have older versions recognise transcriptions (replace video.mp4 with the actual filename you have): `update source set name='video.mp4.transcribed' where name='video.mp4.txt'`

## INSTALLATION 

### Prerequisites
You will need to have a python3.6 or newer version installed and a 64 bit VLC player installed. 

### Windows

Install  [VLC](https://www.videolan.org/vlc/download-windows.html) or from the Windows Store. 

The 2.8 Release contains an exe file (created on Windows 10, 64 bit).Double-click to run. This does work on older Windows versions (e.g. Win 7). I have had one instance on Windows where an anti-virus affected the importing and moving of files by QualCoder (AVG). 

**Alternatively:**

1. Download the QualCoder software from: https://github.com/ccbogel/QualCode from the Green Code button. This is the newest, but not yet officially released code. Alternatively, choose the most recent release. Click the green button "Code", and then "Download ZIP". Then, unpack the file in a selected place (e.g. desktop).

2. Download and install the Python programming language. The minimum version for QualCoder is 3.6.  [Python3](https://www.python.org/downloads/). Download the file (at the bottom of the web site) "Windows installer (64-bit)"
IMPORTANT: in the first window of the installation mark the option "Add Python to PATH"

3. Install python modules from command. Type "cmd" in the Windows Start search engine, and click on the black software "cmd.exe" - the command console for Windows. In the console type or paste, using the right-click context menu (ctrl+v does not work) the following:

`py -m pip install wheel pyqt5 lxml Pillow ebooklib ply chardet pdfminer.six openpyxl pydub SpeechRecognition`

 Wait, until all modules are installed .
 
4. Build and install Qualcoder, from the downloaded folder type

`py setup.py install`

The `py` command uses the most recent installed version of python. You can use a specific version on your Windows, if you have many python versions installed, e.g. `py -3.8`  See discussion here: [Difference between py and python](https://stackoverflow.com/questions/50896496/what-is-the-difference-between-py-and-python-in-the-terminal)

5. Run QualCoder from cmd.exe
Move to the QualCoder-master folder, then type 

`py -m qualcoder`

Alternately, run by double-click. Open the QualCoder-master\qualcoder folder. Double-click the __main__.py file to run. You can make a shortcut to this file and keep the shortcut on the desktop.

### Debian/Ubuntu Linux

1. Install  modules from the command line

`sudo apt install python3-pip python3-lxml python3-ply python3-six python3-pdfminer python3-chardet python3-pyqt5 python3-pillow`

2. Install additional modules

`sudo python3 -m pip install pdfminer.six openpyxl ebooklib pydub SpeechRecognition`

3. Building and install QualCoder, from the downloaded folder type

`sudo python3 setup.py install`

4. To run type

`qualcoder`


### Arch/Manjaro Linux

1. Install modules from the command line

`sudo pacman -S python python-lxml python-ply python-six python-pdfminer python-chardet python-pyqt5 python-pillow python-pip`

2. Install additional python modules

`sudo python3 -m pip install pdfminer.six openpyxl ebooklib pydub SpeechRecognition`

If success, all requirements are satisfied.

3. Build and install QualCoder, from the downloaded folder type

`sudo python3 setup.py install`

4. To run type:

`qualcoder`

### Fedora/CentOS/RHEL linux

These instructions may need revision.

Retrieve the current package code from this repository

`git clone https://github.com/ccbogel/QualCoder.git`

Make `install_fedora.sh` executable (`chmod +x install_fedora.sh`) and run the `./install_fedora.sh` script from the terminal. Make sure the qualcoder folder is in the same directory as the install.sh script (i.e. as it appears when you download the QualCoder-master folder). The script is for python version 3.10.

This script installs the dependencies using dnf and the ebook libraries with a work-around, specified at https://github.com/ccbogel/QualCoder/issues/72#issuecomment-695962784.

Fedora uses wayland with does not work well with the Qt graphical interface (for now). I suggest you also install xwayland.

### MacOS

1) Install recent versions of [Python3](https://www.python.org/downloads/) and [VLC](https://www.videolan.org/vlc/).

2) Download the latest release "Source code" version in ZIP format, from the releases section of the project here on Github: https://github.com/ccbogel/QualCoder/releases/tag/2.8 and extract it into /Applications

3) Open the Terminal app (or any other command shell)

4) Install PIP (if not yet installed, try typing `pip3 --version` and hit ENTER) 

```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

-> You should now be able to run `pip3` as above.

5) Install Python dependency modules using `pip`:

(you might already have them, don't do this again if you just update QualCoder to a newer version)

```sh
pip install pyqt5 lxml pillow six ebooklib ply chardet pdfminer.six openpyxl pydub SpeechRecognition
```

6) Install system dependencies using Homebrew (aka `brew`) 

6.1) Install `brew` if do not already have it (try typing `brew` and hit ENTER):

* Follow instructions here about installing Homebrew on your macOS: https://brew.sh/

6.2) Install QPDF package (needed to deal with PDF files) using Homebrew package manager:

```sh
brew install qpdf
```

From the QualCoder-Master directory run the setup script:

`python3 setup.py install`


Assuming you downloaded the 2.8 version. You can now run with:

```
python3 /applications/QualCoder-2.8/qualcoder/__main__.py
```

Alternative commands to run QualCoder (Suggestions):

From any directory:

`qualcoder`

From the QualCoder-Master directory:

`python -m qualcoder`

or

`python qualcoder/__main__.py`

You can install QualCoder anywhere you want, so the path above depends on where you extracted the archive.

Another option to run Qualcoder is shown here: [https://www.maketecheasier.com/run-python-script-in-mac/](https://www.maketecheasier.com/run-python-script-in-mac/). This means you can right-click on the qualcoder.py file and open with --> python launcher. 
You can make an alias to the file and place it on your desktop.

**Another option to install on Mac:**

Open the Terminal App and move to the unzipped Qualcoder-Master directory, then run the following commands:

`pip install -U py2app`  or for a system installation of python `sudo pip install -U py2app`

`python3 setup.py py2app` 
 
## Dependencies
Required:

Python 3.6+ version, PyQt5, lxml, Pillow, six  (Mac OS), ebooklib, ply, chardet, pdfminer.six, openpyxl, pydub,  SpeechRecognition, qpdf  (Linux for programatically applying pdf decryption for pdfs with blank password)

## License
QualCoder is distributed under the MIT LICENSE.

##  Citation APA style

Curtain, C. (2021) QualCoder 2.8 [Computer software]. Retrieved from
https://github.com/ccbogel/QualCoder/releases/tag/2.8


## Leave a review
If you like QualCoder and found it useful for your work. Please leave a review on these sites:

https://www.saashub.com/qualcoder-alternatives

https://alternativeto.net/software/qualcoder


