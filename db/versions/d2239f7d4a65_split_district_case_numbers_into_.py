"""split district case numbers into separate table from CC

Revision ID: d2239f7d4a65
Revises: b279918a6f75
Create Date: 2018-05-21 09:02:25.532060

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2239f7d4a65'
down_revision = 'b279918a6f75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cc_district_case_numbers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district_case_number', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('cc', 'district_case_number')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cc', sa.Column('district_case_number', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_table('cc_district_case_numbers')
    # ### end Alembic commands ###
