class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0

            losses[loser] = losses.get(loser, 0) + 1
        no_loss = []
        one_loss = []

        for player, loss_count in losses.items():
            if loss_count == 0:
                no_loss.append(player)
            elif loss_count == 1:
                one_loss.append(player)

        return [sorted(no_loss), sorted(one_loss)]
