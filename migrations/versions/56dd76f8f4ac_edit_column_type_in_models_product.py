"""edit column type in models.product

Revision ID: 56dd76f8f4ac
Revises: 1e72a829de61
Create Date: 2023-03-17 14:25:17.939181

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56dd76f8f4ac'
down_revision = '1e72a829de61'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('price',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('count',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.alter_column('count',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)
        batch_op.alter_column('price',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
