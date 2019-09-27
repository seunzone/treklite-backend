"""add trip table

Revision ID: f55951b7ffdf
Revises: 989661f20b08
Create Date: 2019-09-27 15:54:04.276844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f55951b7ffdf'
down_revision = '989661f20b08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trips',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('host_id', sa.Integer(), nullable=True),
    sa.Column('estimated_time', sa.String(), nullable=False),
    sa.Column('distance', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('destination_address', sa.String(), nullable=False),
    sa.Column('destination_longitude', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('destination_latitude', sa.Numeric(precision=9, scale=6), nullable=False),
    sa.Column('status', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['host_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trips')
    # ### end Alembic commands ###