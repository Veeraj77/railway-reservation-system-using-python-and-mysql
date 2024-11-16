import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime


# MySQL database connection
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="veeraj777",
        database="railway",
        auth_plugin="mysql_native_password"
    )

# Main Application Class
class TrainBookingApp:
    def __init__(self, root):  # Corrected to __init__
        self.root = root
        self.root.title("Train Booking System")
        self.root.geometry("1024x768")

        # Establish database connection once
        self.db_connection = connect_to_database()

        # Initialize frames
        self.frame1 = Frame1(self.root, self)
        self.frame2 = Frame2(self.root, self)
        self.frame3 = Frame3(self.root, self)

        # Show the first frame
        self.show_frame(self.frame1)

    def show_frame(self, frame):
        """Hide all frames and show the selected frame."""
        for f in (self.frame1, self.frame2, self.frame3):
            f.pack_forget()
        frame.pack(fill="both", expand=True)


# Frame 1: Train Booking System
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from PIL import Image, ImageTk
from datetime import datetime

class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)  # Initialize the parent frame
        self.controller = controller

        # Create a canvas to allow scrolling
        canvas = tk.Canvas(self, bg="#f5f5f5")  # Soft light gray canvas background
        canvas.pack(side="left", fill="both", expand=True)

        # Create a scrollbar and link it to the canvas
        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create a frame within the canvas to hold all content
        content_frame = tk.Frame(canvas, bg="#f5f5f5")  # Soft light gray background for content frame
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        # Configure the canvas scroll region dynamically
        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        # Load and display image at the top with rounded corners and a border
        img_path = r"C:/Users/veera/Downloads/vande-bharat-1440x680.jpg"
        try:
            img = Image.open(img_path)
            img = img.resize((1000, 400), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            image_label = tk.Label(content_frame, image=photo, bd=5, relief="solid", bg="#ffffff")
            image_label.image = photo  # Keep a reference to avoid garbage collection
            image_label.pack(pady=20, padx=20)
        except Exception as e:
            print(f"Error loading image: {e}")

        # Title with updated color scheme and larger font size
        title_label = tk.Label(content_frame, text="Train Booking System", font=("Helvetica", 30, "bold"), bg="#ffffff", fg="#005b7f")
        title_label.pack(pady=30)

        # City Information with updated text color and style
        city_info_label = tk.Label(content_frame, text="Explore popular cities across India:\nBangalore, Hyderabad, Delhi, Mumbai, Chennai, Kolkata",
                                   font=("Arial", 14), bg="#f5f5f5", fg="#333333", justify="center")
        city_info_label.pack(pady=20)

        # Main form frame with updated background color and padding
        form_frame = tk.Frame(content_frame, bg="#ffffff", bd=2, relief="solid", borderwidth=2, padx=20, pady=20)  # White background for form frame
        form_frame.pack(pady=20, padx=30, ipadx=10, ipady=20)

        # Dropdown options
        stations = ["Bangalore", "Hyderabad", "Delhi", "Mumbai", "Chennai", "Kolkata"]
        classes = ["General", "AC"]

        # From dropdown with enhanced visual
        tk.Label(form_frame, text="From", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333").grid(row=0, column=0, padx=15, pady=10, sticky="w")
        self.from_var = tk.StringVar(value=stations[0])
        from_menu = ttk.Combobox(form_frame, textvariable=self.from_var, values=stations, font=("Arial", 12), background="#e3f2fd")
        from_menu.grid(row=0, column=1, padx=10, pady=10)

        # To dropdown with enhanced visual
        tk.Label(form_frame, text="To", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333").grid(row=0, column=2, padx=15, pady=10, sticky="w")
        self.to_var = tk.StringVar(value=stations[1])
        to_menu = ttk.Combobox(form_frame, textvariable=self.to_var, values=stations, font=("Arial", 12), background="#e3f2fd")
        to_menu.grid(row=0, column=3, padx=10, pady=10)

        # Date picker with better styling
        tk.Label(form_frame, text="Date", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333").grid(row=1, column=0, padx=15, pady=10, sticky="w")
        self.date_var = tk.StringVar()
        date_entry = DateEntry(form_frame, textvariable=self.date_var, width=12, background="darkblue", foreground="white", font=("Arial", 12))
        date_entry.grid(row=1, column=1, padx=10, pady=10)

        # Class dropdown with better styling
        tk.Label(form_frame, text="Class", font=("Arial", 14, "bold"), bg="#ffffff", fg="#333333").grid(row=2, column=0, padx=15, pady=10, sticky="w")
        self.class_var = tk.StringVar(value=classes[0])
        class_menu = ttk.Combobox(form_frame, textvariable=self.class_var, values=classes, font=("Arial", 12), background="#e3f2fd")
        class_menu.grid(row=2, column=1, padx=10, pady=10)

        # Submit button with hover effect
        submit_btn = tk.Button(form_frame, text="Search", command=self.search_trains, bg="#388e3c", fg="white", font=("Arial", 14, "bold"))
        submit_btn.grid(row=2, column=3, padx=10, pady=20)

        # Button to view available trains
        available_trains_btn = tk.Button(content_frame, text="View Available Trains", command=lambda: controller.show_frame(controller.frame2), bg="#388e3c", fg="white", font=("Arial", 14, "bold"))
        available_trains_btn.pack(pady=20)

        # Tourist Deals section with rounded corners and shadow effect
        tourist_deals_frame = tk.Frame(content_frame, bg="#03a9f4", bd=2, relief="solid", borderwidth=2)  # Blue background for tourist deals
        tourist_deals_frame.pack(pady=30, padx=20, fill="both", expand=True)

        # Title for the tourist deals section
        tourist_deals_title_label = tk.Label(tourist_deals_frame, text="Discover top travel destinations and exclusive deals:", font=("Arial", 14, "bold"), bg="#03a9f4", fg="white", justify="left", padx=10, pady=10)
        tourist_deals_title_label.pack(fill="x")

        # Create a Text widget for the city deals section with improved colors
        city_deals_text = tk.Text(tourist_deals_frame, height=10, width=50, wrap="word", font=("Arial", 12), bg="#e1f5fe", fg="#004d40", bd=0, padx=10, pady=10)
        city_deals_text.pack(fill="both", expand=True)

        # Insert the text with city names and descriptions
        city_deals_text.insert(tk.END, """\n🌆 Bangalore: Enjoy the tech city with 'Weekend Getaway' discounts on group bookings.\n
        🍲 Hyderabad: Dive into 'Heritage & Food Tour' with cultural sites and cuisine.\n
        🏛 Delhi: Experience the 'Old Delhi City Tour' with guided historic site visits.\n
        🌊 Mumbai: Sail on a 'Coastal Cruise' combo for families with scenic sea views.\n
        🎶 Chennai: Explore with 'South Indian Heritage Tour' featuring music and temples.\n
        📚 Kolkata: Book the 'City of Joy' package to explore cultural richness at a special rate.\n""")

        # Set background color and text style
        city_deals_text.config(state=tk.DISABLED)  # Disable editing for this text

        # Contact Us section at the bottom
        contact_label = tk.Label(content_frame, text="📞 Contact Us\nFor inquiries and assistance, reach us at:\nEmail: support@trainbooking.com | Phone: +91-123-456-7890", font=("Arial", 12, "italic"), bg="#f5f5f5", fg="#2c6c4f", justify="center", pady=20)
        contact_label.pack()

    def search_trains(self):
        """Fetch available trains from the database based on criteria."""
        try:
            cursor = self.controller.db_connection.cursor(dictionary=True)

            # Get the selected date from DateEntry (mm/dd/yy format)
            selected_date = self.date_var.get()

            # Convert the date to yyyy-mm-dd format
            date_obj = datetime.strptime(selected_date, '%m/%d/%y')  # mm/dd/yy format
            formatted_date = date_obj.strftime('%Y-%m-%d')  # Convert to yyyy-mm-dd

            # Prepare the SQL query
            query = """
                SELECT * FROM train
                WHERE Source = %s AND Destination = %s AND Dates = %s
            """

            # Execute the query with parameters
            cursor.execute(query, (self.from_var.get(), self.to_var.get(), formatted_date))

            # Fetch the results
            results = cursor.fetchall()

            if results:
                self.controller.frame2.populate_trains(results)
                self.controller.show_frame(self.controller.frame2)
            else:
                messagebox.showinfo("No Results", "No trains found matching criteria.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        except ValueError as e:
            messagebox.showerror("Invalid Date", f"Invalid date format: {e}")
        finally:
            cursor.close()




# Frame 2: Display Available Trains
import tkinter as tk
from tkinter import ttk, messagebox


import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox


import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import messagebox, ttk


class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f4f7f6")  # Corrected method name and initialization
        self.controller = controller
        self.selected_train_id = None
        # To store the selected Train ID

        # About the App Section
        about_frame = tk.Frame(self, bg="#4caf50", bd=2, relief="solid")
        about_frame.pack(fill="x", padx=20, pady=10)

        about_label = tk.Label(about_frame, text="About the Train Booking System", font=("Arial", 14, "bold"),
                               fg="white", bg="#4caf50")
        about_label.pack(pady=5)

        about_content = """
        Welcome to the Train Booking System!
        This application allows you to search for trains, view train details, book and cancel tickets conveniently.
        Easily manage your reservations, check seat availability, and select from various travel classes.
        Follow the booking guidelines and enjoy a seamless travel experience.
        """
        about_text = tk.Label(about_frame, text=about_content, font=("Arial", 12), fg="white", bg="#4caf50",
                              justify="left", padx=10)
        about_text.pack(pady=5)

        # Guidelines Box
        guidelines_box = tk.Frame(self, bg="#e6f7ff", bd=2, relief="groove", padx=20, pady=20)
        guidelines_box.pack(padx=20, pady=10, fill="both", expand=True)

        guidelines_heading = tk.Label(guidelines_box, text="Train Booking Guidelines", font=("Arial", 16, "bold"),
                                      fg="#4caf50", bg="#e6f7ff")
        guidelines_heading.pack(pady=(0, 10))

        guidelines_content = """
        1. Please select a train from the list.
        2. Check the Departure Time and Arrival Time before booking.
        3. Ensure the date of travel is correct.
        4. You can proceed with booking or canceling your ticket after selecting the train.
        5. Use the 'Cancel Ticket' option if you want to cancel an existing booking.
        """
        guidelines_text = tk.Label(guidelines_box, text=guidelines_content, font=("Arial", 12), fg="#333333",
                                   bg="#e6f7ff", justify="left", padx=10)
        guidelines_text.pack(pady=5)

        # Table Frame
        table_frame = tk.Frame(self, bg="#e6f7ff", relief="groove", bd=2)
        table_frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Treeview (Table) setup
        self.train_table = ttk.Treeview(
            table_frame,
            columns=("TrainID", "TrainName", "Source", "Destination", "DepartureTime", "ArrivalTime", "TotalSeats", "dates"),
            show="headings",
            height=8
        )

        self.train_table.bind("<<TreeviewSelect>>", self.on_train_select)

        # Define the headings for each column
        self.train_table.heading("TrainID", text="Train ID")
        self.train_table.heading("TrainName", text="Train Name")
        self.train_table.heading("Source", text="Source")
        self.train_table.heading("Destination", text="Destination")
        self.train_table.heading("DepartureTime", text="Departure Time")
        self.train_table.heading("ArrivalTime", text="Arrival Time")
        self.train_table.heading("TotalSeats", text="Total Seats")
        self.train_table.heading("dates", text="Date")

        # Set column widths and center align
        self.train_table.column("TrainID", width=80, anchor="center")
        self.train_table.column("TrainName", width=150, anchor="center")
        self.train_table.column("Source", width=100, anchor="center")
        self.train_table.column("Destination", width=100, anchor="center")
        self.train_table.column("DepartureTime", width=120, anchor="center")
        self.train_table.column("ArrivalTime", width=120, anchor="center")
        self.train_table.column("TotalSeats", width=80, anchor="center")
        self.train_table.column("dates", width=100, anchor="center")

        # Scrollbar for the Treeview
        self.scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.train_table.yview)
        self.train_table.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        # Add table styling
        self.train_table.tag_configure('oddrow', background="#f0f0f0")
        self.train_table.tag_configure('evenrow', background="#ffffff")

        self.train_table.pack(fill="both", expand=True)

        # Style the header and table rows
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"), foreground="#333333", background="#e6f7ff")
        style.configure("Treeview", rowheight=25, font=("Arial", 10))

        # Button to go to passenger booking details
        booking_details_btn = tk.Button(self, text="Proceed to Booking",
                                        command=lambda: controller.show_frame(controller.frame3), bg="#28a745",
                                        fg="white", font=("Arial", 12))
        booking_details_btn.pack(pady=10)

        # Cancel Ticket button
        cancel_ticket_btn = tk.Button(self, text="Cancel Ticket", command=self.cancel_ticket, bg="#ff5733",
                                      fg="white", font=("Arial", 12))
        cancel_ticket_btn.pack(pady=10)

        # Footer Section
        footer_frame = tk.Frame(self, bg="#f4f7f6")
        footer_frame.pack(fill="x", pady=10)

        footer_label = tk.Label(footer_frame, text="For assistance, contact us at support@trainbooking.com",
                                font=("Arial", 10), fg="#333333", bg="#f4f7f6")
        footer_label.pack(pady=5)

    def populate_trains(self, trains):
        """Insert available trains into the table with alternating row colors."""
        for row in self.train_table.get_children():
            self.train_table.delete(row)

        for index, train in enumerate(trains):
            tag = 'oddrow' if index % 2 == 0 else 'evenrow'
            self.train_table.insert(
                "", "end", values=(
                    train["TrainID"], train["TrainName"], train["Source"], train["Destination"],
                    train["DepartureTime"], train["ArrivalTime"], train["TotalSeats"], train["dates"]
                ),
                tags=(tag,)
            )

    def on_train_select(self, event):
        """Get the TrainID of the selected row."""
        selected_item = self.train_table.selection()
        if selected_item:
            train_details = self.train_table.item(selected_item)
            self.selected_train_id = train_details["values"][0]  # First column (TrainID)
            self.controller.frame3.set_selected_train_for_booking(
                self.selected_train_id)  # Set selected train for booking
            print(f"Selected Train ID: {self.selected_train_id}")  # Debug: Print selected Train ID

    def cancel_ticket(self):
        """Cancel the ticket for the selected train."""
        if self.selected_train_id is None:
            messagebox.showerror("Cancel Failed", "Please select a train first.")
            return

        # Go to the booking form with the selected train
        self.controller.frame3.set_selected_train_for_cancellation(self.selected_train_id)
        self.controller.show_frame(self.controller.frame3)






# Frame 3: Ticket Booking and Cancellation
import tkinter as tk
from tkinter import ttk, messagebox

import tkinter as tk
from tkinter import messagebox, ttk

import tkinter as tk
from tkinter import messagebox, ttk
from tkinter.scrolledtext import ScrolledText


class Frame3(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#e0f7fa")  # Corrected method name and fixed initialization
        self.controller = controller

        # Frame content goes here
        self.label = tk.Label(self, text="This is Frame 3")
        self.label.pack()

        # Add additional components for Frame3 as needed

        # Scrollable Frame setup
        canvas = tk.Canvas(self, bg="#e0f7fa", highlightthickness=0)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="#e0f7fa")
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Title
        title_label = tk.Label(
            scrollable_frame, text="Book Ticket / Cancel Ticket",
            font=("Arial", 20, "bold"), fg="#005662", bg="#e0f7fa"
        )
        title_label.pack(pady=(20, 10))

        # Guidelines Section
        guidelines_frame = tk.Frame(scrollable_frame, bg="#00796b", bd=2, relief="ridge", padx=10, pady=10)
        guidelines_frame.pack(pady=10, padx=20, fill="x")

        guidelines_label = tk.Label(
            guidelines_frame, text="Booking & Cancellation Guidelines",
            font=("Arial", 16, "bold"), fg="white", bg="#00796b"
        )
        guidelines_label.pack(pady=5)

        guidelines_content = """
        1. Enter your details in the booking form to book a ticket.
        2. Ensure all required fields are filled before submission.
        3. To cancel your ticket, enter the Passenger ID provided at booking.
        4. Cancellations are only allowed if the ticket exists in the system.
        5. After booking, seat availability will be automatically updated.
        6. Successful bookings will display a confirmation message.
        7. Please note: Alcohol and smoking are strictly prohibited on all trains.
        8. Passengers should carry a valid ID for verification during travel.
        """
        guidelines_text = tk.Label(
            guidelines_frame, text=guidelines_content, font=("Arial", 12),
            fg="white", bg="#00796b", justify="left"
        )
        guidelines_text.pack(pady=5)

        # Discount Advertisement
        ad_frame = tk.Frame(scrollable_frame, bg="#ffecb3", bd=2, relief="ridge", padx=10, pady=10)
        ad_frame.pack(pady=10, padx=20, fill="x")

        ad_label = tk.Label(
            ad_frame, text="Special Discounts on Train Bookings!",
            font=("Arial", 16, "bold"), fg="#6b4207", bg="#ffecb3"
        )
        ad_label.pack(pady=5)

        ad_content = """
        Limited time offer! Book your tickets now and enjoy up to 20% off on selected routes.
        Use code TRAIN20 at checkout. Hurry, offer ends soon!
        """
        ad_text = tk.Label(
            ad_frame, text=ad_content, font=("Arial", 12), fg="#6b4207", bg="#ffecb3", justify="left"
        )
        ad_text.pack(pady=5)

        # Passenger Information Form
        form_frame = tk.Frame(scrollable_frame, bg="white", bd=2, relief="groove", padx=10, pady=10)
        form_frame.pack(pady=20, padx=50, ipadx=20, ipady=20, fill="x", expand=True)

        # Define Variables at the beginning
        self.first_name_var = tk.StringVar()
        self.last_name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar(value="Male")
        self.phone_var = tk.StringVar()
        self.berth_pref_var = tk.StringVar(value="Lower")
        self.passenger_id_var = tk.StringVar()
        self.selected_train_id = None
        # Form Labels and Entry Fields
        self.create_form_row(form_frame, "First Name", 0, self.first_name_var)
        self.create_form_row(form_frame, "Last Name", 1, self.last_name_var)
        self.create_form_row(form_frame, "Age", 2, self.age_var)

        tk.Label(form_frame, text="Gender", font=("Arial", 10), bg="white").grid(row=3, column=0, padx=10, pady=5)
        gender_menu = ttk.Combobox(form_frame, textvariable=self.gender_var, values=["M", "F", "O"])
        gender_menu.grid(row=3, column=1, padx=10, pady=5)

        self.create_form_row(form_frame, "Phone No", 4, self.phone_var)

        tk.Label(form_frame, text="Berth Preference", font=("Arial", 10), bg="white").grid(row=5, column=0, padx=10,
                                                                                           pady=5)
        berth_menu = ttk.Combobox(form_frame, textvariable=self.berth_pref_var, values=["Lower", "Middle", "Upper"])
        berth_menu.grid(row=5, column=1, padx=10, pady=5)

        # Book Ticket Button
        submit_btn = tk.Button(
            form_frame, text="Book Ticket", command=self.book_ticket,
            bg="#0288d1", fg="white", font=("Arial", 12, "bold"), width=15, relief="ridge"
        )
        submit_btn.grid(row=6, column=1, pady=15)

        # Passenger ID for Cancellation
        self.create_form_row(form_frame, "Passenger ID (for cancellation)", 7, self.passenger_id_var)

        # Cancel Ticket Button
        cancel_ticket_btn = tk.Button(
            form_frame, text="Cancel Ticket", command=self.cancel_ticket,
            bg="#d32f2f", fg="white", font=("Arial", 12, "bold"), width=15, relief="ridge"
        )
        cancel_ticket_btn.grid(row=8, column=1, pady=15)

        # Contact Us Section
        contact_frame = tk.Frame(scrollable_frame, bg="#e0f7fa", bd=2, relief="ridge", padx=10, pady=10)
        contact_frame.pack(pady=10, padx=20, fill="x")

        contact_label = tk.Label(
            contact_frame, text="Contact Us", font=("Arial", 14, "bold"), fg="#005662", bg="#e0f7fa"
        )
        contact_label.pack(pady=5)

        contact_content = """
        For booking or cancellation inquiries, please contact our support:
        Email: support@trainbooking.com
        Phone: +1 800 123 4567
        Customer Service Hours: 9 AM - 6 PM (Mon-Fri)
        """
        contact_text = tk.Label(
            contact_frame, text=contact_content, font=("Arial", 12), fg="#333", bg="#e0f7fa", justify="left"
        )
        contact_text.pack(pady=5)

    # Keep the existing create_form_row, book_ticket, and cancel_ticket methods unchanged

    def create_form_row(self, frame, label_text, row, var):
        """Helper function to create form rows with label and entry widget."""
        tk.Label(frame, text=label_text, font=("Arial", 10), bg="white").grid(row=row, column=0, padx=10, pady=5)
        ttk.Entry(frame, textvariable=var).grid(row=row, column=1, padx=10, pady=5)

    def set_selected_train_for_booking(self, train_id):
        self.selected_train_id = train_id

    def set_selected_train_for_cancellation(self, train_id):
        self.selected_train_id = train_id



    def book_ticket(self):
        """Book the ticket by inserting the passenger details into the database."""
        try:
            cursor = self.controller.db_connection.cursor()

            # Validate user inputs
            if not self.first_name_var.get() or not self.last_name_var.get() or not self.age_var.get() or not self.phone_var.get():
                messagebox.showerror("Input Error", "Please fill all the required fields.")
                return

            # Get the entered passenger details
            first_name = self.first_name_var.get()
            last_name = self.last_name_var.get()
            age = self.age_var.get()
            gender = self.gender_var.get()
            phone_number = self.phone_var.get()
            berth_preference = self.berth_pref_var.get()
            train_id = self.selected_train_id

            # Insert into the passenger table
            cursor.execute(""" 
                INSERT INTO passenger (FirstName, LastName, Age, Gender, PhoneNumber, BerthPreference, TrainID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (first_name, last_name, age, gender, phone_number, berth_preference, train_id))

            # Commit the transaction
            self.controller.db_connection.commit()

            # Update the total seats of the train (decrement by 1)
            cursor.execute(""" 
                UPDATE train SET TotalSeats = TotalSeats - 1 WHERE TrainID = %s
            """, (train_id,))
            self.controller.db_connection.commit()

            messagebox.showinfo("Booking Successful", "Your ticket has been successfully booked!")
            self.controller.show_frame(self.controller.frame1)  # Go back to the main screen

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error while booking ticket: {e}")
        finally:
            cursor.close()

    def cancel_ticket(self):
        """Cancel the selected train ticket by deleting the passenger details."""
        passenger_id = self.passenger_id_var.get()  # Get input from the passenger ID field

        # Check if Passenger ID is provided
        if not passenger_id:
            messagebox.showwarning("No Passenger Selected", "Please enter the Passenger ID to cancel the ticket.")
            return

        try:
            cursor = self.controller.db_connection.cursor()

            # Query to check if the passenger exists in the 'passenger' table
            cursor.execute(""" 
                SELECT TrainID FROM passenger WHERE PassengerID = %s
            """, (passenger_id,))
            passenger = cursor.fetchone()

            if passenger:
                train_id = passenger[0]

                # Query to delete passenger details from the 'passenger' table based on the given passenger_id
                delete_query = """ 
                    DELETE FROM passenger WHERE PassengerID = %s
                """
                cursor.execute(delete_query, (passenger_id,))
                self.controller.db_connection.commit()

                # Update the total seats of the train (increment by 1 since a seat is being freed)
                update_query = """ 
                    UPDATE train SET TotalSeats = TotalSeats + 1 WHERE TrainID = %s
                """
                cursor.execute(update_query, (train_id,))
                self.controller.db_connection.commit()

                # Check if any row was deleted
                if cursor.rowcount > 0:
                    messagebox.showinfo("Cancellation Success", "The ticket has been canceled successfully.")
                else:
                    messagebox.showwarning("Cancellation Success", "The ticket has been canceled successfully.")

            else:
                messagebox.showwarning("No Matching Record", "No passenger found with the provided ID.")

        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Database error: {e}")
        finally:
            cursor.close()


if __name__ == "__main__":
    root = tk.Tk()
    app = TrainBookingApp(root)
    root.mainloop()
