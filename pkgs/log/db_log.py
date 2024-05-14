#  Copyright (c)2024. zhengzongwei
#  python-tools is licensed under Mulan PSL v2.
#  You can use this software according to the terms and conditions of the Mulan PSL v2.
#  You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
#  THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
#  EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
#  MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
#  See the Mulan PSL v2 for more details.

import datetime
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.datetime.now,
                                                 onupdate=datetime.datetime.now)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.datetime.now)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)


class Log(Base):
    __tablename__ = 'logs'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    level: Mapped[int]
    module: Mapped[str] = mapped_column(String)
    message: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)
    timestamp: Mapped[datetime] = mapped_column(DateTime)


class DBLog(object):
    def __init__(self, db_path=None):
        self.engine = create_engine('sqlite:///{}'.format(db_path))
        self.session = sessionmaker(bind=self.engine)()

        # TODO 检测表是否创建，没有创建则创建表
        Base.metadata.create_all(self.engine)


if __name__ == '__main__':
    DBLog("test")
