from sqlalchemy import create_engine

engine = create_engine(
        'mysql+pymysql://performance:performance@localhost/performance?charset=utf8',
    connect_args={
        'port': 3306
    },
    echo=False,
    echo_pool=False
)
