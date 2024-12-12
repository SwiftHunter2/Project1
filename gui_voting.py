from tkinter import *
from logic import *

class VotingGUI:
    """Graphical User Interface for the Voting System."""
    def __init__(self, window: Tk):
        """Initialize the GUI and display the main menu."""
        self.voting_system = VotingSystem()
        self.window = window
        self.window.geometry("400x500")
        self.window.title("Voting System")
        self.last_vote_message = None
        self.main_menu()

    def main_menu(self) -> None:
        """Display the main menu with options to vote or exit."""
        self.clear_window()
        Label(self.window, text="Voting System Menu", font=("Arial", 20, "bold")).pack(pady=20)

        if self.last_vote_message:
            Label(self.window, text=self.last_vote_message, font=("Arial", 12), fg="green").pack(pady=10)

        Button(self.window, text="Vote", command=self.vote_menu, width=20, height=2).pack(pady=10)
        Button(self.window, text="Exit", command=self.show_results, width=20, height=2).pack(pady=10)

    def vote_menu(self) -> None:
        """Display the voting menu to input voter ID and select a candidate."""
        self.clear_window()
        self.last_vote_message = None
        Label(self.window, text="Enter Voter ID (Numbers Only):", font=("Arial", 12)).pack(pady=10)
        self.voter_id_entry = Entry(self.window, width=25)
        self.voter_id_entry.pack(pady=5)
        Label(self.window, text="Select a Candidate:", font=("Arial", 14)).pack(pady=10)
        self.selected_candidate = StringVar(value="4")
        Radiobutton(self.window, text="Bianca", variable=self.selected_candidate, value="1").pack(anchor="w")
        Radiobutton(self.window, text="Edward", variable=self.selected_candidate, value="2").pack(anchor="w")
        Radiobutton(self.window, text="Felicia", variable=self.selected_candidate, value="3").pack(anchor="w")
        Button(self.window, text="Vote", command=self.cast_vote, width=15).pack(pady=5)
        Button(self.window, text="Back to Menu", command=self.main_menu, width=15).pack(pady=5)
        self.output_label = Label(self.window, text="", font=("Arial", 12))
        self.output_label.pack(pady=10)

    def cast_vote(self) -> None:
        """Cast a vote for the selected candidate and return to the main menu."""
        voter_id = self.voter_id_entry.get()
        candidate_id = self.selected_candidate.get()
        try:
            if not voter_id.isdigit():
                raise ValueError("Voter ID must be numbers only.")
            self.last_vote_message = self.voting_system.cast_vote(voter_id, candidate_id)
            self.main_menu()
        except ValueError as e:
            self.output_label.config(text=str(e), fg="red")
        except DuplicateVoterError as e:
            self.output_label.config(text=str(e), fg="orange")

    def show_results(self) -> None:
        """Display the voting results and a button to close the application."""
        self.clear_window()
        results = self.voting_system.get_results()
        Label(self.window, text="Voting Results:", font=("Arial", 16)).pack(pady=10)
        Label(self.window, text=results, justify=LEFT, font=("Arial", 12)).pack(pady=10)
        Button(self.window, text="Close", command=self.window.quit, width=15).pack(pady=10)

    def clear_window(self) -> None:
        """Clear all widgets from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()