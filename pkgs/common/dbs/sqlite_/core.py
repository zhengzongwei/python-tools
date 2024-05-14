#  Copyright (c)2024. zhengzongwei
#  python-tools is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

from sqlalchemy import create_engine, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class SQLITE(object):
    def __init__(self, db_path: str = None):
        self.engine = create_engine('sqlite:///{}'.format(db_path))
        self.session = sessionmaker(bind=self.engine)()

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(self.engine)


class UserORM(SQLITE):
    def __init__(self, db_path: str = None):
        super().__init__(db_path)
        self.create_tables()

    def add_user(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.flush()
        self.session.commit()

    def get_user_by_id(self, id):
        return self.session.get(User, id)

    def get_user_by_name(self, name):
        return self.session.get(User, name)

    def __del__(self):
        if self.session:
            self.session.close()


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    full_name: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, full_name={self.full_name!r})"


# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email: Mapped[str]
#     user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
#
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email={self.email!r})"
#

#
if __name__ == '__main__':
    sqlite = UserORM('./test.db')
    print(sqlite.get_user_by_id(2))
#     user_data = {'id': 5, 'name': 'zhengzongwei', 'full_name': 'zhengzongwei'}
#     sqlite.add_user(user_data)
