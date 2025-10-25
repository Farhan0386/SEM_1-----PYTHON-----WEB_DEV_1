"""
Small wrapper to start Jupyter Notebook/Lab on Windows without the zmq Proactor warning.

Run with the Python used in this workspace, for example:
"C:/Program Files/Python314/python.exe" start_jupyter.py

This sets the WindowsSelectorEventLoopPolicy before launching the notebook server.
"""
import asyncio
import sys

try:
    # Use selector event loop on Windows to avoid zmq Proactor warning
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
except Exception:
    # If setting policy fails, continue to start Jupyter anyway
    pass

import runpy
import subprocess

def _start_notebook_via_module():
    # Fallback: run as a module (equivalent to `python -m notebook`)
    runpy.run_module('notebook', run_name='__main__')

def _start_notebook_via_subprocess():
    # Last-resort fallback: spawn python -m notebook
    subprocess.run([sys.executable, '-m', 'notebook'])

if __name__ == "__main__":
    # Try to start notebook using the module API if available.
    try:
        import notebook
        # Prefer notebook.notebookapp.main() if present
        notebook_app = getattr(notebook, 'notebookapp', None)
        if notebook_app and hasattr(notebook_app, 'main'):
            notebook_app.main()
        else:
            # Fallback to running the module
            _start_notebook_via_module()
    except Exception:
        # If import fails or something else goes wrong, try subprocess fallback
        try:
            _start_notebook_via_subprocess()
        except Exception:
            # If everything fails, raise so the caller can see the error
            raise
