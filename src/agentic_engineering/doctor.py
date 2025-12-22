from __future__ import annotations

import os
import platform
from dataclasses import dataclass


@dataclass(frozen=True)
class DoctorReport:
    python_version: str
    platform: str
    gemini_api_key_set: bool


def collect_doctor_report() -> DoctorReport:
    return DoctorReport(
        python_version=platform.python_version(),
        platform=platform.platform(),
        gemini_api_key_set=bool(os.getenv("GEMINI_API_KEY")),
    )


def render_doctor_report(report: DoctorReport) -> str:
    # Important: do NOT print the key, only whether it's present.
    lines = [
        "agentic-engineering doctor",
        f"- python_version: {report.python_version}",
        f"- platform: {report.platform}",
        f"- GEMINI_API_KEY set: {report.gemini_api_key_set}",
    ]
    return "\n".join(lines) + "\n"
