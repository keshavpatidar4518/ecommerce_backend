"""add content table to post table

Revision ID: 820e94f2315e
Revises: 49071b956fb1
Create Date: 2026-10-10 19:34:20.918709

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '820e94f2315e'
down_revision: Union[str, Sequence[str], None] = '49071b956fb1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
