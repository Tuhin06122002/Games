import tkinter as tk
from tkinter import ttk

class MnFrm(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.isComplete = tk.IntVar()
        self.isComplete.set(0)

        self.mat=[]
        for i in range(9):
            arr=[]
            for j in range(9):
                arr.append(tk.IntVar())
            self.mat.append(arr)

        self.inputMat=[]
        for i in range(9):
            arr=[]
            for j in range(9):
                arr.append(ttk.Spinbox(self, from_=0, to=9, increment=1, textvariable=self.mat[i][j]))
            self.inputMat.append(arr)

        for i in range(9):
            for j in range(9):
                self.inputMat[i][j].grid(row=i+1, column=j)
        
        solveButton = ttk.Button(self, text = "Solve It", command=self.solve)
        solveButton.grid(row=0,column=0,columnspan=9)

        resetButton = ttk.Button(self, text = "Reset", command=self.reset)
        resetButton.grid(row=10,column=0,columnspan=9)

        for i in range(9):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i+1,weight=1)
    
    def reset(self):
        for i in range(9):
            for j in range(9):
                self.mat[i][j].set(0)
        self.isComplete.set(0)

    def isPossible(self,x,y,n):
        for i in range(9):
            if self.mat[y][i].get()==n:
                return 0
            if self.mat[i][x].get()==n:
                return 0

        xf = (x//3)*3
        yf = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.mat[yf+i][xf+j].get()==n:
                    return 0
    
        return 1

    def solve(self):
        if self.isComplete.get() == 1:
            return
        for y in range(9):
            for x in range(9):
                if self.mat[y][x].get()==0:
                    for n in range(1,10):
                        if self.isPossible(x,y,n):
                            self.mat[y][x].set(n)
                            self.solve()
                            if self.isComplete.get() == 1:
                                return
                            self.mat[y][x].set(0)
                    return
        self.isComplete.set(1)
        return

class myApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Sudoku")
        self.geometry("1250x230")
        self.resizable(width=False, height=False)

        self.gridFrm=MnFrm(self)
        self.gridFrm.grid(row=0, column=0)
        
if __name__=="__main__":
    myApplication().mainloop()