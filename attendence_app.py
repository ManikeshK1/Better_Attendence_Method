import customtkinter as ctk
import pandas as pd
from datetime import datetime
import os

class AttendanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Attendance System")
        self.geometry("600x500")
        ctk.set_appearance_mode("dark")
        
        # Load or Create Local Database
        self.file_path = "attendance_records1.xlsx"
        self.date_col = datetime.now().strftime("%m/%d")
        self.init_excel()

        # UI Setup
        self.label = ctk.CTkLabel(self, text=f"Marking for: {self.date_col}", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.cse_box = self.create_input_group("CSE (23BCS...)")
        self.dsai_box = self.create_input_group("DSAI (23BDS...)")
        self.ece_box = self.create_input_group("ECE (23BEC...)")

        self.submit_btn = ctk.CTkButton(self, text="Submit Attendance", command=self.submit, fg_color="#2ecc71", hover_color="#27ae60")
        self.submit_btn.pack(pady=30)

    def init_excel(self):
        if not os.path.exists(self.file_path):
            # Create dummy structure if file doesn't exist
            df = pd.DataFrame(columns=["Roll No", "Student Name"])
            df.to_excel(self.file_path, index=False)

    def create_input_group(self, label_text):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=10, padx=50, fill="x")
        lbl = ctk.CTkLabel(frame, text=label_text)
        lbl.pack(side="left", padx=10)
        entry = ctk.CTkEntry(frame, placeholder_text="e.g. 1 12 34")
        entry.pack(side="right", fill="x", expand=True)
        return entry

    def submit(self):
        df = pd.read_excel(self.file_path)
        if self.date_col not in df.columns:
            df[self.date_col] = 0
        
        branch_map = {"23BCS": self.cse_box.get(), "23BDS": self.dsai_box.get(), "23BEC": self.ece_box.get()}
        
        for prefix, vals in branch_map.items():
            for r in vals.split():
                full_roll = f"{prefix}{r.zfill(3)}"
                if full_roll in df['Roll No'].values:
                    df.loc[df['Roll No'] == full_roll, self.date_col] = 1
                else:
                    print(f"Roll {full_roll} not found in Excel.")

        df.to_excel(self.file_path, index=False)
        print("Attendance Saved Locally!")

if __name__ == "__main__":
    app = AttendanceApp()
    app.mainloop()