"""init migrate

Revision ID: 1e72a829de61
Revises: 
Create Date: 2023-03-17 13:57:31.877432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e72a829de61'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('file_name', sa.String(), nullable=True))
        batch_op.drop_column('description')
        batch_op.drop_column('image')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image', sa.VARCHAR(length=128), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True))
        batch_op.drop_column('file_name')

    # ### end Alembic commands ###