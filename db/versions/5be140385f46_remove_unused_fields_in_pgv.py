"""Remove unused fields in PGV

Revision ID: 5be140385f46
Revises: f252364cce3d
Create Date: 2021-10-12 09:38:05.786001

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5be140385f46'
down_revision = 'f252364cce3d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pgv_defendants', 'address_2')
    op.drop_column('pgv_plaintiffs', 'address_2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pgv_plaintiffs', sa.Column('address_2', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('pgv_defendants', sa.Column('address_2', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
