import subprocess
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: h5ad2seurat <path_to_h5ad_file>")
        sys.exit(1)
    # Call the Bash script
    subprocess.run(["./h5ad2seurat/h5ad2seurat.sh", sys.argv[1]])

if __name__ == "__main__":
    main()