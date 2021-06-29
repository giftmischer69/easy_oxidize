from wasabi import msg

from {{cookiecutter.project_slug}}._version import __version__

def main():
    name = "{{cookiecutter.project_slug}}"
    msg.good(f"hello from {name} version: {__version__}")

if __name__ == '__main__':
    main()