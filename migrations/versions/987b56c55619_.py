"""empty message

Revision ID: 987b56c55619
Revises: 70260cd4c39e
Create Date: 2025-04-10 15:45:47.523211

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '987b56c55619'
down_revision = '70260cd4c39e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('farmers', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('farmers', sa.Column('timestamp', sa.DATETIME(), nullable=True))
    # ### end Alembic commands ###
