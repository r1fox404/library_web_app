"""empty message

Revision ID: 32bb1d422856
Revises: 878270489838
Create Date: 2024-12-13 19:32:42.909058

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32bb1d422856'
down_revision: Union[str, None] = '878270489838'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrows', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Boolean(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_borrows_book_id_books'), 'books', ['book_id'], ['id'])

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('borrows', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_borrows_book_id_books'), type_='foreignkey')
        batch_op.drop_column('status')

    # ### end Alembic commands ###