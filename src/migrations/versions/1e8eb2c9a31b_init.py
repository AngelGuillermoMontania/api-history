"""init

Revision ID: 1e8eb2c9a31b
Revises: 
Create Date: 2024-05-26 21:14:15.827880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e8eb2c9a31b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('continent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('imagen', sa.String(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('civilizations', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('civilization',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('origen', sa.String(), nullable=True),
    sa.Column('año_inicio', sa.Integer(), nullable=True),
    sa.Column('año_fin', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(), nullable=True),
    sa.Column('logros', sa.String(), nullable=True),
    sa.Column('continent_id', sa.Integer(), nullable=True),
    sa.Column('images', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['continent_id'], ['continent.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('civilization_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['civilization_id'], ['civilization.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('image')
    op.drop_table('civilization')
    op.drop_table('continent')
    # ### end Alembic commands ###