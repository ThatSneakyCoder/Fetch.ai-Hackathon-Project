# Fetch.ai-Hackathon-Project

# Currency Checker:
Sends notification on Linux OS whenvever the user conditions matches with the currency rate.


## Packages Used:
1. tkinter (for gui)
2. Forex API (for currency)
3. Plyer (for sending notification)  
4. Fetch AI


## How to use:
1. Run Command 'poetry install'
2. Run Command 'python3 fetchai/currency_checker_module.py'
3. GUI will appear.![image-1](https://github.com/shubh220922/Fetch.ai-Hackathon-Project/assets/90137881/d97810a7-0e31-4818-b4c4-333d571b1c95)
4. Enter the number of converters and click on add
5. Enter the details/conditions and submit.
6. Whenever the conditions match you get notification
![image](https://github.com/shubh220922/Fetch.ai-Hackathon-Project/assets/90137881/1c262ed8-6027-4245-b81c-3bbedd210d05)

## How it works:
1. Running 'currency_checker_module.py' will run 'gui_interface'
2. On entering details and clicking on submit will start the agent- currency_checker.
3. currency_checker agent  will run for every 5 seconds with which will call forex API.
4. Whenever the conditions match you get notification
