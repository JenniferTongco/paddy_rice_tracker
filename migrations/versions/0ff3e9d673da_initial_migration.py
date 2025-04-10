"""Initial migration

Revision ID: 0ff3e9d673da
Revises: 
Create Date: 2025-04-10 21:22:23.917355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ff3e9d673da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('full_name', sa.String(length=150), nullable=False),
    sa.Column('role', sa.String(length=50), nullable=False),
    sa.Column('barangay_name', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('farmers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=False),
    sa.Column('middle_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.Column('barangay_name', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('drying_records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(timezone=True), nullable=True),
    sa.Column('batch_name', sa.String(length=150), nullable=False),
    sa.Column('farmer_name', sa.String(length=150), nullable=True),
    sa.Column('initial_weight', sa.Float(), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('humidity', sa.Float(), nullable=False),
    sa.Column('sensor_value', sa.Float(), nullable=False),
    sa.Column('initial_moisture', sa.Float(), nullable=False),
    sa.Column('final_moisture', sa.Float(), nullable=False),
    sa.Column('drying_time', sa.String(length=50), nullable=False),
    sa.Column('final_weight', sa.Float(), nullable=False),
    sa.Column('shelf_life', sa.String(length=50), nullable=True),
    sa.Column('date_dried', sa.Date(), nullable=True),
    sa.Column('date_planted', sa.Date(), nullable=True),
    sa.Column('date_harvested', sa.Date(), nullable=True),
    sa.Column('barangay_name', sa.String(length=150), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('farmer_id', sa.Integer(), nullable=True),
    sa.Column('due_date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['farmer_id'], ['farmers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drying_records')
    op.drop_table('farmers')
    op.drop_table('users')
    # ### end Alembic commands ###
