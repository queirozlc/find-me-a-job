"""Run with python3 -B scripts/test_resume_gate.py."""

from resume_gate import bullets, roles, SECTION_NAMES


for heading in ("Experience", "Experiência", r"Experi\^encia", "Experiencia"):
    source = (
        rf"\section{{{heading}}}"
        r"\resumeSubheading{Company}{Jan 2024 - Present}{Engineer}{Remote}"
        r"\resumeItem{Built TypeScript services.}"
        r"\section{Education}\resumeItem{Degree}"
    )
    assert roles(source) == [("Company", "Jan 2024 - Present", "Engineer", "Remote")]
    assert bullets(source) == ["Built TypeScript services."]
assert SECTION_NAMES["es"] == ("Resumen", "Habilidades", "Experiencia", "Educación", "Idiomas")
print("PASS: English, Portuguese, escaped Portuguese, and Spanish Experience sections")
