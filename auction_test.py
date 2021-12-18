from classes.auction import Auction
from classes.team import Team
import datetime

test_auction = Auction(include_managers=0)

test_auction.get_player_info_from_api()

print(len(test_auction.players))
# print(test_auction.players)
print(test_auction.players[1])

test_auction.add_team("Stuart")
test_auction.add_team("Alex")

test_auction.add_team("Stuart")

target_team = test_auction.teams[0]
print(target_team)
print(test_auction.players[1])
test_auction.add_member_to_team(1, target_team, 5)

print(test_auction.players[1])

target_team = test_auction.teams[1]
print(target_team)
print(test_auction.players[487])
test_auction.add_member_to_team(487, target_team, 9)

for team in test_auction.teams:
    print(team)
    print("****************")

print(test_auction.transaction_log)
print(datetime.datetime.utcnow())

test_auction.nominate_player(2)

