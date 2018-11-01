from tkinter.ttk import Frame, Button
from tkinter import Tk, BOTH, messagebox as mbox


class membuatPeringatan(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.window = parent
        self.initUI()

    def initUI(self):
        self.window.title("Message box")
        self.window.geometry("300x150")

        self.pack()
        self.buatTombol()

    def buatTombol(self):
        pesanError = Button(self, text="Error", command=self.tampilError)
        pesanError.grid(padx=5, pady=5)
        pesanPeringatan = Button(self, text="Peringatan", command=self.tampilPeringatan)
        pesanPeringatan.grid(row=1, column=0)
        pesanPertanyaan = Button(self, text="pertanyaan", command=self.tampilPertanyaan)
        pesanPertanyaan.grid(row=0, column=1)
        pesanInformasi = Button(self, text="infromasi", command=self.tampilInfromasi)
        pesanInformasi.grid(row=1, column=1)

    def tampilError(self):
        mbox.showerror("Error", "Maaf ada yang Error.")

    def tampilPeringatan(self):
        mbox.showwarning("Warning", "Di aplikasi ini ada peringatan.")

    def tampilPertanyaan(self):
        mbox.askquestion("Question", "Kalian sudah makan ?")

    def tampilInfromasi(self):
        mbox.showinfo("Information", "Aplikasi sukses di buat.")


if __name__ == '__main__':
    root = Tk()
    ex = membuatPeringatan(root)
    root.mainloop()
