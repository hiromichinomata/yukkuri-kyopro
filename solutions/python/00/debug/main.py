import sys


def debug(*args, **kwargs) -> None:
    print(*args, **kwargs, file=sys.stderr)


def main() -> None:
    debug("local only", 42)  # 標準エラー出力なので、提出しても判定には影響しない


if __name__ == "__main__":
    main()
