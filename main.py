from tkinter import *
from tkinter import messagebox
import base64

root = Tk()
root.geometry("1200x600")
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=800, relief=SUNKEN)
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'), text="SECRET MESSAGING \n Vigenère Cipher", fg="Black", bd=10, anchor='w')
lblInfo.grid(row=0, column=0)

Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# Function to display tips on input
def set_default_text(entry, default_text):
    entry.insert(0, default_text)
    entry.config(fg="grey")

def clear_default_text(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, END)
        entry.config(fg="black")

def on_focus_out(event, entry, default_text):
    if not entry.get():
        set_default_text(entry, default_text)

# Entry for message
lblMsg = Label(f1, font=('arial', 16, 'bold'), text="MESSAGE", bd=16, anchor="w")
lblMsg.grid(row=1, column=0)
txtMsg = Entry(f1, font=('arial', 16, 'bold'), textvariable=Msg, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtMsg.grid(row=1, column=1)
set_default_text(txtMsg, "Enter your message here")  # Set default text
txtMsg.bind("<FocusIn>", lambda event: clear_default_text(event, txtMsg, "Enter your message here"))
txtMsg.bind("<FocusOut>", lambda event: on_focus_out(event, txtMsg, "Enter your message here"))

# Entry for key
lblkey = Label(f1, font=('arial', 16, 'bold'), text="KEY (Only Integer)", bd=16, anchor="w")
lblkey.grid(row=2, column=0)
txtkey = Entry(f1, font=('arial', 16, 'bold'), textvariable=key, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtkey.grid(row=2, column=1)
set_default_text(txtkey, "Enter an integer key")  # Set default text
txtkey.bind("<FocusIn>", lambda event: clear_default_text(event, txtkey, "Enter an integer key"))
txtkey.bind("<FocusOut>", lambda event: on_focus_out(event, txtkey, "Enter an integer key"))

# Entry for mode
lblmode = Label(f1, font=('arial', 16, 'bold'), text="MODE(e for encrypt, d for decrypt)", bd=16, anchor="w")
lblmode.grid(row=3, column=0)
txtmode = Entry(f1, font=('arial', 16, 'bold'), textvariable=mode, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtmode.grid(row=3, column=1)
set_default_text(txtmode, "Enter 'e' for encrypt or 'd' for decrypt")  # Set default text
txtmode.bind("<FocusIn>", lambda event: clear_default_text(event, txtmode, "Enter 'e' for encrypt or 'd' for decrypt"))
txtmode.bind("<FocusOut>", lambda event: on_focus_out(event, txtmode, "Enter 'e' for encrypt or 'd' for decrypt"))

# Entry for result
lblResult = Label(f1, font=('arial', 16, 'bold'), text="The Result-", bd=16, anchor="w")
lblResult.grid(row=2, column=2)
txtResult = Entry(f1, font=('arial', 16, 'bold'), textvariable=Result, bd=10, insertwidth=4, bg="powder blue", justify='right')
txtResult.grid(row=2, column=3)

# Vigenère cipher
def encode(key, msg):
    try:
        enc = []
        for i in range(len(msg)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(msg[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()
    except Exception as e:
        return f"Error during encryption: {str(e)}"

def decode(key, enc):
    try:
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)
    except Exception as e:
        return f"Error during decryption: {str(e)}"

def Results():
    msg = Msg.get()
    k = key.get()
    m = mode.get()

    try:
        k = int(k)  # Convert key to integer
    except ValueError:
        messagebox.showerror("Error", "Key must be an integer.")
        return

    if m not in {'e', 'd'}:
        messagebox.showerror("Error", "Mode must be 'e' for encrypt or 'd' for decrypt.")
        return

    try:
        k_str = str(k)
        if m == 'e':
            Result.set(encode(k_str, msg))
        else:
            Result.set(decode(k_str, msg))

        root.update_idletasks()  # Update the GUI immediately
    except Exception as e:
        messagebox.showerror("Error", str(e))

def qExit():
    root.destroy()

def Reset():
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

# Show message button
btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Show Message", bg="powder blue", command=Results)
btnTotal.grid(row=7, column=1)

# Reset button
btnReset = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Reset", bg="green", command=Reset)
btnReset.grid(row=7, column=2)

# Exit button
btnExit = Button(f1, padx=16, pady=8, bd=16, fg="black", font=('arial', 16, 'bold'), width=10, text="Exit", bg="red", command=qExit)
btnExit.grid(row=7, column=3)

root.mainloop()
