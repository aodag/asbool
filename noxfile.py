import nox

nox.options.sessions = ["test"]


@nox.session
def test(session):
    session.install("-e", ".[testing]")
    session.run("pytest")


@nox.session
def pack(session):
    session.install("pep517")
    session.run("python", "-m", "pep517.build", ".")