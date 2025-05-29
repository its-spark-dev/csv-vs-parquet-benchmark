import os
import subprocess
import webbrowser

# Directory where .prof files are stored
PROFILE_DIR = "results"

# Collect all .prof files and sort them by modification time
prof_files = sorted(
    [f for f in os.listdir(PROFILE_DIR) if f.endswith(".prof")],
    key=lambda x: os.path.getmtime(os.path.join(PROFILE_DIR, x))
)

# If no .prof files exist, print a warning and exit
if not prof_files:
    print("⚠️  No .prof files found in 'results/' directory. Please run the benchmark first.")
else:
    print(f"🔍 Found {len(prof_files)} profile file(s). Launching SnakeViz in browser tabs...\n")

    # Launch SnakeViz for each .prof file in a new browser tab
    for prof_file in prof_files:
        prof_path = os.path.join(PROFILE_DIR, prof_file)
        print(f"Opening: {prof_path}")
        subprocess.Popen(["snakeviz", prof_path])
