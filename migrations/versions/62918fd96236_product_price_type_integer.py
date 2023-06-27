"""Product.price type Integer

Revision ID: 62918fd96236
Revises: 675d42bd4a85
Create Date: 2023-06-27 19:52:37.715762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62918fd96236'
down_revision = '675d42bd4a85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.VARCHAR(),
               type_=sa.Integer(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.Integer(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###