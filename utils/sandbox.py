# utils/sandbox.py
import tempfile, os, shutil, atexit

_SANDBOXES = []

def create_sandbox_workspace():
    path = tempfile.mkdtemp(prefix="mfn_workspace_")
    _SANDBOXES.append(path)
    # Optionally register cleanup on program exit.
    atexit.register(lambda: cleanup_sandboxes())
    return path

def cleanup_sandboxes():
    for p in list(_SANDBOXES):
        try:
            shutil.rmtree(p)
            _SANDBOXES.remove(p)
        except Exception:
            pass
