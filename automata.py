from typing import List
from sys import exit as error


class DFA:
    initial_state: str
    final_states: List[str]
    other_states: List[str]
    all_states: List[str]
    transitions: List[List]

    @staticmethod
    def _input_list(msg: str) -> List[str]:
        lst = []
        entered_list = input(msg).split(',')
        for item in entered_list:
            stripped_item = item.strip()
            if stripped_item != '':
                lst.append(stripped_item)
        return lst

    def _input_transition(self, state: str) -> List[List]:
        def _input_state(val: int):
            state_val = input(f"\tState '{state}' on input {val} goes to -> ")
            if state_val not in self.all_states:
                error("ERROR: Please enter a valid state value. [State does not exist]!")
            return [state, val, state_val]

        state_0 = _input_state(0)
        state_1 = _input_state(1)

        return [state_0, state_1]

    def __init__(self, name: str) -> None:
        self.initial_state = input(f"Enter {name} DFA's initial state: ").strip()
        if not self.initial_state:
            error("ERROR: Initial state not valid!")

        self.final_states = self._input_list(f"Enter {name} DFA's final states separated by commas: ")
        self.other_states = self._input_list(f"Enter {name} DFA's all other states separated by commas: ")

        self.all_states = sorted([*{self.initial_state, *self.final_states, *self.other_states}])

        if not self.final_states:
            error("ERROR: DFA must have at least one final state!")

        for state in self.other_states:
            if state == self.initial_state or state in self.final_states:
                error("ERROR: Please input a valid DFA with the appropriate states!")

        self.transitions = []
        print(f"Enter {name} DFA's transitions:")
        for state in self.all_states:
            self.transitions.append(self._input_transition(state))


def check_equivalence(dfa1: DFA, dfa2: DFA) -> bool:
    if len(dfa1.final_states) != len(dfa2.final_states):
        return False
    else:
        transitions_len = min(len(dfa1.transitions), len(dfa2.transitions))

        for idx in range(transitions_len):
            dfa1_transition = dfa1.transitions[idx]
            dfa2_transition = dfa2.transitions[idx]

            if (dfa1_transition[0][2] in dfa1.final_states) != (dfa2_transition[0][2] in dfa2.final_states):
                return False

            if (dfa1_transition[1][2] in dfa1.final_states) != (dfa2_transition[1][2] in dfa2.final_states):
                return False

        return True


if __name__ == '__main__':
    dfa_1 = DFA('1st')
    dfa_2 = DFA('2nd')

    is_equivalent = check_equivalence(dfa_1, dfa_2)
    print(f"\nThe 2 DFA's are {'' if is_equivalent else 'non-'}equivalent!")

    input()
