import argparse
import sys
from os.path import basename, splitext, abspath, exists

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
                hpp, cpp = generate(data, name, basename(file), abspath(file))
                hpp_file = f"{args.dest}/{basename(file)}.hpp"
                hpp_prev = ""
                if exists(hpp_file):
                    with open(hpp_file, "r", encoding="utf-8") as hpp_f:
                        hpp_prev = hpp_f.read()
                if hpp != hpp_prev:
                    with open(hpp_file, "w", encoding="utf-8") as hpp_f:
                        hpp_f.write(hpp)
                cpp_file = f"{args.dest}/{basename(file)}.cpp"
                cpp_prev = ""
                if exists(cpp_file):
                    with open(cpp_file, "r", encoding="utf-8") as cpp_f:
                        cpp_prev = cpp_f.read()
                if cpp != cpp_prev:
                    with open(cpp_file, "w", encoding="utf-8") as cpp_f:
                        cpp_f.write(cpp)
        except FileNotFoundError:
            print(f"The file '{file}' does not exist.")
            sys.exit(1)
        except yaml.YAMLError as e:
            print(f"Error parsing YAML file '{file}': {e}")
            sys.exit(1)


if __name__ == "__main__":
    main()
