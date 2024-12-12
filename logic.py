import os

class DuplicateVoterError(Exception):
    """Exception raised when a duplicate voter ID is detected."""
    pass

class VotingSystem:
    """Class to manage voting logic."""
    def __init__(self, voter_log_file: str = "voter_log.txt") -> None:
        """Initialize the voting system with candidates and votes."""
        self.candidates = {"1": "Bianca", "2": "Edward", "3": "Felicia"}
        self.votes = {"1": 0, "2": 0, "3": 0}
        self.voter_log_file = voter_log_file
        if not os.path.exists(self.voter_log_file):
            with open(self.voter_log_file, "w") as file:
                pass

    def cast_vote(self, voter_id: str, candidate_id: str) -> str:
        """Register a vote for a given candidate and raises errors if candidate is invalid or a duplicate voter ID."""
        if not voter_id.isdigit() or len(voter_id) != 6:
            raise ValueError("Voter ID must be exactly 6 numeric characters.")
        if candidate_id not in self.candidates:
            raise ValueError("Invalid candidate ID. Please select a valid option.")

        with open(self.voter_log_file, "r") as file:
            voter_ids = {line.split(":")[1].strip().split(",")[0] for line in file.readlines()}
            if voter_id in voter_ids:
                raise DuplicateVoterError(f"This voter ID ({voter_id}) has already voted.")

        self.votes[candidate_id] += 1
        with open(self.voter_log_file, "a") as file:
            file.write(f"Voter ID: {voter_id}, Candidate Voted For: {self.candidates[candidate_id]}\n")
        return f"Voted for {self.candidates[candidate_id]}"

    def get_results(self) -> str:
        """Get the results of the voting."""
        total_votes = sum(self.votes.values())
        results = [
            f"{self.candidates[candidate_id]} – {votes}"
            for candidate_id, votes in self.votes.items()
        ]
        return "\n".join(results + [f"Total Votes – {total_votes}"])