from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session
)

from core.config import settings


class DBConnection:
    
    def __init__(self, url: str, echo: bool):
        self._engine = create_async_engine(
            url=url,
            echo=echo
        )
        self._session_factory = async_sessionmaker(
            bind=self._engine,
            autoflush=False,
            expire_on_commit=False
        )
    
    
    def _get_scoped_session(self) -> async_scoped_session:
        session = async_scoped_session(
            session_factory=self._session_factory,
            scopefunc=current_task
        )
        return session
    
    
    async def scoped_session(self) -> AsyncSession:
        session = self._get_scoped_session()
        yield session
        await session.close()


db_conn = DBConnection(
    url=settings.db.url,
    echo=settings.db.echo
)