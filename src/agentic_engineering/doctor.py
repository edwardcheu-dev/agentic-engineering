from __future__ import annotations

import os
import platform
from dataclasses import dataclass


@dataclass(frozen=True)
class DoctorReport:
    python_version: str
    platform: str
    google_cloud_project_set: bool
    google_cloud_location_set: bool


def collect_doctor_report() -> DoctorReport:
    return DoctorReport(
        python_version=platform.python_version(),
        platform=platform.platform(),
        google_cloud_project_set=bool(os.getenv("GOOGLE_CLOUD_PROJECT")),
        google_cloud_location_set=bool(os.getenv("GOOGLE_CLOUD_LOCATION")),
    )


def render_doctor_report(report: DoctorReport) -> str:
    # Important: do NOT print the key, only whether it's present.
    lines = [
        "agentic-engineering doctor",
        f"- python_version: {report.python_version}",
        f"- platform: {report.platform}",
        f"- GOOGLE_CLOUD_PROJECT set: {report.google_cloud_project_set}",
        f"- GOOGLE_CLOUD_LOCATION set: {report.google_cloud_location_set}",
    ]
    return "\n".join(lines) + "\n"
