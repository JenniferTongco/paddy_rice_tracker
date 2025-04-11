"""empty message

Revision ID: 9a5bf5557f43
Revises: 0ff3e9d673da
Create Date: 2025-04-11 13:59:38.149742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a5bf5557f43'
down_revision = '0ff3e9d673da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('municipalities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('barangays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('municipality_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['municipality_id'], ['municipalities.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('barangays')
    op.drop_table('municipalities')
    # ### end Alembic commands ###
