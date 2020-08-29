token = 'HH0KrCdBFbKpmPgS'
import berserk

session = berserk.TokenSession(token)
client = berserk.Client(session)
res = client.board.seek(3, 2)
print(res)
# for state in client.board.stream_game_state('hROJhUvS7Ee4'):
#     print(state)