"""create urls  table

Revision ID: 43f71df15b94
Revises: 
Create Date: 2024-07-12 22:49:08.442432

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '43f71df15b94'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original_url', sa.String(length=2000), nullable=False),
    sa.Column('short_key', sa.String(length=10), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=True),
    sa.Column('visit_count', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_urls_id'), 'urls', ['id'], unique=False)
    op.create_index(op.f('ix_urls_short_key'), 'urls', ['short_key'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_urls_short_key'), table_name='urls')
    op.drop_index(op.f('ix_urls_id'), table_name='urls')
    op.drop_table('urls')
    # ### end Alembic commands ###