"""Add body_weight_kg & weight_class to users.

Revision ID: 449d04fca80b
Revises: 5a7d8d8c5d05
Create Date: 2025-10-03
"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "449d04fca80b"
down_revision = "5a7d8d8c5d05"
branch_labels = None
depends_on = None


def upgrade():
    # Idempotent: works on fresh and existing DBs
    op.execute(
        "ALTER TABLE IF EXISTS users\n"
        "ADD COLUMN IF NOT EXISTS body_weight_kg DOUBLE PRECISION"
    )
    op.execute(
        "ALTER TABLE IF EXISTS users\n" "ADD COLUMN IF NOT EXISTS weight_class TEXT"
    )


def downgrade():
    op.execute("ALTER TABLE IF EXISTS users\n" "DROP COLUMN IF EXISTS body_weight_kg")
    op.execute("ALTER TABLE IF EXISTS users\n" "DROP COLUMN IF EXISTS weight_class")
