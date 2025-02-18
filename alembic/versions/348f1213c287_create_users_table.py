"""Create users table

Revision ID: 348f1213c287
Revises: 
Create Date: 2024-12-10 15:55:10.285867

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '348f1213c287'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('lastname', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_authors_id'), 'authors', ['id'], unique=False)
    op.create_index(op.f('ix_authors_lastname'), 'authors', ['lastname'], unique=False)
    op.create_index(op.f('ix_authors_name'), 'authors', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_authors_name'), table_name='authors')
    op.drop_index(op.f('ix_authors_lastname'), table_name='authors')
    op.drop_index(op.f('ix_authors_id'), table_name='authors')
    op.drop_table('authors')
    # ### end Alembic commands ###
