import os

import pytest
from flask import current_app
from project.tools.functions import create_tables_

def load_fixtures_():
    with current_app.app_context():
        create_tables_("Fixtures", current_app.config['JSON_PATH'])

if __name__ == '__main__':
    load_fixtures_()
