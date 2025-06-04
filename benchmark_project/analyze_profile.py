import os
import pstats

# Paths
PROFILE_PATH = os.path.join("results", "profile_results.prof")
OUTPUT_IMAGE_PATH = os.path.join("results", "profile_results.png")

# 1. Text-based profiling summary
print(f"📊 Analyzing: {PROFILE_PATH}\n")
if not os.path.exists(PROFILE_PATH):
    print("❌ profile_results.prof not found.")
else:
    stats = pstats.Stats(PROFILE_PATH)
    stats.strip_dirs().sort_stats("cumulative").print_stats(20)

# 2. Visualize using gprof2dot and Graphviz
print("\n🖼️ Generating image visualization...\n")
dot_command = f"gprof2dot -f pstats {PROFILE_PATH} | dot -Tpng -o {OUTPUT_IMAGE_PATH}"
ret = os.system(dot_command)

if ret == 0:
    print(f"✅ Image saved to {OUTPUT_IMAGE_PATH}")
else:
    print("⚠️ Failed to generate image. Please check if Graphviz is installed (dot command available).")
