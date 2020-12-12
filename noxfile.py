import nox


@nox.session
def test(session):
    session.install("-e", ".[testing]")
    session.run("pytest")