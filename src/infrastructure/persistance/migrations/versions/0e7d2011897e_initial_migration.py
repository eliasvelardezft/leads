"""initial migration

Revision ID: 0e7d2011897e
Revises: 
Create Date: 2023-10-10 17:18:44.560488

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0e7d2011897e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(), nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('province', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_deleted_date'), 'address', ['deleted_date'], unique=False)
    op.create_table('career',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_career_deleted_date'), 'career', ['deleted_date'], unique=False)
    op.create_index(op.f('ix_career_name'), 'career', ['name'], unique=False)
    op.create_table('subject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subject_deleted_date'), 'subject', ['deleted_date'], unique=False)
    op.create_index(op.f('ix_subject_name'), 'subject', ['name'], unique=True)
    op.create_table('career_subject_association',
    sa.Column('career_id', sa.Integer(), nullable=True),
    sa.Column('subject_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['career_id'], ['career.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], )
    )
    op.create_table('course',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('professor', sa.String(), nullable=False),
    sa.Column('classroom', sa.String(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_course_deleted_date'), 'course', ['deleted_date'], unique=False)
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('address_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['address_id'], ['address.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_person_deleted_date'), 'person', ['deleted_date'], unique=False)
    op.create_index(op.f('ix_person_email'), 'person', ['email'], unique=True)
    op.create_table('lead',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year_of_inscription', sa.Integer(), nullable=False),
    sa.Column('career_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['career_id'], ['career.id'], ),
    sa.ForeignKeyConstraint(['id'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('enrollment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('subject_times_taken', sa.Integer(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], ),
    sa.ForeignKeyConstraint(['lead_id'], ['lead.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_enrollment_deleted_date'), 'enrollment', ['deleted_date'], unique=False)
    op.create_table('status_change',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('created', 'progress', 'completed', 'failed', 'dropped', name='enrollment_status_enum'), nullable=False),
    sa.Column('enrollment_id', sa.Integer(), nullable=False),
    sa.Column('created_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('deleted_date', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['enrollment_id'], ['enrollment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_status_change_deleted_date'), 'status_change', ['deleted_date'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_status_change_deleted_date'), table_name='status_change')
    op.drop_table('status_change')
    op.drop_index(op.f('ix_enrollment_deleted_date'), table_name='enrollment')
    op.drop_table('enrollment')
    op.drop_table('lead')
    op.drop_index(op.f('ix_person_email'), table_name='person')
    op.drop_index(op.f('ix_person_deleted_date'), table_name='person')
    op.drop_table('person')
    op.drop_index(op.f('ix_course_deleted_date'), table_name='course')
    op.drop_table('course')
    op.drop_table('career_subject_association')
    op.drop_index(op.f('ix_subject_name'), table_name='subject')
    op.drop_index(op.f('ix_subject_deleted_date'), table_name='subject')
    op.drop_table('subject')
    op.drop_index(op.f('ix_career_name'), table_name='career')
    op.drop_index(op.f('ix_career_deleted_date'), table_name='career')
    op.drop_table('career')
    op.drop_index(op.f('ix_address_deleted_date'), table_name='address')
    op.drop_table('address')
    # ### end Alembic commands ###
