"""empty message

Revision ID: 93f3c7a64d7f
Revises: ce48a8d6b85a
Create Date: 2025-11-25 21:57:08.198404

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '93f3c7a64d7f'
down_revision: Union[str, Sequence[str], None] = 'ce48a8d6b85a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
