"""Update likes

Revision ID: 9561fc7719a8
Revises: 540e3814066f
Create Date: 2021-06-16 13:02:59.907052

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9561fc7719a8'
down_revision = '540e3814066f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pitches', 'dislikes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('dislikes', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
