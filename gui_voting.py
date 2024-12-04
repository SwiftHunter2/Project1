from tkinter import *
from logic import *

class VotingGUI:
    """Graphical User Interface for the Voting System."""
    def __init__(self, window):
        """Initialize the GUI and display the main menu."""
        self.voting_system = VotingSystem()
        self.window = window
        self.window.geometry("300x400")
        self.window.title("Voting System")
        self.main_menu()

    def main_menu(self) -> None:
        """Display the main menu with options to vote or exit."""
        self.clear_window()
        Label(self.window, text="Voting System Menu", font=("Times New Roman", 20, "bold")).pack(pady=20)
        Button(self.window, text="Vote", command=self.vote_menu, width=20, height=2).pack(pady=10)
        Button(self.window, text="Exit", command=self.show_results, width=20, height=2).pack(pady=10)

    def vote_menu(self) -> None:
        """Display the voting menu to select a candidate."""
        self.clear_window()
        Label(self.window, text="Select a Candidate:", font=("Times New Roman", 16)).pack(pady=10)

        self.selected_candidate = StringVar(value="4")  # Ensures no pre-selection of candidates
        Radiobutton(self.window, text="Bianca", variable=self.selected_candidate, value="1").pack(anchor="w")
        Radiobutton(self.window, text="Edward", variable=self.selected_candidate, value="2").pack(anchor="w")
        Radiobutton(self.window, text="Felicia", variable=self.selected_candidate, value="3").pack(anchor="w")

        Button(self.window, text="Vote", command=self.cast_vote, width=15).pack(pady=5)
        Button(self.window, text="Back to Menu", command=self.main_menu, width=15).pack(pady=5)
        self.output_label = Label(self.window, text="", fg="blue", font=("Times New Roman", 12))
        self.output_label.pack(pady=10)

    def cast_vote(self) -> None:
        """Cast a vote for the selected candidate and return to the main menu."""
        candidate_id = self.selected_candidate.get()
        try:
            message = self.voting_system.cast_vote(candidate_id)
            self.output_label.config(text=message)
            self.window.after(1000, self.main_menu)  # Return to main menu after 1.5 seconds
        except ValueError as e:
            self.output_label.config(text=str(e))

    def show_results(self) -> None:
        """Display the voting results and a button to close the application."""
        self.clear_window()
        results = self.voting_system.get_results()
        Label(self.window, text="Voting Results:", font=("Times New Roman", 16)).pack(pady=10)
        Label(self.window, text=results, justify=LEFT, font=("Times New Roman", 12)).pack(pady=10)
        Button(self.window, text="Close", command=self.window.quit, width=15).pack(pady=10)

    def clear_window(self) -> None:
        """Clear all widgets from the window."""
        for widget in self.window.winfo_children():
            widget.destroy()