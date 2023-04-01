import os
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger

class PdfMergerGUI:
    def __init__(self, master):
        self.master = master
        master.title("PDF Merger")

        # create file directory label and button
        self.directory_label = tk.Label(master, text="Select directory containing PDF files:")
        self.directory_label.grid(row=0, column=0, padx=10, pady=10)
        self.directory_button = tk.Button(master, text="Select", command=self.select_directory)
        self.directory_button.grid(row=0, column=1, padx=10, pady=10)

        # create file name label and entry
        self.filename_label = tk.Label(master, text="Enter output file name (including .pdf extension):")
        self.filename_label.grid(row=1, column=0, padx=10, pady=10)
        self.filename_entry = tk.Entry(master)
        self.filename_entry.grid(row=1, column=1, padx=10, pady=10)

        # create merge button
        self.merge_button = tk.Button(master, text="Merge PDFs", command=self.merge_pdfs)
        self.merge_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def select_directory(self):
        self.directory = filedialog.askdirectory()

    def merge_pdfs(self):
        # get selected directory and output file name
        directory = self.directory
        filename = self.filename_entry.get()

        # initialize a PdfMerger object
        pdf_merger = PdfMerger()

        # loop through all PDF files in the directory and add them to the merger
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                filepath = os.path.join(directory, filename)
                pdf_merger.append(open(filepath, 'rb'))

        # write the merged PDF to a file
        with open(filename, 'wb') as output_file:
            pdf_merger.write(output_file)

        # close all input PDF files
        pdf_merger.close()

        # show success message
        success_message = f"PDFs merged successfully and saved to {filename}"
        tk.messagebox.showinfo(title="Success", message=success_message)

root = tk.Tk()
pdf_merger_gui = PdfMergerGUI(root)
root.mainloop()
