"""initial migration

Revision ID: cd2701baaa58
Revises: 
Create Date: 2024-04-17 13:52:01.417497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd2701baaa58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vex',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('category', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('edge',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_vex_id', sa.Integer(), nullable=False),
    sa.Column('to_vex_id', sa.Integer(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.ForeignKeyConstraint(['from_vex_id'], ['vex.id'], ),
    sa.ForeignKeyConstraint(['to_vex_id'], ['vex.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('edge')
    op.drop_table('vex')
    # ### end Alembic commands ###