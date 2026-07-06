# File-cloning
✅ Basic Termux setup (do this first)
pkg update && pkg upgrade -y
pkg install git python -y
📥 Clone the repo
git clone https://github.com/zemant1py/File-cloning.git
📂 Enter the folder
cd File-cloning
🔎 Check what files are inside
ls
▶️ Now run it (depends on file type)
1. If it has Python file (most common)
Look for .py file then run:
python file.py
Example:
python main.py
2. If it has requirements.txt
pip install -r requirements.txt
Then run again:
python main.py
3. If it uses bash script
If you see .sh file:
chmod +x file.sh
bash file.sh
