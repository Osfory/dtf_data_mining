### Data Mining project 

Example shows how to build and develop artifact using standard python ecosystem:
- `pip`: for dependencies management
- `venv`: for project isolation. By default python installs user or system wide dependencies
- `dependencies.txt` contains pip dependencies and version for reproducible builds
- `src` contains source code

Getting started:

- Install venv for python project isolation: `python -m venv .`
- Activate venv for shell: `source bin/activate`
- Install manual declared dependencies: `pip install -r dependencies.txt`
