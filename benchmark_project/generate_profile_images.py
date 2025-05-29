import os
import subprocess

PROFILE_DIR = "results"
OUTPUT_DIR = os.path.join(PROFILE_DIR, "graphs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

prof_files = [f for f in os.listdir(PROFILE_DIR) if f.endswith(".prof")]

if not prof_files:
    print("No .prof files found in 'results/' directory.")
else:
    for prof_file in prof_files:
        input_path = os.path.join(PROFILE_DIR, prof_file)
        output_path = os.path.join(OUTPUT_DIR, prof_file.replace(".prof", ".png"))

        cmd = f"gprof2dot -f pstats \"{input_path}\" | dot -Tpng -o \"{output_path}\""
        subprocess.run(cmd, shell=True)
        print(f"Saved: {output_path}")
