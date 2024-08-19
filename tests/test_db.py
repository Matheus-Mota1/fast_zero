from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Matheus',
        email='chessmota@gmail.com',
        password='mypassword',
    )

    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'chessmota@gmail.com')
    )

    assert result.username == 'Matheus'
