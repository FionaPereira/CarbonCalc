import tkinter as tk
from tkinter import messagebox
import requests


ingredients = requests.get('https://www.vegansociety.com/sites/default/files/uploads/Campaigns/PlateUp/ingredients-updated-3.json').json()
#stores ingredients into JSON object
                           
def list_to_dict(lis):
    #returns dictionary of ingredients and carbon footprint
    ingredient_dict = {}
    for item in lis:
        ingredient_dict[item['FOOD']] = item
    return ingredient_dict

def window_display():
    
    def refresh_ingredients(val):
        '''Refreshes ingredients dropdown menu
        
                Parameter: val (str): user selected food group
                Returns: updated dropdown options with all ingredients within food group
        '''
        group_ingredients = {k:v for (k,v) in ingredients_dict.items() if v['Group'] == val}
        food_list = tk.OptionMenu(root, food_list_button, *group_ingredients, command=refresh_region)
        food_list.grid(row = 0, column = 1, padx=50)
        food_list_button.set('Select Ingredient')
        
    
    def refresh_region(val):
        '''Refreshes region dropdown menu
        
                Parameter: val (str): user selected ingredient
                Returns: updated dropdown options with source options
        '''
        nonlocal current_ingredient
        current_ingredient = ingredients_dict[val]
        sources_list = current_ingredient.copy()
        
        del sources_list['FOOD']
        del sources_list['Group']
        
        sources_list = list(sources_list.keys())
        
        region_list_button.set('Select its source')
        region_list = tk.OptionMenu(root, region_list_button, *sources_list, command=update_region)
        region_list.grid(row = 0, column = 2)
        
    def update_region(val):
        nonlocal region
        region = val
    

    def refresh_footprint():
        # Updates the running table of user ingredient selections
        
        nonlocal current_ingredient
        nonlocal region
        nonlocal user_selections
        nonlocal height
        
        if g_input.get() == 'warwickhack2021':
            messagebox.showinfo(title='WarwickHack2021', message='CONGRATULATIONS - you have found our secret easter egg!! \n Happy carbon footprint calculating!!')
            return
        try:
            float(g_input.get())
        except:
             messagebox.showerror(title='ERROR', message='Please only enter a number')
             return
        
        footprint = round(current_ingredient[region] * (float(g_input.get())/1000), 2)
        current = [current_ingredient['FOOD'], g_input.get(), region, footprint]
        user_selections.append([current_ingredient['FOOD'], g_input.get(), region, footprint])
        
        height += 1
        for item in current: #Columns
            b = tk.Label(root, text=item)
            b.grid(row=height, column=current.index(item))
    
    def refresh_total():
        '''Calculates total CO2e and milage equivalent
        
                Parameter: none
                Returns: String to user with CO2e and milage equivalent
        '''
        nonlocal user_selections
        nonlocal height
        nonlocal add_button
        nonlocal total_button
        total_footprint = [float(item[3]) for item in user_selections]
        total_footprint = round(sum(total_footprint), 2)
        car_miles = 0
        car_miles = "{:.2f}".format(total_footprint/0.392)
        result_text = f"Your food's carbon footprint is {total_footprint} CO2e. That's equivalent to a {car_miles} mile car journey!!"
        total_label = tk.Label(root, text=result_text)
        total_label.grid(row=height+1, column=0, columnspan=4, pady=20)
        add_button['state'] = tk.DISABLED
        total_button['state'] = tk.DISABLED
        
    def reset_screen():
        
        root.destroy()
        window_display()
        
        
        

    current_ingredient = {}     
    ingredients_dict = list_to_dict(ingredients)
    ingredients_list = [food for food in ingredients_dict.keys()]
    group_list = [item['Group'] for item in ingredients]
    group_list = set(group_list)
    group_list = list(group_list)
    region = 'works'
    sources_list = ['']
    height = 4 #for table
    user_selections = []

    
    root = tk.Tk()
    root.title('Carbon Footprint Calculator')
    root.geometry("1000x700+500+180")
    
    group_list_button = tk.StringVar(root)
    group_list_button.set('Select Group')
    group_list = tk.OptionMenu(root, group_list_button, *group_list, command=refresh_ingredients)
    group_list.grid(row=0,column=0, padx=50, pady=50)
    
    food_list_button = tk.StringVar(root)
    food_list_button.set('Select Ingredient')
    food_list = tk.OptionMenu(root, food_list_button, *ingredients_list, command=refresh_region)
    food_list.grid(row = 0, column = 1, padx=50)
    
    region_list_button = tk.StringVar(root)
    region_list_button.set('Select its source')
    region_list = tk.OptionMenu(root, region_list_button, *sources_list, command=update_region)
    region_list.grid(row = 0, column = 2, padx=50)
    region_list.grid_forget() 
   
    g_input = tk.Entry(root)
    g_input.insert(0, '1')
    g_input.grid(row = 1, column = 0)
    g_label = tk.Label(root, text = 'g')
    g_label.grid(row = 1, column = 1, sticky = 'W', pady=75)
    
    add_button = tk.Button(root, text='Add', command = refresh_footprint)
    add_button.grid(row=1,column=2, sticky = 'W')
    
    total_button = tk.Button(root, text='Calculate Total', command=refresh_total)
    total_button.grid(row=1, column=3, sticky='W')
    
    reset_button = tk.Button(root, text='Reset', command=reset_screen)
    reset_button.grid(row=1, column=4)
                             
    
    #Outputs list of user selected ingredients with carbon footprint value
    header = ['Ingredient', 'Amount (in g)', 'Region', 'Carbon footprint (CO2e)']
    for item in header: #Columns
            b = tk.Label(root, text=item)
            b.grid(row=height, column=header.index(item), pady=20)

    tk.mainloop()

window_display()


