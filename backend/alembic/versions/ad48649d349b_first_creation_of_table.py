"""first creation of table

Revision ID: ad48649d349b
Revises: 
Create Date: 2025-10-17 18:12:23.185992

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad48649d349b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("Grocery",
                    sa.Column("id",sa.Integer(),primary_key=True,nullable=False),
                    sa.Column("name",sa.String(),nullable=False),
                    sa.Column("description",sa.String(),nullable=False),
                    sa.Column("price",sa.Float(),nullable=False),
                    sa.Column("quantity",sa.Integer(),nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("Grocery")



