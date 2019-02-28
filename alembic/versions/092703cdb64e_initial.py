"""initial

Revision ID: 092703cdb64e
Revises: 
Create Date: 2019-02-28 19:11:32.614608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '092703cdb64e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat_rates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('currencies', sa.Text(), nullable=False),
    sa.Column('cnt', sa.Integer(), server_default='0', nullable=False),
    sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('chat_id', 'currencies')
    )
    op.create_index(op.f('ix_chat_rates_chat_id'), 'chat_rates', ['chat_id'], unique=False)
    op.create_index(op.f('ix_chat_rates_cnt'), 'chat_rates', ['cnt'], unique=False)
    op.create_table('chats',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('is_subscribed', sa.Boolean(), server_default='true', nullable=False),
    sa.Column('is_console_mode', sa.Boolean(), server_default='true', nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('event', sa.Text(), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_chat_id'), 'events', ['chat_id'], unique=False)
    op.create_index(op.f('ix_events_event'), 'events', ['event'], unique=False)
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('tag', sa.Text(), nullable=True),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_messages_chat_id'), 'messages', ['chat_id'], unique=False)
    op.create_index(op.f('ix_messages_created'), 'messages', ['created'], unique=False)
    op.create_index(op.f('ix_messages_user_id'), 'messages', ['user_id'], unique=False)
    op.create_table('notifications',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.BigInteger(), nullable=False),
    sa.Column('currencies', sa.Text(), nullable=False),
    sa.Column('clause', sa.Enum('more', 'less', 'diff', 'percent', name='notification_clause'), nullable=False),
    sa.Column('value', sa.Numeric(precision=14, scale=6), nullable=False),
    sa.Column('last_rate', sa.Numeric(precision=14, scale=6), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_notifications_chat_id'), 'notifications', ['chat_id'], unique=False)
    op.create_table('rates',
    sa.Column('currency', sa.CHAR(length=3), nullable=False),
    sa.Column('rate_open', sa.Numeric(precision=14, scale=6), nullable=False),
    sa.Column('rate', sa.Numeric(precision=14, scale=6), nullable=False),
    sa.Column('source', sa.Text(), nullable=False),
    sa.Column('weight', sa.Integer(), server_default='0', nullable=False),
    sa.Column('last_trade_at', sa.TIMESTAMP(), nullable=False),
    sa.Column('created', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated', sa.TIMESTAMP(), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('currency')
    )
    op.create_index(op.f('ix_rates_weight'), 'rates', ['weight'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_rates_weight'), table_name='rates')
    op.drop_table('rates')
    op.drop_index(op.f('ix_notifications_chat_id'), table_name='notifications')
    op.drop_table('notifications')
    op.drop_index(op.f('ix_messages_user_id'), table_name='messages')
    op.drop_index(op.f('ix_messages_created'), table_name='messages')
    op.drop_index(op.f('ix_messages_chat_id'), table_name='messages')
    op.drop_table('messages')
    op.drop_index(op.f('ix_events_event'), table_name='events')
    op.drop_index(op.f('ix_events_chat_id'), table_name='events')
    op.drop_table('events')
    op.drop_table('chats')
    op.drop_index(op.f('ix_chat_rates_cnt'), table_name='chat_rates')
    op.drop_index(op.f('ix_chat_rates_chat_id'), table_name='chat_rates')
    op.drop_table('chat_rates')
    # ### end Alembic commands ###