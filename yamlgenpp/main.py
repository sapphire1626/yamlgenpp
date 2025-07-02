import argparse
import sys
from os.path import basename, splitext, abspath

try:
    from .generator import generate
except ImportError:
    from generator import generate

try:
    import yaml
except ImportError as e:
    print("ImportError:", e)
    print("Try installing PyYAML with 'pip install pyyaml'")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="YAML to C++ struct generator")
    parser.add_argument("files", nargs="*", help="Path to the YAML files.")
    parser.add_argument(
        "-d",
        "--dest",
        type=str,
        default=".",
        help="Destination directory for generated files.",
    )
    args = parser.parse_args()

    if not args.files:
        print("No files provided.")
        sys.exit(1)

    for file in args.files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
                if data is None:
                    print(f"Warning: The file '{file}' is empty")
                    data = {}
                elif not isinstance(data, dict):
                    print(f"The file '{file}' does not contain a YAML dictionary")
                    sys.exit(1)
                name = basename(splitext(file)[0])
                hpp, cpp = generate(data, name, abspath(file))
                with open(f"{args.dest}/{name}.hpp", "w", encoding="utf-8") as out_f:
                    out_f.write(hpp)
                with open(f"{args.dest}/{name}.cpp", "w", encoding="utf-8") as out_f:
                    out_f.write(cpp)
        except FileNotFoundError:
            print(f"The file '{file}' does not exist.")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file '{file}': {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
