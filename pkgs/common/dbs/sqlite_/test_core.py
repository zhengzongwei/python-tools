import pytest
import random
from core import UserORM, User


@pytest.fixture
def user_orm():
    db_path = 'test.db'
    user_orm = UserORM(db_path)
    yield user_orm
    user_orm.session.close()


def test_add_user(user_orm):
    test_user_data = {
        'id': random.randint(1, 1000),
        'name': 'Test User',
        'full_name': 'Test User',
    }
    user_orm.add_user(test_user_data)

    # 确认用户是否添加
    user = user_orm.session.get(User, test_user_data['id'])
    assert user is not None
    assert user.name == test_user_data['name']
    assert user.full_name == test_user_data['full_name']
