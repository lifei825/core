from core import app
from imports import *

app.register_blueprint(net)
app.register_blueprint(os)
app.register_blueprint(user)
app.register_blueprint(process)
app.register_blueprint(mem)
app.register_blueprint(disk)
app.register_blueprint(cpu)
