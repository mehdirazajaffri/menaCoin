from celery.utils.log import get_task_logger

from menaCoin.celery import app
from .services import get_current_btc_exchange_rate

logger = get_task_logger(__name__)


@app.task
def get_btc_exchange_rate():
    get_current_btc_exchange_rate()
