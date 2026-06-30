import shutil
import subprocess
import sys

def run(cmd: list[str]) -> None:
    print(f"+ {' '.join(cmd)}")
    subprocess.check_call(cmd)

def main() -> int:
    uv = shutil.which("uv")
    if not uv:
        print(
            "uv is not installed.\n"
            "Install it first (see Astral docs), then run:\n"
            "  uv sync\n"
            "  uv add <package>\n"
        )
        return 0

    # Create/update lockfile + create .venv + install deps
    run([uv, "sync"])

    # (Optional) install dev groups too:
    # run([uv, "sync", "--group", "dev"])

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
