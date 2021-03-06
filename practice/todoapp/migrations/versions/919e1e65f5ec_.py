"""empty message

Revision ID: 919e1e65f5ec
Revises: d689e982d338
Create Date: 2020-06-12 00:51:57.057096

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919e1e65f5ec'
down_revision = 'd689e982d338'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
