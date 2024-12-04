class VotingSystem:
    """Class to manage voting logic."""
    def __init__(self):
        """Initialize the voting system with candidates and votes."""
        self.candidates = {"1": "Bianca", "2": "Edward", "3": "Felicia"}
        self.votes = {"1": 0, "2": 0, "3": 0}

    def cast_vote(self, candidate_id: str) -> str:
        """Register a vote for a given candidate.

        Args:
            candidate_id (str): The ID of the candidate to vote for.

        Returns:
            str: Confirmation message of the vote.

        Raises:
            ValueError: If the candidate ID is invalid.
        """
        if candidate_id in self.candidates:
            self.votes[candidate_id] += 1
            return f"Voted for {self.candidates[candidate_id]}"
        else:
            raise ValueError("Invalid candidate ID. Please select a valid option.")

    def get_results(self) -> str:
        """Get the results of the voting.

        Returns:
            str: A formatted string of vote counts and total votes.
        """
        total_votes = sum(self.votes.values())
        results = [
            f"{self.candidates[candidate_id]} – {votes}"
            for candidate_id, votes in self.votes.items()
        ]
        return "\n".join(results + [f"Total Votes – {total_votes}"])