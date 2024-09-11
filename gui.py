from tkinter import *
from scapy.all import *
from scapy.layers.inet import IP, ICMP
import threading

global status

count = 1


def main():
    # Main window configs
    root = Tk()

    def icmp_flood(on_or_off):
        while True:
            print(on_or_off)
            if on_or_off == "01":
                quit()
            #flood = IP(dst="192.168.4.47")/ICMP(type=9)
            #send(flood)


    def switch(event):
        global count
        on_or_off = count % 2
        count += 1
        if on_or_off == 1:
            status.config(text="Enabled", fg="green")
            thread = threading.Thread(target=icmp_flood, args=(str(on_or_off)))
            thread.start()
        elif on_or_off == 0:
            status.config(text="Disabled", fg="red")
            icmp_flood(str(on_or_off))


    root.geometry("480x200")
    root.config(bg="black")
    root.title("DOS")
    root.iconbitmap("favicon.ico")

    # Widgets
    filler = Label(bg="black", padx=90, pady=22)
    filler2 = Label(bg="black", padx=0)
    filler3 = Label(bg="black")
    creator_info = Label(text="DOS | Made by 0x4155", fg="white", bg="black")
    status = Label(text="Disabled", bg="black", fg="red")
    start = Button(text="Start/Stop")

    start.bind("<Button-1>", switch)
    ip = Entry()
    ip_label = Label(text="Destination IP: ", bg="black", fg="white")

    # Packed widgets
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
