from flask import Flask


app = Flask(__name__)

from config import *

from news import *

from index import *

from table_data import *

from authorization import *

from about import *

from partners import *

from authors import *

from error_handlers import *

if __name__ == "__main__":
    app.run(debug=True, port=4040)
    finalize()