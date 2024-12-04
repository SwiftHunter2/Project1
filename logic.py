class VotingSystem:
    def __init__(self):
        self.candidates = {"1": "Bianca", "2": "Edward", "3": "Felicia"}
        self.votes = {"1": 0, "2": 0, "3": 0}

    def cast_vote(self, candidate_id: str) -> str:
        if candidate_id in self.candidates:
            self.votes[candidate_id] += 1
            return f"Voted for {self.candidates[candidate_id]}"
        else:
            raise ValueError("Invalid candidate ID. Please select a valid option.")

    def get_results(self) -> str:
        total_votes = sum(self.votes.values())
        results = [
            f"{self.candidates[candidate_id]} – {votes}"
            for candidate_id, votes in self.votes.items()
        ]
        return "\n".join(results + [f"Total Votes – {total_votes}"])