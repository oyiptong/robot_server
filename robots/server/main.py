#!/usr/bin/env python
import os
import json
import logging

import tornado.options
from tornado.options import define, options
import tornado.ioloop
import tornado.web as web
import tornado.websocket as websocket
import tornado.gen as gen
import tornado.template as template

robot_state = {
        "cutter": True,
        "light": True,
        "notification": True,
        "wheels" : {
            "left": 0,
            "right": 0,
        },
        "camera" : 0
}

class UIHandler(web.RequestHandler):
    @web.asynchronous
    @gen.engine
    def get(self):
        self.render("../robots/server/templates/index.html")

class InputSocketHandler(websocket.WebSocketHandler):
    def open(self):
        logging.info("WebSocket opened")

    def on_message(self, message):
        input = json.loads(message)
        logging.info("message: {0}".format(message))

        global robot_state

        # switches
        if input.has_key("cutter") and input["cutter"] in [True, False]:
            robot_state["cutter"] = input["cutter"]
        if input.has_key("light") and input["light"] in [True, False]:
            robot_state["light"] = input["light"]
        if input.has_key("notification") and input["notification"] in [True, False]:
            robot_state["notification"] = input["notification"]

        # wheels
        if input.has_key("wheels") and input["wheels"].has_key("left") and input["wheels"]["left"] >= 0 and input["wheels"]["left"] <= 255:
            robot_state["wheels"]["left"] = input["wheels"]["left"]

        if input.has_key("wheels") and input["wheels"].has_key("right") and input["wheels"]["right"] >= 0 and input["wheels"]["right"] <= 255:
            robot_state["wheels"]["right"] = input["wheels"]["right"]

        if input.has_key("camera") and input["camera"] >= 0 and input["camera"] <= 180:
            robot_state["camera"] = input["camera"]

        self.write_message(json.dumps(robot_state))

    def on_close(self):
        logging.info("WebSocket closed")

class OutputHandler(web.RequestHandler):
    @web.asynchronous
    @gen.engine
    def get(self):
        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(robot_state, indent=4))
        self.finish()

class Static(web.StaticFileHandler):
    def get(self, path, include_body=True):
        super(Static, self).get(path, include_body)


define("port", help="run on the given port", type=int)
define("debug", help="debug switch", type=bool)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    port = options.port or 8888
    debug = options.debug
    logging.info("robot-server listening on port {0}".format(port))
    application = tornado.web.Application([
        (r"/robot_server/?", UIHandler),
        (r"/robot_server/commands/?", InputSocketHandler),
        (r"/robot_server/out.json", OutputHandler),
        (r'/robot_server/static/(.*)', Static, {'path' : os.path.join(os.path.dirname(os.path.abspath(__file__)), '../robots/server/static')}),
        ], debug=debug)
    application.listen(port)
    tornado.ioloop.IOLoop.instance().start()
