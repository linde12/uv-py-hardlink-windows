import nox

nox.options.default_venv_backend = "uv"

@nox.session
def test(session):
    session.install("markupsafe")
    session.run("python", "-c", """
import markupsafe
print(markupsafe.escape('Hello, <world>!'))
    """)
