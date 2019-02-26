from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://root@localhost/sqlquery-poc?charset=utf8',
    connect_args={
        'port': 3306
    },
    echo='debug',
    echo_pool=True
)