import sys


def debug(*args, **kwargs) -> None:
    print(*args, **kwargs, file=sys.stderr)


def main() -> None:
    debug("local only", {"ok": True})


if __name__ == "__main__":
    main()
