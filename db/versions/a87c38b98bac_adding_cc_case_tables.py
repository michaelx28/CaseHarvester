"""adding CC case tables

Revision ID: a87c38b98bac
Revises: b2b48b98612f
Create Date: 2018-05-20 18:20:20.552446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a87c38b98bac'
down_revision = 'b2b48b98612f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cc',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('court_system', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('case_type', sa.String(), nullable=True),
    sa.Column('filing_date', sa.Date(), nullable=True),
    sa.Column('filing_date_str', sa.String(), nullable=True),
    sa.Column('case_status', sa.String(), nullable=True),
    sa.Column('case_disposition', sa.String(), nullable=True),
    sa.Column('disposition_date', sa.Date(), nullable=True),
    sa.Column('disposition_date_str', sa.String(), nullable=True),
    sa.Column('district_case_number', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cases.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cc_case_number'), 'cc', ['case_number'], unique=True)
    op.create_table('cc_court_schedule',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('event_type', sa.String(), nullable=True),
    sa.Column('notice_date', sa.Date(), nullable=True),
    sa.Column('notice_date_str', sa.String(), nullable=True),
    sa.Column('event_date', sa.Date(), nullable=True),
    sa.Column('event_date_str', sa.String(), nullable=True),
    sa.Column('event_time', sa.Time(), nullable=True),
    sa.Column('event_time_str', sa.String(), nullable=True),
    sa.Column('result', sa.String(), nullable=True),
    sa.Column('result_date', sa.Date(), nullable=True),
    sa.Column('result_date_str', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_defendants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('party_type', sa.String(), nullable=True),
    sa.Column('party_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('business_org_name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('document_number', sa.Integer(), nullable=True),
    sa.Column('sequence_number', sa.Integer(), nullable=True),
    sa.Column('file_date', sa.Date(), nullable=True),
    sa.Column('file_date_str', sa.String(), nullable=True),
    sa.Column('entered_date', sa.Date(), nullable=True),
    sa.Column('entered_date_str', sa.String(), nullable=True),
    sa.Column('decision', sa.String(), nullable=True),
    sa.Column('party_type', sa.String(), nullable=True),
    sa.Column('party_number', sa.Integer(), nullable=True),
    sa.Column('document_name', sa.String(), nullable=True),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_judgments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entered_date', sa.Date(), nullable=True),
    sa.Column('entered_date_str', sa.String(), nullable=True),
    sa.Column('amount', sa.Numeric(), nullable=True),
    sa.Column('prejudgment_interest', sa.Numeric(), nullable=True),
    sa.Column('appearance_fee', sa.Numeric(), nullable=True),
    sa.Column('filing_fee', sa.Numeric(), nullable=True),
    sa.Column('other_fee', sa.Numeric(), nullable=True),
    sa.Column('service_fee', sa.Numeric(), nullable=True),
    sa.Column('witness_fee', sa.Numeric(), nullable=True),
    sa.Column('attorney_fee', sa.Numeric(), nullable=True),
    sa.Column('total_indexed_judgment', sa.Numeric(), nullable=True),
    sa.Column('comments', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_plaintiffs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('party_type', sa.String(), nullable=True),
    sa.Column('party_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('business_org_name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_related_persons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('party_type', sa.String(), nullable=True),
    sa.Column('party_number', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('business_org_name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_support_orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('version', sa.Integer(), nullable=True),
    sa.Column('order_date', sa.Date(), nullable=True),
    sa.Column('order_date_str', sa.String(), nullable=True),
    sa.Column('obligor', sa.String(), nullable=True),
    sa.Column('effective_date', sa.Date(), nullable=True),
    sa.Column('effective_date_str', sa.String(), nullable=True),
    sa.Column('effective_date_text', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('date_str', sa.String(), nullable=True),
    sa.Column('reason', sa.String(), nullable=True),
    sa.Column('support_amount', sa.Numeric(), nullable=True),
    sa.Column('support_frequency', sa.String(), nullable=True),
    sa.Column('support_to', sa.String(), nullable=True),
    sa.Column('arrears_amount', sa.Numeric(), nullable=True),
    sa.Column('arrears_frequency', sa.String(), nullable=True),
    sa.Column('arrears_to', sa.String(), nullable=True),
    sa.Column('mapr_amount', sa.Numeric(), nullable=True),
    sa.Column('mapr_frequency', sa.String(), nullable=True),
    sa.Column('medical_insurance_report_date', sa.Date(), nullable=True),
    sa.Column('medical_insurance_report_date_str', sa.String(), nullable=True),
    sa.Column('btr_amount', sa.Numeric(), nullable=True),
    sa.Column('btr_frequency', sa.String(), nullable=True),
    sa.Column('lien', sa.String(), nullable=True),
    sa.Column('provisions', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_attorneys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plaintiff_id', sa.Integer(), nullable=True),
    sa.Column('defendant_id', sa.Integer(), nullable=True),
    sa.Column('related_person_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('appearance_date', sa.Date(), nullable=True),
    sa.Column('appearance_date_str', sa.String(), nullable=True),
    sa.Column('practice_name', sa.String(), nullable=True),
    sa.Column('address_1', sa.String(), nullable=True),
    sa.Column('address_2', sa.String(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('zip_code', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['defendant_id'], ['cc_defendants.id'], ),
    sa.ForeignKeyConstraint(['plaintiff_id'], ['cc_plaintiffs.id'], ),
    sa.ForeignKeyConstraint(['related_person_id'], ['cc_related_persons.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_judgments_against',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judgment_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['judgment_id'], ['cc_judgments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cc_judgments_in_favor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judgment_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('case_number', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['case_number'], ['cc.case_number'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['judgment_id'], ['cc_judgments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cc_judgments_in_favor')
    op.drop_table('cc_judgments_against')
    op.drop_table('cc_attorneys')
    op.drop_table('cc_support_orders')
    op.drop_table('cc_related_persons')
    op.drop_table('cc_plaintiffs')
    op.drop_table('cc_judgments')
    op.drop_table('cc_documents')
    op.drop_table('cc_defendants')
    op.drop_table('cc_court_schedule')
    op.drop_index(op.f('ix_cc_case_number'), table_name='cc')
    op.drop_table('cc')
    # ### end Alembic commands ###
