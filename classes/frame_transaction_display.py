import tkinter as tk
from classes.auction import Auction

class TransactionDisplay(tk.Frame):

    def __init__(self, parent, auction):
        tk.Frame.__init__(self, parent)
        self.auction = auction

        # Create heading label.
        label_heading = tk.Label(self, text="Latest transactions:", font='none 10 bold')
        label_heading.grid(row=0, column=0, sticky='w')

        # Create label to hold the transactions list.
        self.label_transactions = tk.Label(self, justify=tk.LEFT)
        self.label_transactions.grid(row=1, column=0, sticky='w')

    def get_latest_transactions(self):
        # Get last 10 transactions and reverse them.
        latest_transactions_list = self.auction.transaction_log[-10:][::-1]
        # Format them into a string.
        latest_transaction_string = ""
        for t in latest_transactions_list:
            t_formatted = f"Team {t['team'].name} bought player {t['player']['simple_name_raw']} " \
                          f"({t['player']['position']}, {t['player']['club']}) for £{t['price']}m.\n"
            latest_transaction_string += t_formatted
        # Add the string as the text of the transactions label.
        self.label_transactions['text'] = latest_transaction_string
        return latest_transaction_string
    pass

if __name__ == "__main__":
    # test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    test_list = [1, 2, 3, 4]
    latest_list = test_list[-5:][::-1]
    print(latest_list)

    # root = tk.Tk()
    # auction = Auction()
    # test_frame = TransactionDisplay(root, auction)
    # test_frame.pack()
    # root.mainloop()

