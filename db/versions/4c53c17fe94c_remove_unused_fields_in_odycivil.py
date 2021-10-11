"""Remove unused fields in ODYCIVIL

Revision ID: 4c53c17fe94c
Revises: f3606af6398f
Create Date: 2021-10-11 15:36:35.851693

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c53c17fe94c'
down_revision = 'f3606af6398f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('odycivil_defendants', 'race')
    op.drop_column('odycivil_defendants', 'height')
    op.drop_column('odycivil_defendants', 'sex')
    op.drop_column('odycivil_defendants', 'weight')
    op.drop_column('odycivil_documents', 'filed_by')
    op.drop_column('odycivil_services', 'service_status')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('odycivil_services', sa.Column('service_status', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('odycivil_documents', sa.Column('filed_by', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('odycivil_defendants', sa.Column('weight', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('odycivil_defendants', sa.Column('sex', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('odycivil_defendants', sa.Column('height', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('odycivil_defendants', sa.Column('race', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###