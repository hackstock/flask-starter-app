from . import admin
from .. import db
from ..models import *

@admin.route('/')
def index():
    return 'Welcome to admin homepage'