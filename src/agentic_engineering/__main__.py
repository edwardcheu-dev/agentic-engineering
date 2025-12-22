from __future__ import annotations

import argparse

from .doctor import collect_doctor_report, render_doctor_report


def _cmd_doctor(_: argparse.Namespace) -> int:
    report = collect_doctor_report()
    print(render_doctor_report(report), end="")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ae", description="agentic-engineering CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    p_doctor = sub.add_parser("doctor", help="print environment + config sanity checks")
    p_doctor.set_defaults(func=_cmd_doctor)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
