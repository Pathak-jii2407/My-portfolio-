import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
from pytrends.request import TrendReq
from datetime import datetime, timedelta
import random

from Load_logo import root_logo

def get_realtime_trending(country_code):
    timeout = 0
    while timeout < 5:
        try:
            pytrend = TrendReq()
            real_trending = pytrend.realtime_trending_searches(pn=country_code)
            return real_trending['title'].head(5), real_trending['entityNames'].head(5)
        except Exception as e:
            print("Error fetching real-time trending:", e)
            timeout += 1
            btn_show_trend.config(text='Processing')

def get_trend(search_query, country_code, start_date, end_date, use_grid):
    timeout = 0
    while timeout < 7:
        try:
            pytrend = TrendReq()
            if not start_date or not end_date:
                end_date = datetime.now().strftime('%Y-%m-%d')
                start_date = (datetime.now() - timedelta(days=5*365)).strftime('%Y-%m-%d')
            pytrend.build_payload(search_query, geo=country_code, timeframe=f'{start_date} {end_date}')
            interest = pytrend.interest_over_time()
            interest = interest.fillna(False)
            return interest
        except Exception as e:
            if '' in search_query:
                print('ok')
                break
            print("Error fetching trend data:")
            timeout += 1
            btn_show_trend.config(text='Processing')


def show_trend():
    error_label.config(text='')  
    search_query = entry_search.get().split(',')   
    country_code = country_var.get().upper()
    start_date = entry_start_date.get()
    end_date = entry_end_date.get()
    use_grid = grid_var.get()
    plot_type = plot_type_var.get()
    btn_show_trend.config(text="Retry")
    btn_show_trend.config(fg='red')
    interest = get_trend(search_query, country_code, start_date, end_date, use_grid)
    btn_show_trend.config(text="Show Trend")
    if interest is not None:
        show(interest, search_query, use_grid, plot_type)

def display_trending():
    error_label.config(text='')  
    country_code = country_var.get().upper()
    btn_display_trending.config(text="Processing...")
    real_trending_titles, real_trending_entities = get_realtime_trending(country_code)
    btn_display_trending.config(text="Display Trending Searches")
    if real_trending_titles is not None:
        trending_list.delete(0, END)
        for title, entity in zip(real_trending_titles, real_trending_entities):
            trending_list.insert(END, f"{title} -- {entity[:20]}")

def clear_outputs():
    trending_list.delete(0, END)
    
canvas = None  

def clear_plot():
    global canvas
    if canvas:
        canvas.get_tk_widget().destroy()

def show(interest, data, use_grid, plot_type):
    global canvas
    clear_plot()

    fig, ax = plt.subplots()
    if plot_type == "Line Plot":
        for i in range(len(data)):
            ax.plot(interest.index, interest[data[i]], label=data[i])

    elif plot_type == "Scatter Plot":
        for i in range(len(data)):
            ax.scatter(interest.index, interest[data[i]], label=data[i])

    elif plot_type == "Area Plot":
        for i in range(len(data)):
            ax.fill_between(interest.index, interest[data[i]], label=data[i])
    else:
        for i in range(len(data)):
            ax.plot(interest.index, interest[data[i]], label=data[i])

    ax.set_xlabel('Date', fontsize=12, fontweight='bold', color='blue')
    ax.set_ylabel("Interest over time", fontsize=12, fontweight='bold', color='blue')
    ax.legend(loc='upper right', fontsize=10)
    
    if use_grid:
        ax.grid(True, linestyle='--', linewidth=0.5)
    else:
        ax.grid(False)

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=RIGHT, fill=BOTH, expand=True)


root = Tk()
root.title("Real-time Trending Searches and Trend Plot")
root.configure(bg='gray')

try:
    logo=root_logo()
    root.iconphoto(True, logo)
except:
    pass

trending_frame = Frame(root,background='lightsteelblue')
trending_frame.pack(side=LEFT, padx=10, pady=10)

label_clear_outputs = Label(trending_frame, text='Clear Outputs:', font=('Helvetica', 12, 'bold'), bg='lightyellow')
label_clear_outputs.grid(row=0, column=0, sticky=W)
btn_clear_outputs = Button(trending_frame, text='Clear', command=clear_outputs, font=('Helvetica', 12), bg='white')
btn_clear_outputs.grid(row=0, column=1, sticky=W)

label_country = Label(trending_frame, text='Country Code: ', font=('Helvetica', 12, 'bold'), bg='lightyellow')
label_country.grid(row=1, column=0, sticky=W)
countries = ['IN', 'US', 'IT', 'UK', 'FR', 'JP', 'CN', 'BR', 'CA']
country_var = StringVar(root)
country_var.set(countries[random.randint(0, 8)]) 
country_dropdown = OptionMenu(trending_frame, country_var, *countries)
country_dropdown.grid(row=1, column=1,padx=150,pady=10)

btn_display_trending = Button(trending_frame, text='Display Trending Searches', command=display_trending, font=('Helvetica', 12), bg='white')
btn_display_trending.grid(row=2, columnspan=2,padx=150,pady=10)

trending_list = Listbox(trending_frame, height=15,width=50,font=('Arial', 12))
trending_list.grid(row=3, columnspan=2)

plot_frame = Frame(root,bg='palegreen')
plot_frame.pack(side=RIGHT, padx=10, pady=10, fill=BOTH, expand=True)

label_search = Label(plot_frame, text='Search Queries (comma-separated): ', font=('Helvetica', 12, 'bold'))
label_search.pack()

entry_search = Entry(plot_frame, font=('Helvetica', 10,'bold'),border=2,highlightthickness=1,highlightbackground='black',highlightcolor='lightblue')
entry_search.pack()


label_dates = Label(plot_frame, text='Start Date (YYYY-MM-DD)', font=('Helvetica', 12, 'bold'))
label_dates.pack(side='top')

entry_start_date = Entry(plot_frame, font=('Helvetica', 10,'bold'),border=2,highlightthickness=1,highlightbackground='black',highlightcolor='lightblue')
entry_start_date.pack()
label_dates = Label(plot_frame, text='End Date (YYYY-MM-DD)', font=('Helvetica', 12, 'bold'))
label_dates.pack()
entry_end_date = Entry(plot_frame, font=('Helvetica', 10,'bold'),border=2,highlightthickness=1,highlightbackground='black',highlightcolor='lightblue')
entry_end_date.pack()

grid_var = BooleanVar(root)
grid_checkbox = Checkbutton(plot_frame, text="Show Grid", variable=grid_var, font=('Helvetica', 12, 'bold'), bg='lightgray')
grid_checkbox.pack()

label_plot_type = Label(plot_frame, text='Select Plot Type:', font=('Helvetica', 12, 'bold'))
label_plot_type.pack()
plot_types = ["Line Plot", "Scatter Plot", "Area Plot"]
plot_type_var = StringVar(root)
plot_type_var.set(plot_types[0])  
plot_type_dropdown = OptionMenu(plot_frame, plot_type_var, *plot_types)
plot_type_dropdown.pack()

btn_show_trend = Button(plot_frame, text='Show Trend', command=show_trend, font=('Helvetica', 12), bg='white')
btn_show_trend.pack()

error_label = Label(root, fg='red', font=('Helvetica', 12, 'bold'))
error_label.pack()

root.mainloop()
