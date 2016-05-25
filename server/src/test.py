# from flask import Flask
# import pusher
# app = Flask(__name__)
#
# pusher_client = pusher.Pusher(
#   app_id='209391',
#   key='3a07e26ad5dafe9ae4ca',
#   secret='cc88a22eaeea4ed58b9a',
#   ssl=True
# )
#
#
# @app.route("/")
# def main():
#     sum = 0
#     pusher_client.trigger('abacus_channel', 'updated', sum)
#     #return str(sum)
#
# if __name__ == "__main__":
#     app.run()

import pusher

pusher_client = pusher.Pusher(
  app_id='209391',
  key='3a07e26ad5dafe9ae4ca',
  secret='cc88a22eaeea4ed58b9a',
  ssl=True
)

while(True):
    sum = 0
    pusher_client.trigger('abacus_channel', 'updated', sum)