"""idx users level/score

Revision ID: ccce9e853985
Revises: 449d04fca80b
Create Date: 2025-10-02 22:38:19.417837

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ccce9e853985"
down_revision: Union[str, Sequence[str], None] = "449d04fca80b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    _ = (op, sa)


def downgrade() -> None:
    _ = (op, sa)
