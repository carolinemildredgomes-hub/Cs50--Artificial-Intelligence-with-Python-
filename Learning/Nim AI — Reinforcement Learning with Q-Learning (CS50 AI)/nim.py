import math
import random
import time


class Nim():

    def __init__(self, initial=[1, 3, 5, 7]):
        """
        Initialize game board.
        Each game board has
            - piles: a list containing the number of objects in each pile
            - player: 0 or 1 indicating whose turn it is
            - winner: None until someone wins
        """

        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    @classmethod
    def available_actions(cls, piles):
        """
        Return a set of all possible actions.

        Each action is represented as a tuple:
            (pile_index, number_to_remove)
        """

        actions = set()

        for i, pile in enumerate(piles):
            for j in range(1, pile + 1):
                actions.add((i, j))

        return actions

    @classmethod
    def other_player(cls, player):
        """
        Return the other player.
        """

        return 0 if player == 1 else 1

    def switch_player(self):
        """
        Switch the current player.
        """

        self.player = Nim.other_player(self.player)

    def move(self, action):
        """
        Apply an action to the game.

        Action is a tuple:
            (pile, count)
        """

        pile, count = action

        if self.winner is not None:
            raise Exception("Game already won")

        elif pile < 0 or pile >= len(self.piles):
            raise Exception("Invalid pile")

        elif count < 1 or count > self.piles[pile]:
            raise Exception("Invalid number of objects")

        # Remove objects
        self.piles[pile] -= count

        # Switch players
        self.switch_player()

        # Check whether all piles are empty
        if all(pile == 0 for pile in self.piles):
            self.winner = self.player


class NimAI():

    def __init__(self, alpha=0.5, epsilon=0.1):
        """
        Initialize AI with an empty Q-learning dictionary,
        an alpha (learning) rate, and an epsilon rate.

        The Q-learning dictionary maps (state, action)
        pairs to a Q-value.

        state: tuple of remaining piles
        action: tuple (pile, count)
        """

        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state, action, new_state, reward):
        """
        Update Q-learning model after taking an action.
        """

        old = self.get_q_value(old_state, action)

        best_future = self.best_future_reward(new_state)

        self.update_q_value(
            old_state,
            action,
            old,
            reward,
            best_future
        )

    def get_q_value(self, state, action):
        """
        Return the Q-value for the state and action.

        If no Q-value exists, return 0.
        """

        return self.q.get((tuple(state), action), 0)

    def update_q_value(self, state, action, old_q, reward, future_rewards):
        """
        Update the Q-value for the state `state` and the action `action`
        given the previous Q-value `old_q`, a current reward `reward`,
        and an estimate of future rewards `future_rewards`.

        Use the formula:

        Q(s, a) <- old value estimate
                   + alpha * (new value estimate - old value estimate)

        where the new value estimate is:
            reward + future_rewards
        """

        new_estimate = reward + future_rewards

        new_q = old_q + self.alpha * (new_estimate - old_q)

        self.q[(tuple(state), action)] = new_q

    def best_future_reward(self, state):
        """
        Given a state, return the highest Q-value of any available action.

        Use 0 as the Q-value if a state-action pair has not been seen before.

        If there are no available actions, return 0.
        """

        actions = Nim.available_actions(state)

        if not actions:
            return 0

        return max(
            self.get_q_value(state, action)
            for action in actions
        )

    def choose_action(self, state, epsilon=True):
        """
        Given a state, return an action (i, j).

        If epsilon is False, always choose the best action.

        If epsilon is True, use the epsilon-greedy strategy:
        - choose a random action with probability epsilon
        - otherwise choose the best action
        """

        actions = list(Nim.available_actions(state))

        if not actions:
            return None

        best_action = max(
            actions,
            key=lambda action: self.get_q_value(state, action)
        )

        if not epsilon:
            return best_action

        if random.random() < self.epsilon:
            return random.choice(actions)

        return best_action


def train(n):
    """
    Train an AI by playing `n` games against itself.
    """

    player = NimAI()

    # Play n games
    for i in range(n):

        print(f"Playing training game {i + 1}")

        game = Nim()

        # Keep track of each player's last move
        last = {
            0: {"state": None, "action": None},
            1: {"state": None, "action": None}
        }

        # Game loop
        while True:

            # Current state
            state = game.piles.copy()

            # AI chooses an action
            action = player.choose_action(game.piles)

            # Save last move
            last[game.player]["state"] = state
            last[game.player]["action"] = action

            # Apply action
            game.move(action)

            # New state
            new_state = game.piles.copy()

            # If game finished
            if game.winner is not None:

                # Losing move
                player.update(
                    state,
                    action,
                    new_state,
                    -1
                )

                # Winning move
                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    1
                )

                break

            # Otherwise continue learning
            elif last[game.player]["state"] is not None:

                player.update(
                    last[game.player]["state"],
                    last[game.player]["action"],
                    new_state,
                    0
                )

    print("Done training")

    return player


def play(ai, human_player=None):
    """
    Play human game against the AI.
    """

    # Randomly choose who goes first
    if human_player is None:
        human_player = random.randint(0, 1)

    game = Nim()

    while True:

        print()
        print("Piles:")

        for i, pile in enumerate(game.piles):
            print(f"Pile {i}: {pile}")

        print()

        available_actions = Nim.available_actions(game.piles)

        time.sleep(1)

        # Human turn
        if game.player == human_player:

            print("Your Turn")

            while True:

                pile = int(input("Choose Pile: "))
                count = int(input("Choose Count: "))

                if (pile, count) in available_actions:
                    break

                print("Invalid move, try again.")

        # AI turn
        else:

            print("AI's Turn")

            pile, count = ai.choose_action(
                game.piles,
                epsilon=False
            )

            print(f"AI chose to take {count} from pile {pile}.")

        # Apply move
        game.move((pile, count))

        # Check for winner
        if game.winner is not None:

            print()
            print("GAME OVER")

            winner = "Human" if game.winner == human_player else "AI"

            print(f"Winner is {winner}")

            return
