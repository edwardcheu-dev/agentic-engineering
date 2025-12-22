from agentic_engineering.doctor import collect_doctor_report, render_doctor_report


def test_collect_doctor_report_shape():
    report = collect_doctor_report()
    assert isinstance(report.python_version, str)
    assert isinstance(report.platform, str)
    assert isinstance(report.gemini_api_key_set, bool)


def test_render_doctor_report_contains_fields():
    report = collect_doctor_report()
    out = render_doctor_report(report)
    assert "python_version" in out
    assert "platform" in out
    assert "GEMINI_API_KEY set" in out
